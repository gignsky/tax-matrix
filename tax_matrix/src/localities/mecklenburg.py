"""
    meck co rates document
"""

from . import classes
from . import InputHelper


def main():
    # INFORMATION:
    COUNTY_NAME = "Mecklenburg Co., NC"
    COUNTY_WIDE_RATE = 0.003481
    COUNTY_WIDE_RATE_TITLE = "Mecklenburg County Unincorporated Tax Rate"
    CITIES = {
        1: charlotte(),
        2: city_of_charlotte(),
        3: town_of_cornelius(),
        4: town_of_davidson(),
        5: town_of_huntersville(),
        6: town_of_matthews(),
        7: town_of_mint_hill(),
        8: town_of_pineville(),
    }
    WASTE_OPTIONS = {
        1: {"Mecklenburg Single Family Solid Waste Fee": 39.50},
        2: {"Charlotte Single Family Solid Waste Fee": 75.02},
    }
    MECK_SERVICES = None

    meck = Mecklenburg(
        COUNTY_NAME,
        COUNTY_WIDE_RATE,
        COUNTY_WIDE_RATE_TITLE,
        CITIES,
        WASTE_OPTIONS,
        MECK_SERVICES,
    )

    return meck


class Mecklenburg(classes.County):
    def __init__(
        self,
        county_name,
        county_wide_rate,
        county_wide_rate_title,
        cities,
        waste_options,
        meck_services,
    ):
        super().__init__(county_name, county_wide_rate, county_wide_rate_title, cities)
        self.waste_options = waste_options
        self.meck_services = meck_services

    def get_waste_options(self):
        pass

    def get_meck_services(self):
        pass


class CityOfCharlotte(classes.City):
    def __init__(
        self,
        city,
        city_wide_rate,
        city_wide_rate_title,
        police_rate,
        police_title,
        fire_rate,
        fire_title,
        special_districts,
    ):
        super().__init__(
            city,
            city_wide_rate,
            city_wide_rate_title,
            police_rate,
            police_title,
            fire_rate,
            fire_title,
        )
        self.special_districts = special_districts

    def select_special_district(self):
        in_special_district = InputHelper.option_bool(
            "Is the subject property within one of the City of Charlotte's four (4) special districts?"
        )
        if in_special_district:
            self.special_district = InputHelper.input_from_dict(
                self.special_districts,
                "Please Enter Number Associated with the selected with subject's location",
            )
            self.special_district_rate = self.special_districts[self.special_district]
            return self.special_district_rate, self.special_district_rate
        else:
            return None

    def print_all_info(self):
        print(f"City Name: {self.city_name}")
        print(f"City Rate: {self.city_wide_rate}")
        print(f"City Rate Title: {self.city_wide_rate_title}")
        print(f"Police Rate: {self.police_rate}")
        print(f"Police Rate Title: {self.police_title}")
        print(f"Fire Rate: {self.fire_rate}")
        print(f"Fire Rate Title: {self.fire_title}")
        print(f"Special District Rate: {self.special_district_rate}")
        print(f"Special District: {self.special_district}")


def city_of_charlotte():
    # INFORMATION
    CITY_NAME = "City of Charlotte"
    CITY_RATE = 0.003481
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = 0.001781
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = 0.00075
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"
    SPECIAL_DISTRICTS = {
        1: {"District 1": {0.000136: "City of Charlotte District 1"}},
        2: {"District 2": {0.000363: "City of Charlotte District 2"}},
        3: {"District 3": {0.000474: "City of Charlotte District 3"}},
        4: {"District 4": {0.00039: "City of Charlotte District 4"}},
        5: {"District 5": {0.000279: "City of Charlotte District 5"}},
    }

    city = CityOfCharlotte(
        CITY_NAME,
        CITY_RATE,
        CITY_RATE_TITLE,
        POLICE_RATE,
        POLICE_RATE_TITLE,
        FIRE_RATE,
        FIRE_RATE_TITLE,
        SPECIAL_DISTRICTS,
    )

    return city


def charlotte():
    # INFORMATION
    CITY_NAME = "Charlotte"
    CITY_RATE = 0.003481
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = 0
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = 0
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    city = classes.City(
        CITY_NAME,
        CITY_RATE,
        CITY_RATE_TITLE,
        POLICE_RATE,
        POLICE_RATE_TITLE,
        FIRE_RATE,
        FIRE_RATE_TITLE,
    )

    return city


def town_of_cornelius():
    # INFORMATION
    CITY_NAME = "Town of Cornelius"
    CITY_RATE = 0.00222
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = 0.00229
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = 0.000612
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    city = classes.City(
        CITY_NAME,
        CITY_RATE,
        CITY_RATE_TITLE,
        POLICE_RATE,
        POLICE_RATE_TITLE,
        FIRE_RATE,
        FIRE_RATE_TITLE,
    )

    return city


def town_of_davidson():
    # INFORMATION
    CITY_NAME = "Town of Davidson"
    CITY_RATE = 0.0029
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = 0.001432
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = 0.00089
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    city = classes.City(
        CITY_NAME,
        CITY_RATE,
        CITY_RATE_TITLE,
        POLICE_RATE,
        POLICE_RATE_TITLE,
        FIRE_RATE,
        FIRE_RATE_TITLE,
    )

    return city


def town_of_huntersville():
    # INFORMATION
    CITY_NAME = "Town of Huntersville"
    CITY_RATE = 0.0024
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = 0.001584
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = 0.000456
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    city = classes.City(
        CITY_NAME,
        CITY_RATE,
        CITY_RATE_TITLE,
        POLICE_RATE,
        POLICE_RATE_TITLE,
        FIRE_RATE,
        FIRE_RATE_TITLE,
    )

    return city


def town_of_matthews():
    # INFORMATION
    CITY_NAME = "Town of Matthews"
    CITY_RATE = 0.00295
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = 0
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = 0
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    city = classes.City(
        CITY_NAME,
        CITY_RATE,
        CITY_RATE_TITLE,
        POLICE_RATE,
        POLICE_RATE_TITLE,
        FIRE_RATE,
        FIRE_RATE_TITLE,
    )

    return city


def town_of_mint_hill():
    # INFORMATION
    CITY_NAME = "Town of Mint Hill"
    CITY_RATE = 0.00255
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = 0.001558
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = 0.0007
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    city = classes.City(
        CITY_NAME,
        CITY_RATE,
        CITY_RATE_TITLE,
        POLICE_RATE,
        POLICE_RATE_TITLE,
        FIRE_RATE,
        FIRE_RATE_TITLE,
    )

    return city


def town_of_pineville():
    # INFORMATION
    CITY_NAME = "Town of Pineville"
    CITY_RATE = 0.0033
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = 0.001637
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = 0
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    city = classes.City(
        CITY_NAME,
        CITY_RATE,
        CITY_RATE_TITLE,
        POLICE_RATE,
        POLICE_RATE_TITLE,
        FIRE_RATE,
        FIRE_RATE_TITLE,
    )

    return city
