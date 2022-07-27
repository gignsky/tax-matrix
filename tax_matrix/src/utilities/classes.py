"""
    Countains classes for use in program
"""
from . import LogicalWork
from . import InputHelper
from . import Printer


class Property:
    """
    class containing information about the subject property
    """

    def __init__(self):
        self.price_float = None
        self.price_str = None
        self.county = None
        self.statistics = None
        self.statement = None

    def add_price(self, price_float, price_str):
        self.price_float = price_float
        self.price_str = price_str
        print(f"The Price of {price_str} has been loaded to subject!")

    def get_price(self):
        print(f"Price Float: {self.price_float}")
        print(f"Price String: {self.price_str}")
        return self.price_float, self.price_str

    def add_county(self, county):
        self.county = county
        Printer.welcome_county(self.county.get_county_name())

    def get_county(self):
        print(self.county)
        return self.county0

    def add_statistics(self, statistics):
        self.statistics = statistics

    def get_statistics(self):
        print(self.statistics)
        return self.statistics

    def add_statement(self, statement):
        self.statement = statement

    def get_statement(self):
        print(self.statement)
        return self.statement


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


class County:
    """
    generic county class
    """

    def __init__(self, county_name, county_wide_rate, county_wide_rate_title, cities):
        self.county_name = county_name
        self.county_wide_rate = county_wide_rate
        self.county_wide_rate_title = county_wide_rate_title
        self.cities = cities

        print(f"Initalized {county_name} and all cities and towns")

    def get_county_name(self):
        return self.county_name

    def get_county_wide_rate(self):
        print(f"County Rate is: {self.county_wide_rate}")
        return self.county_wide_rate

    def get_cities(self):
        return self.cities

    def select_city(self):
        city = InputHelper.input_from_dict(self.cities)
        return city


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
        print(f"New City and/or Town of {self.city_name} has been loaded into Memory")

    def get_city_name(self):
        return self.city_name

    def get_city_wide_rate(self):
        return self.city_wide_rate

    def get_city_wide_substatement(self):
        return LogicalWork.substatement(self.city_wide_rate, self.cityi)

    def get_police_rate(self):
        return self.police_rate

    def get_police_substatement(self):
        return LogicalWork.substatement(self.police_rate, self.police_title)

    def get_fire_rate(self):
        return self.fire_rate

    def get_fire_substatement(self):
        return LogicalWork.substatement(self.fire_rate, self.fire_title)

    def print_all_info(self):
        print(f"City Name: {self.city_name}")
        print(f"City Rate: {self.city_wide_rate}")
        print(f"City Rate Title: {self.city_wide_rate_title}")
        print(f"Police Rate: {self.police_rate}")
        print(f"Police Rate Title: {self.police_title}")
        print(f"Fire Rate: {self.fire_rate}")
        print(f"Fire Rate Title: {self.fire_title}")
