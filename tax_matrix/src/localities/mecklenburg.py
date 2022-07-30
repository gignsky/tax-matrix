"""
    meck co rates document
"""

from . import classes
from . import InputHelper
from . import Printer


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
    POLICE_RATE = None
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = None
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
    POLICE_RATE = None
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = None
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
    FIRE_RATE = None
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
    SPECIAL_STUFF = True
    WASTE_OPTIONS = {
        1: {"Mecklenburg Single Family Solid Waste Fee": 39.50},
        2: {"Charlotte Single Family Solid Waste Fee": 75.02},
    }
    MECK_SERVICES = {
        1: {"Mecklenburg Law Enforcement District For Charlotte ETJ": 0.001781},
        2: {"Mecklenburg Fire District For Charlotte ETJ": 0.0008},
    }

    meck = Mecklenburg(
        COUNTY_NAME,
        COUNTY_WIDE_RATE,
        COUNTY_WIDE_RATE_TITLE,
        CITIES,
        SPECIAL_STUFF,
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
        special_stuff,
        waste_options,
        meck_services,
    ):
        super().__init__(
            county_name, county_wide_rate, county_wide_rate_title, cities, special_stuff
        )
        # initalize dict of all options and services
        self.waste_options = waste_options
        self.meck_services = meck_services
        self.clt_waste_fee = None
        self.meck_waste_fee = None
        self.meck_police_rate = None
        self.meck_fire_rate = None

        # set inital clt waste title
        tmp_clt_waste_key = list(waste_options.keys())[1]
        self.clt_waste_dict = waste_options[tmp_clt_waste_key]
        self.clt_waste_title = list(self.clt_waste_dict.keys())[0]

        # set inital meck waste title
        tmp_meck_waste_key = list(waste_options.keys())[0]
        self.meck_waste_dict = waste_options[tmp_meck_waste_key]
        self.meck_waste_title = list(self.meck_waste_dict.keys())[0]

        # set inital meck police title
        tmp_meck_police_key = list(meck_services.keys())[0]
        self.meck_police_dict = meck_services[tmp_meck_police_key]
        self.meck_police_title = list(self.meck_police_dict.keys())[0]

        # set inital meck fire title
        tmp_meck_fire_key = list(meck_services.keys())[1]
        self.meck_fire_dict = meck_services[tmp_meck_fire_key]
        self.meck_fire_title = list(self.meck_fire_dict.keys())[0]

        # save for inital values
        # set inital clt waste rates
        tmp_inital_clt_waste_fee_dict = waste_options[2]
        self.inital_clt_waste_fee = tmp_inital_clt_waste_fee_dict[self.clt_waste_title]

        # set inital meck waste rates
        tmp_inital_meck_waste_fee_dict = waste_options[1]
        self.inital_meck_waste_fee = tmp_inital_meck_waste_fee_dict[
            self.meck_waste_title
        ]

        # set inital meck police rates
        tmp_inital_meck_police_rate_dict = meck_services[1]
        self.inital_meck_police_rate = tmp_inital_meck_police_rate_dict[
            self.meck_police_title
        ]

        # set inital meck fire rates
        tmp_inital_meck_fire_rate_dict = meck_services[2]
        self.inital_meck_fire_rate = tmp_inital_meck_fire_rate_dict[
            self.meck_fire_title
        ]

    def select_special_options(self):
        """
        select_special_options options for waste and meck services to be added
        """

        INPUT_LOOP = True

        while INPUT_LOOP:
            Printer.liner()
            self.print_special_stuff_options()
            Printer.liner()

            modify = InputHelper.choice_bool(
                "Would you like to modify use any of the above Waste or Mecklenburg Services Fees and Rates?"
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
        which_modify helps to determine if one should modify the values available options on the County services

        SPECIFIC TO MECKLENBURG COUNTY
        """
        MOD_LOOP = True

        mod_dict = {
            0: "Quit",
            1: "Charlotte Waste FEE",
            2: "Mecklenburg Waste FEE",
            3: "Meck Law Enforcement for Charlotte ETJ",
            4: "Meck Fire for Charlotte ETJ",
        }

        print("Note a value of '...Rate: 0' will not appear in final statement")

        while MOD_LOOP:
            which_modify = InputHelper.input_from_dict(
                mod_dict,
                "Please Select Number from below options to modify or Quit: ",
            )

            if which_modify == mod_dict[0]:
                MOD_LOOP = False
            elif which_modify == mod_dict[1]:
                self.modify_clt_waste()
            elif which_modify == mod_dict[2]:
                self.modify_meck_waste()
            elif which_modify == mod_dict[3]:
                self.meck_police_etj()
            elif which_modify == mod_dict[4]:
                self.meck_fire_etj()
            else:
                print("ERROR IN CLASS 'Mecklenburg'")

    def modify_clt_waste(self):
        enable = InputHelper.on_or_off_fee(
            self.clt_waste_title, self.inital_clt_waste_fee, self.clt_waste_fee
        )
        if enable:
            self.clt_waste_fee = self.inital_clt_waste_fee
        else:
            self.clt_waste_fee = None
        Printer.print_green(
            f"{self.clt_waste_title} Rate updated to: {self.clt_waste_fee}"
        )

    def modify_meck_waste(self):
        enable = InputHelper.on_or_off_fee(
            self.meck_waste_title, self.inital_meck_waste_fee, self.meck_waste_fee
        )
        if enable:
            self.meck_waste_fee = self.inital_meck_waste_fee
        else:
            self.meck_waste_fee = None
        Printer.print_green(
            f"{self.meck_waste_title} Rate updated to: {self.meck_waste_fee}"
        )

    def meck_police_etj(self):
        enable = InputHelper.on_or_off_rate(
            self.meck_police_title,
            self.inital_meck_police_rate,
            self.meck_police_rate,
        )
        if enable:
            self.meck_police_rate = self.inital_meck_police_rate
        else:
            self.meck_police_rate = None
        Printer.print_green(
            f"{self.meck_police_title} Rate updated to: {self.meck_police_rate}"
        )

    def meck_fire_etj(self):
        enable = InputHelper.on_or_off_rate(
            self.meck_fire_title, self.inital_meck_fire_rate, self.meck_fire_rate
        )
        if enable:
            self.meck_fire_rate = self.inital_meck_fire_rate
        else:
            self.meck_fire_rate = None
        Printer.print_green(
            f"{self.meck_fire_title} Rate updated to: {self.meck_fire_rate}"
        )

    def print_special_stuff_options(self):
        Printer.short_liner()
        Printer.print_yellow("Modify Waste Fees")
        Printer.print_yellow(
            "Modify Mecklenburg Services (i.e. Meck Fire/Police for Charlotte ETJ"
        )
        Printer.short_liner()

    def print_county_selected_info(self):
        # Print super class info
        super().print_county_selected_info()

        # print Mecklenburg specific info (waste and police/fire)
        Printer.short_liner()
        Printer.print_yellow(f"Charlotte Waste Fee: ${self.clt_waste_fee}")
        Printer.print_yellow(f"Mecklenburg Waste Fee: ${self.meck_waste_fee}")
        Printer.short_liner()
        Printer.print_yellow(
            f"Mecklenburg Police for Charlotte ETJ: {self.meck_police_rate}"
        )
        Printer.print_yellow(
            f"Mecklenburg Fire for Charlotte ETJ: {self.meck_fire_rate}"
        )
        Printer.short_liner()

    def generate_county_statistics(self):
        super().generate_county_statistics()

        if self.clt_waste_fee is not None:
            self.county_statistics[self.clt_waste_title] = self.clt_waste_fee
        else:
            pass
        if self.meck_waste_fee is not None:
            self.county_statistics[self.meck_waste_title] = self.meck_waste_fee
        else:
            pass
        if self.meck_police_rate is not None:
            self.county_statistics[self.meck_police_title] = self.meck_police_rate
        else:
            pass
        if self.meck_fire_rate is not None:
            self.county_statistics[self.meck_fire_title] = self.meck_fire_rate
        else:
            pass

        return self.county_statistics


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
        self.special_district_title = None
        self.special_district_rate = None

    def select_special_district(self):
        in_special_district = InputHelper.choice_bool(
            "Is the subject property within one of the City of Charlotte's five (5) special districts?"
        )
        if in_special_district:
            special_district_selection = InputHelper.input_from_dict(
                self.special_districts,
                "Please Enter Number Associated with the selected with subject's location",
            )
            dict_key = list(special_district_selection.keys())[0]
            dict_inner_dict = special_district_selection[dict_key]

            self.special_district_rate = list(dict_inner_dict.keys())[0]
            self.special_district_title = dict_inner_dict[self.special_district_rate]
        else:
            return None

    def modify_or_keep(self):
        INPUT_LOOP = True

        while INPUT_LOOP:
            Printer.liner()
            self.print_modifiable_info()
            Printer.liner()

            modify = InputHelper.choice_bool(
                "Would you like to modify use any of the above Police, Fire, and/or select a special district?"
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

        SPECIFIC TO CITY OF CHARLOTTE
        """
        MOD_LOOP = True

        mod_dict = {
            0: "Quit",
            1: "Select a Special District",
            2: f"Police Rate: {self.police_rate}",
            3: f"Fire Rate: {self.fire_rate}",
        }

        print("Note a value of '...Rate: 0' will not appear in final statement")

        while MOD_LOOP:
            which_modify = InputHelper.input_from_dict(
                mod_dict, "Please Select Number from below options to modify or Quit: "
            )

            if which_modify == mod_dict[0]:
                MOD_LOOP = False
            elif which_modify == mod_dict[1]:
                self.select_special_district()
            elif which_modify == mod_dict[2]:
                self.modify_police()
            elif which_modify == mod_dict[3]:
                self.modify_fire()
            else:
                print("ERROR IN CLASS 'CityOfCharlotte'")

    def print_modifiable_info(self):
        """
        print_modifiable_info print all info capable of being modified
        """
        print("Select a Special District")
        print(f"Police Rate Title: {self.police_title}")
        print(f"Police Rate: {self.police_rate}")
        print(f"Fire Rate Title: {self.fire_title}")
        print(f"Fire Rate: {self.fire_rate}")

    def print_all_info(self):
        print(f"City Name: {self.city_name}")
        print(f"City Rate: {self.city_wide_rate}")
        print(f"City Rate Title: {self.city_wide_rate_title}")
        print(f"Police Rate: {self.police_rate}")
        print(f"Police Rate Title: {self.police_title}")
        print(f"Fire Rate: {self.fire_rate}")
        print(f"Fire Rate Title: {self.fire_title}")

    def print_city_selected_info(self):
        # Print super class info
        super().print_city_selected_info()

        # print City of Charlotte specific info (special districts)
        Printer.short_liner()
        Printer.print_yellow(f"Special District: {self.special_district_title}")
        Printer.print_yellow(f"Special District Rate: {self.special_district_rate}")
        Printer.short_liner()

    def generate_city_statistics(self):
        super().generate_city_statistics()

        if self.special_district_rate is not None:
            self.city_statistics[
                self.special_district_title
            ] = self.special_district_rate
        else:
            self.city_statistics[self.special_district_title] = None

        return self.city_statistics
