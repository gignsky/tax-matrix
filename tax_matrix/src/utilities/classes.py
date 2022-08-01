"""
    Countains classes for use in program
    vscode-fold=2
"""
from . import LogicalWork
from . import InputHelper
from . import Printer
from . import cls


class Property:
    """
    class containing information about the subject property
    """

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
            Printer.print_red("No City has been Selected")
        else:
            self.county.city.print_city_selected_info()

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

        self.CONTAINS_FEES = self.county.check_contains_fees(county_keys, county_values)
        self.generate_total_multiply_rate()
        self.generate_total_tax_burden_after_rate()
        self.COUNTYWIDE_ONLY = LogicalWork.check_countywide_only(
            self.statistics["COUNTY"]
        )

        county_ONLY_statement = self.county.generate_county_ONLY_statement_NO_fee()

        middle_statement = self.generate_middle_statement(county_ONLY_statement)

        return_statement = self.generate_return_statement_AND_check_fee(
            county_keys, county_values, middle_statement
        )

        return return_statement

    def generate_return_statement_AND_check_fee(
        self, county_keys, county_values, middle_statement
    ):
        if not self.CONTAINS_FEES:  # no fees
            return_statement = f"x {middle_statement}"

        else:
            fees = self.county.generate_county_total_fees(county_keys, county_values)
            self.generate_total_tax_burden_after_fee(fees)
            return_statement = f"x {middle_statement}{self.county.generate_county_fees_string(county_keys, county_values)} = {self.generate_total_tax_burden_str()}"
        return return_statement

    def generate_middle_statement(self, county_ONLY_statement):
        if self.WITH_COUNTY_NO_CITY:
            middle_statement = (
                f"{county_ONLY_statement} = {self.generate_total_tax_burden_str()}"
            )
        else:  # has city rates
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


class County:
    """
    generic county class
    """

    def __init__(
        self,
        county_name,
        county_wide_rate,
        county_wide_rate_title,
        all_cities,
        special_stuff,
    ):
        self.county_name = county_name
        self.county_wide_rate = county_wide_rate
        self.county_wide_rate_title = county_wide_rate_title
        self.all_cities = all_cities
        self.city = None
        self.special_stuff = special_stuff

        Printer.inside_liner(f"Initalized {county_name} and all cities and towns")

    def get_county_name(self):
        return self.county_name

    def get_county_wide_rate(self):
        print(f"County Rate is: {self.county_wide_rate}")
        return self.county_wide_rate

    def add_city(self, city):
        self.city = city

    def get_cities(self):
        return self.all_cities

    def select_city(self):
        city = InputHelper.input_from_dict(self.all_cities)
        return city

    def select_special_options(self):
        if self.special_stuff is None:
            Printer.inside_liner(f"NO SPECIAL OPTIONS FOR {self.get_county_name()}")
        else:
            Printer.print_red(
                "If you see this line there is an issue with special options"
            )

    def print_county_selected_info(self):
        Printer.print_green("County...")
        Printer.print_yellow(f"County Name: {self.county_name}")
        Printer.print_yellow(f"Countywide Tax Rate: {self.county_wide_rate}")

    def generate_county_statistics(self):
        # get county stats
        if self.county_wide_rate is not None:
            self.county_statistics = {
                self.county_wide_rate_title: self.county_wide_rate
            }
        else:
            self.county_statistics = None

        return self.county_statistics

    def generate_county_ONLY_statement_NO_fee(self):
        title, rate = LogicalWork.no_index_dict_to_two_lists(self.county_statistics)

        items_added = 0
        for title, rate in zip(title, rate):
            if items_added != 0:
                if "Fee" not in title:
                    return_statement = (
                        return_statement + LogicalWork.substatement_maker(rate, title)
                    )
                    items_added += 1
            else:
                return_statement = f"({rate} - {title})"
                items_added += 1

        return return_statement

    def check_contains_fees(self, county_keys, county_values):
        for key, _ in zip(county_keys, county_values):
            if "Fee" in key:
                return True

        return False

    def generate_county_fees_string(self, county_keys, county_values):
        county_fee_string = ""
        for key, fee in zip(county_keys, county_values):
            if "Fee" in key:
                county_fee_string = county_fee_string + LogicalWork.substatement_maker(
                    f"${fee:,.2f}", key
                )

        return county_fee_string

    def generate_county_total_fees(self, county_keys, county_values):
        total_of_fees = 0
        for key, fee in zip(county_keys, county_values):
            if "Fee" in key:
                total_of_fees += fee

        return total_of_fees

    def generate_county_multiply_rate(self, county_keys, county_values):
        county_multiply_rate = 0.0
        for key, rate in zip(county_keys, county_values):
            if "Fee" not in key:  # only add items that don't have fee
                if rate is not None:  # only add items with None
                    county_multiply_rate += rate

        return county_multiply_rate


