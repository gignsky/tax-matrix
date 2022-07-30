"""
    Countains classes for use in program
"""
from . import pprint
from . import InputTesters
from . import LogicalWork
from . import InputHelper
from . import Printer


class Property:
    """
    class containing information about the subject property
    """

    def __init__(self):
        self.price_int = None
        self.price_str = None
        self.county = None

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

    def select_special_options(self):
        self.county.select_special_options()

    def print_current_stats(self):
        Printer.liner()
        Printer.print_green("Current statistics to be added to final statement:")
        Printer.short_liner()
        Printer.print_yellow(f"Current Subject Price: {self.price_str}")
        self.county.print_county_selected_info()
        if self.county.city is None:
            Printer.print_red("No City has been Selected")
        else:
            self.county.city.print_city_selected_info()
        Printer.liner()

    def generate_statistics(self):
        self.statistics = {}
        self.statistics["COUNTY"] = self.county.generate_county_statistics()
        if self.county.city is None:
            self.statistics["CITY"] = None
        else:
            self.statistics["CITY"] = self.county.city.generate_city_statistics()

    def generate_multiply_rate(self):
        county_keys, county_values = LogicalWork.county_dict_to_two_lists(
            self.statistics["COUNTY"]
        )
        city_keys, city_values = LogicalWork.county_dict_to_two_lists(
            self.statistics["CITY"]
        )
        self.CITY_EXISTS = LogicalWork.check_city_exists(self.statistics["CITY"])

        self.multiply_rate = 0.0

        if self.COUNTY_ONLY:
            self.multiply_rate = county_values[0]
        else:
            # county adder
            for i in county_values:
                self.multiply_rate = self.multiply_rate + i

        # city adder
        if self.CITY_EXISTS:
            for i in list(filter(None, city_values)):
                i_key = list(i)[0]
                self.multiply_rate = self.multiply_rate + i[i_key]
        else:
            pass

    def generate_post_price_statement(self):
        self.COUNTY_ONLY = LogicalWork.check_county_only(
            self.statistics["COUNTY"], self.statistics["CITY"]
        )

        county_statement = self.county.generate_county_ONLY_statement()
        if self.COUNTY_ONLY:
            return f"x {county_statement}"
        else:
            self.generate_multiply_rate()
            return f"x {self.multiply_rate} ({county_statement}{self.generate_all_substatements()})"

    def generate_all_substatements(self):
        _, dicts_values = LogicalWork.county_dict_to_two_lists(self.statistics["CITY"])
        city_keys, city_values = LogicalWork.city_dict_to_two_lists(dicts_values)
        return_statement = ""

        if not self.COUNTY_ONLY:
            if self.CITY_EXISTS:
                for title, rate in zip(city_keys, city_values):
                    substatement = LogicalWork.substatement_maker(rate, title[0])
                    return_statement = return_statement + substatement
        else:
            Printer.liner()
            Printer.print_red("ERROR IN SUBSTATEMENT GENERATOR")
            Printer.liner()

        return return_statement

    def generate_total_tax_cost(self):

        tax_cost_int = self.price_int * self.multiply_rate

        tax_cost_str = f"${tax_cost_int:,.0f}"
        return tax_cost_str


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
        Printer.short_liner()
        Printer.print_green("County...")
        Printer.print_yellow(f"County Name: {self.county_name}")
        Printer.print_yellow(f"Countywide Tax Rate: {self.county_wide_rate}")
        Printer.short_liner()

    def generate_county_statistics(self):
        # get county stats
        if self.county_wide_rate is not None:
            self.county_statistics = {
                self.county_wide_rate_title: self.county_wide_rate
            }
        else:
            self.county_statistics = None

        return self.county_statistics

    def generate_county_ONLY_statement(self):
        if self.county_wide_rate is not None:
            return f"({self.county_wide_rate} - {self.county_wide_rate_title})"
        else:
            Printer.liner()
            Printer.print_red("THERE HAS BEEN AN ERROR IN COUNTY ONLY TITLE GENERATOR")
            Printer.liner()


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
            Printer.liner()
            self.print_modifiable_info()
            Printer.liner()

            modify = InputHelper.choice_bool(
                "Would you like to disable any of the above Police and/or Fire rates?\n **Please note that any item showing a rate of 'None' will\n NOT appear in the final statement and is already disabled**"
            )

            if modify is not None:
                if modify:
                    self.which_modify()
                else:
                    INPUT_LOOP = False
            else:
                pass

    def which_modify(self):
        """
        which_modify helps to determine if one should modify the values available options on the cities services
        """
        MOD_LOOP = True

        mod_dict = {
            0: "Quit",
            1: f"Police Rate: {self.police_rate}",
            2: f"Fire Rate: {self.fire_rate}",
        }

        print("Note a value of '...Rate: 0' will not appear in final statement")

        while MOD_LOOP:
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
        Printer.print_green(f"Police Rate updated to: {self.police_rate}")

    def modify_fire(self):
        enable = InputHelper.on_or_off_rate(
            "Fire", self.inital_fire_rate, self.fire_rate
        )
        if enable:
            self.fire_rate = self.inital_fire_rate
        else:
            self.fire_rate = None
        Printer.print_green(f"Fire Rate updated to: {self.fire_rate}")

    def print_modifiable_info(self):
        """
        print_modifiable_info print all info capable of being modified
        """
        print(f"Police Rate Title: {self.police_title}")
        print(f"Police Rate: {self.police_rate}")
        print(f"Fire Rate Title: {self.fire_title}")
        print(f"Fire Rate: {self.fire_rate}")

    def print_city_selected_info(self):
        Printer.print_green("City...")
        Printer.print_yellow(f"City Name: {self.city_name}")
        Printer.print_yellow(f"Citywide Tax Rate: {self.city_wide_rate}")
        Printer.short_liner()
        Printer.print_yellow(f"City Police Rate: {self.police_rate}")
        Printer.print_yellow(f"City Fire Rate: {self.fire_rate}")
        Printer.short_liner()

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
