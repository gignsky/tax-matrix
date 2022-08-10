"""
    class containing information about the subject property
"""

from . import Printer
from . import LogicalWork

class Property:
    def __init__(self):
        self.price_int = None
        self.price_str = None
        self.county = None
        self.FINAL_TAX_COST = 0.0

    def add_price(self, price_int, price_str):
        self.price_int = price_int
        self.price_str = price_str
        Printer.print_green(f"The Price of {price_str} has been loaded to subject!")

    def get_price_str(self):
        # Printer.print_green(f"Price String: {self.price_str}")
        return self.price_str

    def get_price_int(self):
        # Printer.print_green(f"Price Integer: {self.price_int}")
        return self.price_int

    def add_county(self, county):
        self.county = county
        Printer.welcome_county(self.county.get_county_name())

    def get_county(self):
        return self.county

    def add_statistics(self, statistics):
        self.statistics = statistics

    def add_city(self, city):
        self.county.add_city(city)

    def print_current_stats(self):
        Printer.print_green("Current statistics to be added to final statement:")
        Printer.print_yellow(f"Current Subject Price: {self.price_str}")
        self.county.print_county_selected_info()
        if self.county.city is None:
            Printer.short_liner()
            Printer.print_red("No City has been Selected")
            Printer.short_liner()
        else:
            Printer.short_liner()
            self.county.city.print_modifiable_info()
            Printer.short_liner()

    def generate_statistics(self):
        self.statistics = {}
        self.statistics["COUNTY"] = self.county.generate_county_statistics()
        if self.county.city is None:
            self.statistics["CITY"] = None
        else:
            self.statistics["CITY"] = self.county.city.generate_city_statistics()

    def generate_post_price_statement(self):
        county_keys, county_values = LogicalWork.no_index_dict_to_two_lists(
            self.statistics["COUNTY"]
        )

        self.generate_total_multiply_rate()
        self.generate_total_tax_burden_after_rate()
        self.COUNTYWIDE_ONLY = LogicalWork.check_countywide_only(
            self.statistics["COUNTY"]
        )

        if self.CITY_EXISTS:
            city_keys, city_values = LogicalWork.no_index_dict_to_two_lists(
                self.statistics["CITY"]
            )
        else:
            city_keys = None
            city_values = None

        self.CONTAINS_FEES = self.check_contains_fees_ALL(
            county_keys, county_values, city_keys, city_values
        )

        (
            county_ONLY_statement,
            items_added,
        ) = self.county.generate_county_ONLY_statement_NO_fee()

        middle_statement = self.generate_middle_statement(
            county_ONLY_statement, items_added
        )

        return_statement = self.generate_return_statement_AND_check_fee(
            county_keys, county_values, city_keys, city_values, middle_statement
        )

        return return_statement

    def generate_return_statement_AND_check_fee(
        self, county_keys, county_values, city_keys, city_values, middle_statement
    ):
        if not self.CONTAINS_FEES:  # no fees
            return_statement = f"x {middle_statement}"

        else:
            fees = self.generate_ALL_fees(
                county_keys, county_values, city_keys, city_values
            )
            self.generate_total_tax_burden_after_fee(fees)
            return_statement = f"x {middle_statement}{self.generate_ALL_fee_strings(county_keys, county_values, city_keys, city_values)} = {self.generate_total_tax_burden_str()}"
        return return_statement

    def check_contains_fees_ALL(
        self, county_keys, county_values, city_keys, city_values
    ):
        county_has_fees = self.county.check_contains_fees(county_keys, county_values)
        if city_keys is not None:
            city_has_fees = self.county.city.check_contains_fees(city_keys, city_values)
        else:
            city_has_fees = False

        if county_has_fees or city_has_fees:
            return True
        else:
            return False

    def generate_middle_statement(self, county_ONLY_statement, items_added):
        if self.WITH_COUNTY_NO_CITY:
            if items_added == 1:
                middle_statement = (
                    f"{county_ONLY_statement} = {self.generate_total_tax_burden_str()}"
                )
            else:
                middle_statement = f"{self.multiply_rate:.6g} ({county_ONLY_statement}) = {self.generate_total_tax_burden_str()}"

        else:  # has city rates
            # city_ONLY_statement = self.county.city.city_ONLY_statement()

            city_substatement = self.county.city.generate_CITY_substatements(
                self.statistics["CITY"], self.WITH_COUNTY_NO_CITY, self.CITY_EXISTS
            )

            middle_statement = f"{self.multiply_rate:.6g} ({county_ONLY_statement}{city_substatement}) = {self.generate_total_tax_burden_str()}"

        return middle_statement

    def generate_total_multiply_rate(self):
        # set inital values
        self.multiply_rate = 0.0

        # add county rate
        county_keys, county_values = LogicalWork.no_index_dict_to_two_lists(
            self.statistics["COUNTY"]
        )
        self.multiply_rate = self.county.generate_county_multiply_rate(
            county_keys, county_values
        )

        # check city exists
        self.CITY_EXISTS = LogicalWork.check_city_exists(self.statistics["CITY"])

        # add city rates if they exist and set self.WITH_COUNTY_NO_CITY
        if self.CITY_EXISTS:
            _, city_values = LogicalWork.no_index_dict_to_two_lists(
                self.statistics["CITY"]
            )
            for i in list(filter(None, city_values)):
                i_key = list(i)[0]
                if "Fee" not in i_key:
                    self.multiply_rate += i[i_key]
            self.WITH_COUNTY_NO_CITY = False
        else:
            self.WITH_COUNTY_NO_CITY = True

    def generate_total_tax_burden_str(self):
        return f"${self.FINAL_TAX_COST:,.0f}"

    def generate_total_tax_burden_after_rate(self):
        self.FINAL_TAX_COST = self.price_int * self.multiply_rate

    def generate_total_tax_burden_after_fee(self, fee):
        self.FINAL_TAX_COST += fee

    def generate_ALL_fee_strings(
        self, county_keys, county_values, city_keys, city_values
    ):
        county_fee_string = self.county.generate_county_fees_string(
            county_keys, county_values
        )
        if self.CITY_EXISTS:
            city_fee_string = self.county.city.generate_city_fees_string(
                city_keys, city_values
            )
        else:
            city_fee_string = ""

        return county_fee_string + city_fee_string

    def generate_ALL_fees(self, county_keys, county_values, city_keys, city_values):
        county_fees = self.county.generate_county_total_fees(county_keys, county_values)
        if self.CITY_EXISTS:
            city_fees = self.county.city.generate_city_total_fees(
                city_keys, city_values
            )
        else:
            city_fees = 0

        return county_fees + city_fees