class City:
    """
    generic city class
    """

    def __init__(
        self,
        city_name,
        city_wide_rate,
        city_wide_rate_title,
        police_rate,
        police_title,
        fire_rate,
        fire_title,
    ):
        self.city_name = city_name
        self.city_wide_rate = city_wide_rate
        self.city_wide_rate_title = city_wide_rate_title
        self.police_rate = police_rate
        self.police_title = police_title
        self.fire_rate = fire_rate
        self.fire_title = fire_title
        Printer.print_green(
            f"New City and/or Town of {self.city_name} has been loaded into Memory"
        )

        # saves for inital values
        self.inital_police_rate = self.police_rate
        self.inital_fire_rate = self.fire_rate

    def get_city_name(self):
        return self.city_name

    def modify_or_keep(self):
        INPUT_LOOP = True

        while INPUT_LOOP:
            Printer.short_liner()
            self.print_modifiable_info()
            Printer.short_liner()

            modify = InputHelper.choice_bool(
                "Would you like to disable any of the above Police and/or Fire rates?\n **Please note that any item showing a rate of 'None' will\n NOT appear in the final statement and is already disabled**"
            )

            if modify is not None:
                if modify:
                    self.which_modify()
                else:
                    INPUT_LOOP = False

    def get_police_and_fire_strings(self):
        return self.police_current_default_str, self.fire_current_default_str

    def update_police_and_fire_rates_for_string(self, police_rate, fire_rate):
        self.police_rate = police_rate
        self.fire_rate = fire_rate

    def which_modify(self):
        """
        which_modify helps to determine if one should modify the values available options on the cities services
        """
        MOD_LOOP = True

        print("Note a value of 'None' will not appear in final statement")

        while MOD_LOOP:
            self.generate_CITY_current_default_strs()
            mod_dict = {
                0: "Quit",
                1: self.police_current_default_str,
                2: self.fire_current_default_str,
            }
            which_modify = InputHelper.input_from_dict(
                mod_dict, "Please Select Number from below options to modify or Quit: "
            )

            if which_modify == mod_dict[0]:
                MOD_LOOP = False
            elif which_modify == mod_dict[1]:
                self.modify_police()
            elif which_modify == mod_dict[2]:
                self.modify_fire()
            else:
                print("ERROR IN CLASS 'City'")

    def modify_police(self):
        enable = InputHelper.on_or_off_rate(
            "Police", self.inital_police_rate, self.police_rate
        )
        if enable:
            self.police_rate = self.inital_police_rate
        else:
            self.police_rate = None

        cls()
        Printer.print_green(f"Police Rate updated to: {self.police_rate}")

    def modify_fire(self):
        enable = InputHelper.on_or_off_rate(
            "Fire", self.inital_fire_rate, self.fire_rate
        )
        if enable:
            self.fire_rate = self.inital_fire_rate
        else:
            self.fire_rate = None

        cls()
        Printer.print_green(f"Fire Rate updated to: {self.fire_rate}")

    def print_modifiable_info(self):
        """
        print_modifiable_info print all info capable of being modified
        """
        self.generate_CITY_current_default_strs()

        Printer.print_yellow(f"Police Rate Title: {self.police_title}")
        Printer.print_yellow(self.police_current_default_str)
        Printer.print_yellow(f"Fire Rate Title: {self.fire_title}")
        Printer.print_yellow(self.fire_current_default_str)

    def generate_CITY_current_default_strs(self):
        current_police = self.police_rate if self.police_rate is not None else None
        current_fire = self.fire_rate if self.fire_rate is not None else None
        inital_police = (
            self.inital_police_rate if self.inital_police_rate is not None else None
        )
        inital_fire = (
            self.inital_fire_rate if self.inital_fire_rate is not None else None
        )

        # format if not none
        if current_police is not None:
            current_police = f"{current_police:.6g}"
        else:
            current_police = None

        if current_fire is not None:
            current_fire = f"{current_fire:.6g}"
        else:
            current_fire = None

        if inital_police is not None:
            inital_police = f"{inital_police:.6g}"
        else:
            inital_police = None

        if inital_fire is not None:
            inital_fire = f"{inital_fire:.6g}"
        else:
            inital_fire = None

        self.police_current_default_str = (
            f"Police Rate: {current_police} | STANDARD RATE: {self.inital_police_rate}"
        )
        self.fire_current_default_str = (
            f"Fire Rate: {current_fire} | STANDARD RATE: {self.inital_fire_rate}"
        )

    def print_city_selected_info(self):
        Printer.print_green("City...")
        Printer.print_yellow(f"City Name: {self.city_name}")
        Printer.print_yellow(f"Citywide Tax Rate: {self.city_wide_rate}")
        Printer.print_yellow(
            f"City Police Rate: {self.police_rate} | Default: {self.inital_police_rate:.6g}"
        )
        Printer.print_yellow(
            f"City Fire Rate: {self.fire_rate} | Default: {self.inital_fire_rate:.6g}"
        )

    def generate_city_statistics(self):
        self.city_statistics = {}
        if self.city_wide_rate is not None:
            self.city_statistics["CITYWIDE"] = {
                self.city_wide_rate_title: self.city_wide_rate
            }
        else:
            self.city_statistics["CITYWIDE"] = None
        if self.police_rate is not None:
            self.city_statistics["POLICE"] = {self.police_title: self.police_rate}
        else:
            self.city_statistics["POLICE"] = None
        if self.fire_rate is not None:
            self.city_statistics["FIRE"] = {self.fire_title: self.fire_rate}
        else:
            self.city_statistics["FIRE"] = None

        return self.city_statistics

    def generate_CITY_substatements(self, city_stats, with_county_no_city, city_exists):
        _, dicts_values = LogicalWork.no_index_dict_to_two_lists(city_stats)
        city_keys, city_values = LogicalWork.with_index_dict_to_two_lists(dicts_values)
        return_statement = ""

        if not with_county_no_city:
            if city_exists:
                for title, rate in zip(city_keys, city_values):
                    substatement = LogicalWork.substatement_maker(rate, title[0])
                    return_statement = return_statement + substatement
        else:
            Printer.liner()
            Printer.print_red("ERROR IN SUBSTATEMENT GENERATOR")
            Printer.liner()

        return return_statement


# ALL ITEMS CLASSES
class Counties:
    """
    countains list of all counties class refernce variables
    """

    ALL_COUNTIES = []

    @classmethod
    def add_county(cls, county_class):
        cls.ALL_COUNTIES.append(county_class)

    @classmethod
    def get_all_counties(cls):
        return cls.ALL_COUNTIES

    @classmethod
    def reset_counties(cls):
        cls.ALL_COUNTIES = []


class Cities:
    """
    countains list of all counties class refernce variables
    """

    def __init__(self, county):
        self.all_cities = []
        self.county = county

    def add_city(self, city_class):
        self.all_cities.append(city_class)

    def get_all_cities(self):
        return self.all_cities
