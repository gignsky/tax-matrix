"""
    meck co rates document
"""

import debugpy
from . import LogicalWork
from . import classes
from . import InputHelper
from . import Printer
from . import cls


def main():
    # INFORMATION:
    COUNTY_NAME = "Mecklenburg Co., NC"
    COUNTY_WIDE_RATE_TITLE = "Mecklenburg County Unincorporated Tax Rate"
    COUNTY_WIDE_RATE = 0.006169
    COUNTY_WIDE_POLICE_TITLE = f"{COUNTY_NAME} Police"
    COUNTY_WIDE_POLICE_RATE = None
    COUNTY_WIDE_FIRE_TITLE = f"{COUNTY_NAME} Fire"
    COUNTY_WIDE_FIRE_RATE = None
    COUNTY_WIDE_EMS_TITLE = f"{COUNTY_NAME} EMS"
    COUNTY_WIDE_EMS_RATE = None
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
        COUNTY_WIDE_RATE_TITLE,
        COUNTY_WIDE_RATE,
        COUNTY_WIDE_POLICE_TITLE,
        COUNTY_WIDE_POLICE_RATE,
        COUNTY_WIDE_FIRE_TITLE,
        COUNTY_WIDE_FIRE_RATE,
        COUNTY_WIDE_EMS_TITLE,
        COUNTY_WIDE_EMS_RATE,
        CITIES,
        SPECIAL_STUFF,
        WASTE_OPTIONS,
        MECK_SERVICES,
    )

    return meck


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


