"""
    class containing information about the subject property
"""

from . import Printer
from . import LogicalWork

class Property:
    """
        Class for generic Property
    """
    def __init__(self):
        self.price_int = None
        self.price_str = None
        self.county = None
        self.final_tax_cost = 0.0

        #inital declarations
        self.statistics=None
        self.countywide_only=None
        self.contains_fees=None
        self.multiply_rate=None
        self.city_exists=None
        self.with_county_no_city=None

    #add items
    def add_price(self, price_int, price_str):
        """
        add_price add price to subject

        Args:
            price_int (int): int version of price
            price_str (str): str version of price
        """
        self.price_int = price_int
        self.price_str = price_str
        Printer.print_green(f"The Price of {price_str} has been loaded to subject!")

    def add_county(self, county):
        """
        add_county add county to subject

        Args:
            county (obj): county object
        """
        self.county = county
        Printer.welcome_county(self.county.get_county_name())

    def add_statistics(self, statistics):
        """
        add_statistics to property

        Args:
            statistics (dict): dictionary with statistics for subject
        """
        self.statistics = statistics

    def add_city(self, city):
        """
        add_city add city to county object inside subject

        Args:
            city (obj): city object
        """
        self.county.add_city(city)

    #get items
    def get_price_str(self):
        """
        get_price_str

        Returns:
            str: str version of price
        """
        # Printer.print_green(f"Price String: {self.price_str}")
        return self.price_str

    def get_price_int(self):
        """
        get_price_int

        Returns:
            int: int version of price
        """
        # Printer.print_green(f"Price Integer: {self.price_int}")
        return self.price_int

    def get_county(self):
        """
        get_county object

        Returns:
            obj: county object
        """
        return self.county

    #printing
    def print_current_stats(self):
        """
        print_current_stats
        """
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

    #logical
    def check_contains_fees_all(
        self, county_keys, county_values, city_keys, city_values
    ):
        """
        check_contains_fees_ALL check if fees exist

        Args:
            county_keys (list): county key list
            county_values (list): county values list
            city_keys (list): city keys list
            city_values (list): city values list

        Returns:
            bool: true / false
        """
        county_has_fees = self.county.check_contains_fees(county_keys, county_values)
        if city_keys is not None:
            city_has_fees = self.county.city.check_contains_fees(city_keys, city_values)
        else:
            city_has_fees = False

        if county_has_fees or city_has_fees:
            return True
        else:
            return False

    #generate items
    def generate_statistics(self):
        """
        generate_statistics
        """
        self.statistics = {}
        self.statistics["COUNTY"] = self.county.generate_county_statistics()
        if self.county.city is None:
            self.statistics["CITY"] = None
        else:
            self.statistics["CITY"] = self.county.city.generate_city_statistics()

    def generate_post_price_statement(self):
        """
        generate_post_price_statement string post the price in the final statement

        Returns:
            str: output string for statement after the price is entered
        """
        county_keys, county_values = LogicalWork.no_index_dict_to_two_lists(
            self.statistics["COUNTY"]
        )

        self.generate_total_multiply_rate()
        self.generate_total_tax_burden_after_rate()
        self.countywide_only = LogicalWork.check_countywide_only(
            self.statistics["COUNTY"]
        )

        if self.city_exists:
            city_keys, city_values = LogicalWork.no_index_dict_to_two_lists(
                self.statistics["CITY"]
            )
        else:
            city_keys = None
            city_values = None

        self.contains_fees = self.check_contains_fees_all(
            county_keys, county_values, city_keys, city_values
        )

        (
            county_only_statement,
            items_added,
        ) = self.county.generate_county_only_statement_no_fee()

        middle_statement = self.generate_middle_statement(
            county_only_statement, items_added
        )

        return_statement = self.generate_return_statement_and_check_fee(
            county_keys, county_values, city_keys, city_values, middle_statement
        )

        return return_statement

    def generate_return_statement_and_check_fee(
        self, county_keys, county_values, city_keys, city_values, middle_statement
    ):
        """
        generate_return_statement_AND_check_fee generates second half of post price statement

        Args:
            county_keys (list): county key list
            county_values (list): county values list
            city_keys (list): city keys list
            city_values (list): city values list
            middle_statement (str): string containing 1st part of middle statement

        Returns:
            str: final statement to be returned
        """
        if not self.contains_fees:  # no fees
            return_statement = f"x {middle_statement}"

        else:
            fees = self.generate_all_fees(
                county_keys, county_values, city_keys, city_values
            )
            self.generate_total_tax_burden_after_fee(fees)
            return_statement = f"x {middle_statement}{self.generate_all_fee_strings(county_keys, county_values, city_keys, city_values)} = {self.generate_total_tax_burden_str()}"
        return return_statement

    def generate_middle_statement(self, county_only_statement, items_added):
        """
        generate_middle_statement first half of post price statement

        Args:
            county_only_statement (str): statement from county only
            items_added (str): number of items added to county_only_statement

        Returns:
            str: string containing first half of post price statement
        """
        if self.with_county_no_city:
            if items_added == 1:
                middle_statement = (
                    f"{county_only_statement} = {self.generate_total_tax_burden_str()}"
                )
            else:
                middle_statement = f"{self.multiply_rate:.6g} ({county_only_statement}) = {self.generate_total_tax_burden_str()}"

        else:  # has city rates
            # city_ONLY_statement = self.county.city.city_ONLY_statement()

            city_substatement = self.county.city.generate_city_substatements(
                self.statistics["CITY"], self.with_county_no_city, self.city_exists
            )

            middle_statement = f"{self.multiply_rate:.6g} ({county_only_statement}{city_substatement}) = {self.generate_total_tax_burden_str()}"

        return middle_statement

    def generate_total_multiply_rate(self):
        """
        generate_total_multiply_rate
        """
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
        self.city_exists = LogicalWork.check_city_exists(self.statistics["CITY"])

        # add city rates if they exist and set self.with_county_no_city
        if self.city_exists:
            _, city_values = LogicalWork.no_index_dict_to_two_lists(
                self.statistics["CITY"]
            )
            for i in list(filter(None, city_values)):
                i_key = list(i)[0]
                if "Fee" not in i_key:
                    self.multiply_rate += i[i_key]
            self.with_county_no_city = False
        else:
            self.with_county_no_city = True

    def generate_total_tax_burden_str(self):
        """
        generate_total_tax_burden_str

        Returns:
            str: str containg final cost
        """
        return f"${self.final_tax_cost:,.0f}"

    def generate_total_tax_burden_after_rate(self):
        """
        generate_total_tax_burden_after_rate
        """
        self.final_tax_cost = self.price_int * self.multiply_rate

    def generate_total_tax_burden_after_fee(self, fee):
        """
        generate_total_tax_burden_after_fee

        Args:
            fee (float): fee amount to add
        """
        self.final_tax_cost += fee

    def generate_all_fee_strings(
        self, county_keys, county_values, city_keys, city_values
    ):
        """
        generate_ALL_fee_strings

        Args:
            county_keys (list): county key list
            county_values (list): county values list
            city_keys (list): city keys list
            city_values (list): city values list

        Returns:
            str: str containg all fees added
        """
        county_fee_string = self.county.generate_county_fees_string(
            county_keys, county_values
        )
        if self.city_exists:
            city_fee_string = self.county.city.generate_city_fees_string(
                city_keys, city_values
            )
        else:
            city_fee_string = ""

        return county_fee_string + city_fee_string

    def generate_all_fees(self, county_keys, county_values, city_keys, city_values):
        """
        generate_ALL_fees to be added

        Args:
            county_keys (list): county key list
            county_values (list): county values list
            city_keys (list): city keys list
            city_values (list): city values list

        Returns:
            float: all fees to be added
        """
        county_fees = self.county.generate_county_total_fees(county_keys, county_values)
        if self.city_exists:
            city_fees = self.county.city.generate_city_total_fees(
                city_keys, city_values
            )
        else:
            city_fees = 0

        return county_fees + city_fees