class Mecklenburg(classes.County):
    def __init__(
        self,
        county_name,
        county_wide_rate_title,
        county_wide_rate,
        county_wide_police_title,
        county_wide_police_rate,
        county_wide_fire_title,
        county_wide_fire_rate,
        county_wide_ems_title,
        county_wide_ems_rate,
        all_cities,
        special_stuff,
        waste_options,
        meck_services,
    ):
        super().__init__(
            county_name,
            county_wide_rate_title,
            county_wide_rate,
            county_wide_police_title,
            county_wide_police_rate,
            county_wide_fire_title,
            county_wide_fire_rate,
            county_wide_ems_title,
            county_wide_ems_rate,
            all_cities,
            special_stuff,
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
            self.print_special_stuff_options()

            modify = InputHelper.choice_bool(
                "Would you like to modify use any of the above Waste or Mecklenburg Services Fees and Rates?"
            )

            cls()

            if modify is not None:
                if modify:
                    self.which_modify_special_services()
                else:
                    INPUT_LOOP = False
            else:
                pass

    def which_modify_special_services(self):
        """
        which_modify helps to determine if one should modify the values available options on the County services

        SPECIFIC TO MECKLENBURG COUNTY
        """
        MOD_LOOP = True

        print("Note a value of 'None' will not appear in final statement")

        while MOD_LOOP:
            self.generate_SPECIAL_current_default_strs()
            mod_dict = {
                0: f"Quit",
                1: self.clt_waste_current_default_str,
                2: self.meck_waste_current_default_str,
                3: self.meck_police_current_default_str,
                4: self.meck_fire_current_default_str,
            }
            which_modify = InputHelper.input_from_dict(
                mod_dict,
                "Please Select Number from below options to modify or Quit: ",
            )

            cls()

            # quit
            if which_modify == mod_dict[0]:
                MOD_LOOP = False
            # clt waste
            elif which_modify == mod_dict[1]:
                self.modify_clt_waste()
            # meck waste
            elif which_modify == mod_dict[2]:
                self.modify_meck_waste()
            # meck police
            elif which_modify == mod_dict[3]:
                self.meck_police_etj()
            # meck fire
            elif which_modify == mod_dict[4]:
                self.meck_fire_etj()
            else:
                debugpy.breakpoint()
                print("ERROR IN CLASS 'Mecklenburg'")

    def modify_clt_waste(self):
        enable = InputHelper.on_or_off_fee(
            self.clt_waste_title, self.inital_clt_waste_fee, self.clt_waste_fee
        )

        cls()

        if enable:
            self.clt_waste_fee = self.inital_clt_waste_fee
        else:
            self.clt_waste_fee = None
        Printer.liner()
        Printer.print_green(
            f"{self.clt_waste_title} Rate updated to: {self.clt_waste_fee:.2f}"
        )

    def modify_meck_waste(self):
        enable = InputHelper.on_or_off_fee(
            self.meck_waste_title, self.inital_meck_waste_fee, self.meck_waste_fee
        )

        cls()

        if enable:
            self.meck_waste_fee = self.inital_meck_waste_fee
        else:
            self.meck_waste_fee = None
        Printer.liner()
        Printer.print_green(
            f"{self.meck_waste_title} Rate updated to: {self.meck_waste_fee:.2f}"
        )

    def meck_police_etj(self):
        enable = InputHelper.on_or_off_rate(
            self.meck_police_title,
            self.inital_meck_police_rate,
            self.meck_police_rate,
        )

        cls()

        if enable:
            self.meck_police_rate = self.inital_meck_police_rate
        else:
            self.meck_police_rate = None
        Printer.liner()
        Printer.print_green(
            f"{self.meck_police_title} Rate updated to: {self.meck_police_rate}"
        )

    def meck_fire_etj(self):
        enable = InputHelper.on_or_off_rate(
            self.meck_fire_title, self.inital_meck_fire_rate, self.meck_fire_rate
        )

        cls()

        if enable:
            self.meck_fire_rate = self.inital_meck_fire_rate
        else:
            self.meck_fire_rate = None
        Printer.liner()
        Printer.print_green(
            f"{self.meck_fire_title} Rate updated to: {self.meck_fire_rate}"
        )

    def print_special_stuff_options(self):
        self.generate_SPECIAL_current_default_strs()

        Printer.short_liner()
        Printer.print_yellow(self.clt_waste_current_default_str)
        Printer.print_yellow(self.meck_waste_current_default_str)
        Printer.print_yellow(self.meck_police_current_default_str)
        Printer.print_yellow(self.meck_fire_current_default_str)
        Printer.short_liner()

    def print_county_selected_info(self):
        # Print super class info
        super().print_county_selected_info()

        Printer.print_green(f"{self.get_county_name()} Specific Info...")
        self.generate_SPECIAL_current_default_strs()

        # print Mecklenburg specific info (waste and police/fire)
        Printer.print_yellow(self.clt_waste_current_default_str)
        Printer.print_yellow(self.meck_waste_current_default_str)
        Printer.print_yellow(self.meck_police_current_default_str)
        Printer.print_yellow(self.meck_fire_current_default_str)

    def generate_SPECIAL_current_default_strs(self):
        current_clt_waste = (
            self.clt_waste_fee if self.clt_waste_fee is not None else None
        )
        current_meck_waste = (
            self.meck_waste_fee if self.meck_waste_fee is not None else None
        )
        current_meck_police = (
            self.meck_police_rate if self.meck_police_rate is not None else None
        )
        current_meck_fire = (
            self.meck_fire_rate if self.meck_fire_rate is not None else None
        )

        # format if not none
        if current_clt_waste is not None:
            current_clt_waste = f"${current_clt_waste:.2f}"
        else:
            current_clt_waste = None
        if current_meck_waste is not None:
            current_meck_waste = f"${current_meck_waste:.2f}"
        else:
            current_meck_waste = None
        if current_meck_police is not None:
            current_meck_police = f"{current_meck_police:.6g}"
        else:
            current_meck_police = None
        if current_meck_fire is not None:
            current_meck_fire = f"{current_meck_fire:.6g}"
        else:
            current_meck_fire = None

        self.clt_waste_current_default_str = f"Charlotte Waste Fee: {current_clt_waste} | STANDARD FEE: ${self.inital_clt_waste_fee:.2f}"
        self.meck_waste_current_default_str = f"Mecklenburg Waste Fee: {current_meck_waste} | STANDARD FEE: ${self.inital_meck_waste_fee:.2f}"
        self.meck_police_current_default_str = f"Mecklenburg Police for Charlotte ETJ: {current_meck_police} | STANDARD RATE: {self.inital_meck_police_rate:.6g}"
        self.meck_fire_current_default_str = f"Mecklenburg Fire for Charlotte ETJ: {current_meck_fire} | STANDARD RATE: {self.inital_meck_fire_rate:.6g}"

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

        cls()

        in_special_district = InputHelper.choice_bool(
            "Is the subject property within one of the City of Charlotte's five (5) special districts?"
        )

        if in_special_district:
            special_district_selection = InputHelper.input_from_dict(
                self.special_districts,
                "Please Enter Number Associated with the selected with subject's location",
            )

            cls()

            dict_key = list(special_district_selection.keys())[0]
            dict_inner_dict = special_district_selection[dict_key]

            self.special_district_rate = list(dict_inner_dict.keys())[0]
            self.special_district_title = dict_inner_dict[self.special_district_rate]
        else:
            self.special_district_rate = None
            self.special_district_title = None

    def modify_or_keep(self):
        INPUT_LOOP = True

        while INPUT_LOOP:
            Printer.short_liner()
            self.print_modifiable_info()
            Printer.short_liner()

            modify = InputHelper.choice_bool(
                "Would you like to modify (or select) use any of the above Police, Fire, Special Districts?"
            )

            cls()

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

        print("Note a value of 'None' will not appear in final statement")

        INITAL_RUN = True
        while MOD_LOOP:
            if INITAL_RUN:  # run on first time
                INITAL_RUN = False
            else:
                super().update_police_and_fire_rates_for_string(
                    self.police_rate, self.fire_rate
                )

            self.generate_CITY_current_default_strs()
            (
                police_current_default_str,
                fire_current_default_str,
            ) = super().get_police_and_fire_strings()

            mod_dict = {
                0: "Quit",
                1: police_current_default_str,
                2: fire_current_default_str,
                3: self.special_district_current_default_str,
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
            elif which_modify == mod_dict[3]:
                self.select_special_district()
            else:
                debugpy.breakpoint()
                print("ERROR IN CLASS 'CityOfCharlotte'")

    def print_modifiable_info(self):
        """
        print_modifiable_info print all info capable of being modified
        """
        super().generate_CITY_current_default_strs()
        super().print_modifiable_info()
        self.generate_CITY_current_default_strs()

        Printer.print_yellow(f"Special District Title: {self.special_district_title}")
        Printer.print_yellow(self.special_district_current_default_str)

    def generate_CITY_current_default_strs(self):
        super().generate_CITY_current_default_strs()
        current_special_district = (
            self.special_district_rate
            if self.special_district_rate is not None
            else None
        )
        current_special_district_title = (
            self.special_district_title
            if self.special_district_title is not None
            else None
        )

        inital_special_district = self.inital_special_district_rate = None
        inital_special_district_title = None

        # format if not none
        if current_special_district is not None:
            current_special_district = f"{current_special_district:.6g}"
        else:
            current_special_district = None

        title = (
            self.special_district_title
            if self.special_district_title is not None
            else "Special District"
        )

        self.special_district_current_default_str = f"{title}: {current_special_district} | STANDARD RATE: {self.inital_special_district_rate}"

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

        Printer.print_green(f"{self.get_city_name()} Specific Info...")
        # print City of Charlotte specific info (special districts)
        Printer.print_yellow(
            f"Special District: {self.special_district_title} | Default: {None}"
        )
        Printer.print_yellow(
            f"Special District Rate: {self.special_district_rate} | Default: {None}"
        )

    def generate_city_statistics(self):
        super().generate_city_statistics()

        if self.special_district_rate is not None:
            self.city_statistics["SPECIAL_DISTRICT"] = {
                self.special_district_title: self.special_district_rate
            }
        else:
            self.city_statistics["SPECIAL_DISTRICT"] = None

        return self.city_statistics

    def generate_CITY_substatements(self, city_stats, countywide_only, city_exists):
        return super().generate_CITY_substatements(
            city_stats, countywide_only, city_exists
        )
