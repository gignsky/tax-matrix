"""
   union co rates document
"""

# TODO FIX UP THIS DOC, just barely started adding

import debugpy

from . import Printer
from . import InputHelper
from . import LogicalWork
from . import classes
from . import cls


def main():
    # INFORMATION:
    COUNTY_NAME = "Union Co., NC"
    COUNTY_WIDE_RATE_TITLE = "Union County General Government Fund Tax Rate"
    COUNTY_WIDE_RATE = 0.004819
    COUNTY_WIDE_POLICE_TITLE = f"{COUNTY_NAME} Police"
    COUNTY_WIDE_POLICE_RATE = None
    COUNTY_WIDE_FIRE_TITLE = f"{COUNTY_NAME} Fire"
    COUNTY_WIDE_FIRE_RATE = None
    COUNTY_WIDE_EMS_TITLE = f"{COUNTY_NAME} EMS"
    COUNTY_WIDE_EMS_RATE = None
    CITIES = {
        1: village_of_marvin(),
        2: city_of_monroe(),
        3: town_of_wingate(),
        4: town_of_marshville(),
        5: town_of_waxhaw(),
        6: town_of_indian_trail(),
        7: town_of_stallings(),
        8: town_of_weddington(),
        9: village_of_lake_park(),
        10: town_of_fairview(),
        11: town_of_hemby_bridge(),
        12: village_of_wesley_chapel(),
        13: town_of_unionville(),
        14: town_of_mineral_springs(),
        15: town_of_mint_hill(),
    }
    SPECIAL_STUFF = True

    # Special Stuff Ttiles & Rates
    DEBT_BUDGETARY_FUND_TITLE = "Debt Budgetary Fund"
    DEBT_BUDGETARY_FUND_RATE = 0.001025

    # special fire rates
    SPECIAL_FIRE = {
        1: {"Griffith Road": 0.0002},
        2: {"Stack Road": 0.000348},
        3: {"Springs": 0.000464},
        4: {"Fairview": 0.000503},
        5: {"New Salem": 0.000384},
        6: {"Beaver Lane": 0.000671},
        7: {"Bakers": 0.000343},
        8: {"Stallings": 0.000478},
        9: {"Unionville": 0.000614},
        10: {"Wingate": 0.00067},
        11: {"Hemby Bridge": 0.000441},
        12: {"Allens Crossroads": 0.000689},
        13: {"Jackson": 0.000399},
        14: {"Wesley Chapel": 0.000375},
        15: {"Lanes Creek": 0.000546},
        16: {"Waxhaw": 0.000419},
        17: {"Sandy Ridge": 0.000329},
        18: {"Providence": 0.000375},
    }

    union = Union(
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
        DEBT_BUDGETARY_FUND_TITLE,
        DEBT_BUDGETARY_FUND_RATE,
        SPECIAL_FIRE,
    )

    return union


class Union(classes.County):
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
        debt_budgetary_fund_title,
        debt_budgetary_fund_rate,
        special_fire_dict,
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

        self.special_fire_dict = special_fire_dict

        self.set_inital_values(
            debt_budgetary_fund_title,
            debt_budgetary_fund_rate,
        )

    def set_inital_values(
        self,
        debt_budgetary_fund_title,
        debt_budgetary_fund_rate,
    ):
        # debt budgetary fund
        self.debt_budgetary_fund_title = None
        self.debt_budgetary_fund_rate = None

        self.inital_debt_budgetary_fund_title = debt_budgetary_fund_title
        self.inital_debt_budgetary_fund_rate = debt_budgetary_fund_rate

        # special fire
        self.special_fire_title = None
        self.special_fire_rate = None

    def select_special_options(self):
        """
        select_special_options options for all county fire departments and debt budget fund taxes to be added
        """

        INPUT_LOOP = True

        while INPUT_LOOP:

            options_dict = {
                0: "Return to Main Menu",
                1: f"{self.inital_debt_budgetary_fund_title} - Rate: {self.debt_budgetary_fund_rate} | DEFAULT RATE: {self.inital_debt_budgetary_fund_rate}",
                2: "Modify Special Fire Districts for Union Co.",
            }

            modify_option = InputHelper.input_from_dict(
                options_dict, "Do you wish to modify any of the below options?"
            )

            cls()

            if modify_option == options_dict[0]:
                INPUT_LOOP = False
            elif modify_option == options_dict[1]:
                self.mod_budgetary_fund()
            elif modify_option == options_dict[2]:
                self.mod_special_fire()
            else:
                debugpy.breakpoint()
                print("ERROR IN CLASS 'Union'")

    def mod_budgetary_fund(self):

        include = None
        while include is None:
            Printer.short_liner()
            Printer.print_green(self.inital_debt_budgetary_fund_title)
            Printer.short_liner()
            Printer.print_yellow(f"CURRENT RATE: {self.debt_budgetary_fund_rate}")
            Printer.print_yellow(
                f"DEFAULT RATE: {self.inital_debt_budgetary_fund_rate}"
            )
            Printer.short_liner()

            include = InputHelper.choice_bool_with_header(
                f"Is the property subject to the {self.inital_debt_budgetary_fund_title}?"
            )

        cls()

        if include:
            self.debt_budgetary_fund_title = self.inital_debt_budgetary_fund_title
            self.debt_budgetary_fund_rate = self.inital_debt_budgetary_fund_rate
            Printer.short_liner()
            Printer.print_green(
                f"Debt Budgetary Fund Updated...\n& it WILL now be included in statement - Rate: {self.debt_budgetary_fund_rate:.6g}"
            )
            Printer.short_liner()
        else:
            self.debt_budgetary_fund_title = None
            self.debt_budgetary_fund_rate = None
            Printer.short_liner()
            Printer.print_green(
                f"Debt Budgetary Fund Updated...\n& it will NOT be included in statement."
            )
            Printer.short_liner()

    def mod_special_fire(self):

        include = None
        while include is None:
            Printer.print_special_service_dict_with_single_option_and_quit_option(
                self.special_fire_dict, quit_option=False
            )

            include = InputHelper.choice_bool_with_header(
                "Is the property subject to any of the above specific fire departments that are not attached to cities?"
            )

        if include:
            dict_to_mod = None
            while dict_to_mod is None:
                cls()
                Printer.liner()
                if self.special_fire_rate is not None:
                    Printer.print_yellow(
                        f"CURRENT SPECIAL FIRE DISTRICT: {self.special_fire_rate}"
                    )
                else:
                    Printer.print_yellow("No Special Fire Rate Currently Selected")

                dict_to_mod = InputHelper.input_from_dict_with_inner_dict(
                    self.special_fire_dict,
                    "What Special Fire district is the property subject to?",
                )

            title = list(dict_to_mod.keys())[0]
            rate = dict_to_mod[title]

            self.special_fire_title = title
            self.special_fire_rate = rate

            cls()
            Printer.short_liner()
            Printer.print_green(
                f"Special Fire Updated to {self.special_fire_title} - Rate: {self.special_fire_rate:.6g}"
            )
            Printer.short_liner()

        else:
            self.special_fire_title = None
            self.special_fire_rate = None

            cls()

            Printer.short_liner()
            Printer.print_yellow(
                f"Special Fire Updated to NOT be included in statement"
            )
            Printer.short_liner()

    def generate_county_statistics(self):
        super().generate_county_statistics()

        # debt budget fund
        if self.debt_budgetary_fund_rate is not None:
            self.county_statistics[
                self.debt_budgetary_fund_title
            ] = self.debt_budgetary_fund_rate

        # special fire
        if self.special_fire_rate is not None:
            self.county_statistics[self.special_fire_title] = self.special_fire_rate

        return self.county_statistics

    def print_county_selected_info(self):
        super().print_county_selected_info()

        Printer.print_green(f"{self.get_county_name()} Specific Info")

        self.generate_SPECIAL_current_default_strs()

        # print gaston co specific info
        Printer.print_yellow(self.special_fire_department_default_str)
        Printer.print_yellow(self.special_debt_budget_default_str)

    def generate_SPECIAL_current_default_strs(self):
        # special fire districts
        current_fire_department = (
            self.special_fire_rate if self.special_fire_rate is not None else None
        )

        if current_fire_department is not None:
            current_fire_department = f"{current_fire_department:.6g}"
        else:
            current_fire_department = None

        if current_fire_department is not None:
            self.special_fire_department_default_str = f"Special Fire District for Union County: {self.special_fire_title} - Rate: {current_fire_department}"
        else:
            self.special_fire_department_default_str = (
                "No Special Fire District Selected."
            )

        # debt tax
        current_debt_budget = (
            self.debt_budgetary_fund_rate
            if self.debt_budgetary_fund_rate is not None
            else None
        )

        if current_debt_budget is not None:
            current_debt_budget = f"{current_debt_budget}"
        else:
            current_debt_budget = None

        if current_debt_budget is not None:
            self.special_debt_budget_default_str = (
                f"{self.debt_budgetary_fund_title} - Rate: {current_debt_budget}"
            )
        else:
            self.special_debt_budget_default_str = "No Debt Budget Fund Taxes Selected."

    def get_special_options_title(self):
        return "Special Fire Departments & Debt Budget Fund Taxes"


def village_of_marvin():
    # INFORMATION
    CITY_NAME = "Village of Marvin"
    CITY_RATE = 0.0006
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = None
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = None
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    # Specific
    WASTE_TITLE = f"{CITY_NAME} Solid Waste Fee"
    WASTE_FEE = 61.00

    city = CityWithWasteFee(
        CITY_NAME,
        CITY_RATE,
        CITY_RATE_TITLE,
        POLICE_RATE,
        POLICE_RATE_TITLE,
        FIRE_RATE,
        FIRE_RATE_TITLE,
        WASTE_TITLE,
        WASTE_FEE,
    )

    return city


def city_of_monroe():
    # INFORMATION
    CITY_NAME = "City of Monroe"
    CITY_RATE = 0.006163
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = None
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = None
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    # specific
    SPECIAL_DISTRICT_TITLE = "Downtown Special District"
    SPECIAL_DISTRICT_RATE = 0.00219

    city = CityOfMonroe(
        CITY_NAME,
        CITY_RATE,
        CITY_RATE_TITLE,
        POLICE_RATE,
        POLICE_RATE_TITLE,
        FIRE_RATE,
        FIRE_RATE_TITLE,
        SPECIAL_DISTRICT_TITLE,
        SPECIAL_DISTRICT_RATE,
    )

    return city


class CityOfMonroe(classes.City):
    def __init__(
        self,
        city_name,
        city_wide_rate,
        city_wide_rate_title,
        police_rate,
        police_title,
        fire_rate,
        fire_title,
        SPECIAL_DISTRICT_TITLE,
        SPECIAL_DISTRICT_RATE,
    ):
        super().__init__(
            city_name,
            city_wide_rate,
            city_wide_rate_title,
            police_rate,
            police_title,
            fire_rate,
            fire_title,
        )

        self.set_inital_values(SPECIAL_DISTRICT_TITLE, SPECIAL_DISTRICT_RATE)

    def set_inital_values(self, SPECIAL_DISTRICT_TITLE, SPECIAL_DISTRICT_RATE):
        self.special_district_name = None
        self.special_district_rate = None

        # set inital special district values
        self.inital_special_district_name = SPECIAL_DISTRICT_TITLE
        self.inital_special_district_rate = SPECIAL_DISTRICT_RATE

    def which_modify(self):
        """
        which_modify helps to determine if one should modify the values available options on the cities services

        SPECIFIC TO CITY OF Monroe
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
                print("ERROR IN CLASS 'CityOfMonroe'")

    def select_special_district(self):

        cls()

        in_special_district = InputHelper.choice_bool(
            f"Is the property subject to {self.inital_special_district_name} - Rate: {self.inital_special_district_rate} ?"
        )

        if in_special_district:
            self.special_district_name = self.inital_special_district_name
            self.special_district_rate = self.inital_special_district_rate

            cls()

            Printer.short_liner()
            Printer.print_green(
                f"{self.inital_special_district_name} - Rate: {self.inital_special_district_rate} has been added to statement!"
            )
            Printer.short_liner()

        else:
            self.special_district_name = None
            self.special_district_rate = None

            Printer.short_liner()
            Printer.print_red(
                f"{self.inital_special_district_name} - Rate: {self.inital_special_district_rate} will NOT BE included in statement..."
            )
            Printer.short_liner()

    def generate_CITY_current_default_strs(self):
        super().generate_CITY_current_default_strs()
        current_special_district_rate = (
            self.special_district_rate
            if self.special_district_rate is not None
            else None
        )

        current_special_district_name = (
            self.special_district_name
            if self.special_district_name is not None
            else None
        )

        # format if not none
        if current_special_district_rate is not None:
            current_special_district_rate = f"{current_special_district_rate:.6g}"
        else:
            current_special_district_rate = None

        self.special_district_current_default_str = f"{self.inital_special_district_name}: {current_special_district_rate} | STANDARD RATE: {self.inital_special_district_rate}"

    def print_modifiable_info(self):
        """
        print_modifiable_info print all info capable of being modified
        """
        super().generate_CITY_current_default_strs()
        super().print_modifiable_info()

        Printer.print_yellow(
            f"Special District Title: {self.inital_special_district_name}"
        )
        if self.special_district_rate is not None:
            Printer.print_yellow(
                f"Special District Rate: {self.special_district_rate:.6g}"
            )
        else:
            Printer.print_yellow("Special District Rate: None")

    def generate_city_statistics(self):
        super().generate_city_statistics()

        if self.special_district_rate is not None:
            self.city_statistics["SPECIAL_DISTRICT"] = {
                self.special_district_name: self.special_district_rate
            }
        else:
            self.city_statistics["SPECIAL_DISTRICT"] = None

        return self.city_statistics

    # def generate_CITY_substatements(self, city_stats, countywide_only, city_exists):
    #     return super().generate_CITY_substatements(
    #         city_stats, countywide_only, city_exists
    #     )


def town_of_wingate():
    # INFORMATION
    CITY_NAME = "Town of Wingate"
    CITY_RATE = 0.0034
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


def town_of_marshville():
    # INFORMATION
    CITY_NAME = "Town of Marshville"
    CITY_RATE = 0.0049
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


def town_of_waxhaw():
    # INFORMATION
    CITY_NAME = "Tax of Waxhaw"
    CITY_RATE = 0.00385
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


def town_of_indian_trail():
    # INFORMATION
    CITY_NAME = "Town of Indian Trail"
    CITY_RATE = 0.00185
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = None
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = None
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    # Specific
    WASTE_TITLE = f"{CITY_NAME} Solid Waste Fee"
    WASTE_FEE = 61.00

    city = CityWithWasteFee(
        CITY_NAME,
        CITY_RATE,
        CITY_RATE_TITLE,
        POLICE_RATE,
        POLICE_RATE_TITLE,
        FIRE_RATE,
        FIRE_RATE_TITLE,
        WASTE_TITLE,
        WASTE_FEE,
    )

    return city


def town_of_stallings():
    # INFORMATION
    CITY_NAME = "Town of Stallings"
    CITY_RATE = 0.0016
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = None
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = None
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    # Specific
    WASTE_TITLE = f"{CITY_NAME} Solid Waste Fee"
    WASTE_FEE = 61.00

    city = CityWithWasteFee(
        CITY_NAME,
        CITY_RATE,
        CITY_RATE_TITLE,
        POLICE_RATE,
        POLICE_RATE_TITLE,
        FIRE_RATE,
        FIRE_RATE_TITLE,
        WASTE_TITLE,
        WASTE_FEE,
    )

    return city


def town_of_weddington():
    # INFORMATION
    CITY_NAME = "Town of Weddington"
    CITY_RATE = 0.00048
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


def village_of_lake_park():
    # INFORMATION
    CITY_NAME = "Village of Lake Park"
    CITY_RATE = 0.0019
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = None
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = None
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    # Specific
    WASTE_TITLE = f"{CITY_NAME} Solid Waste Fee"
    WASTE_FEE = 61.00

    city = CityWithWasteFee(
        CITY_NAME,
        CITY_RATE,
        CITY_RATE_TITLE,
        POLICE_RATE,
        POLICE_RATE_TITLE,
        FIRE_RATE,
        FIRE_RATE_TITLE,
        WASTE_TITLE,
        WASTE_FEE,
    )

    return city


def town_of_fairview():
    # INFORMATION
    CITY_NAME = "Town of Fairview"
    CITY_RATE = 0.0002
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


def town_of_hemby_bridge():
    # INFORMATION
    CITY_NAME = "Town of Hemby Bridge"
    CITY_RATE = 0
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


def village_of_wesley_chapel():
    # INFORMATION
    CITY_NAME = "Village of Wesley Chapel"
    CITY_RATE = 0.000129
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


def town_of_unionville():
    # INFORMATION
    CITY_NAME = "Town of Unionville"
    CITY_RATE = 0.0002
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


def town_of_mineral_springs():
    # INFORMATION
    CITY_NAME = "Town of Mineral Springs"
    CITY_RATE = 0.00025
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
    CITY_RATE = 0
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


class CityWithWasteFee(classes.City):
    def __init__(
        self,
        city_name,
        city_wide_rate,
        city_wide_rate_title,
        police_rate,
        police_title,
        fire_rate,
        fire_title,
        waste_title,
        waste_fee,
    ):
        super().__init__(
            city_name,
            city_wide_rate,
            city_wide_rate_title,
            police_rate,
            police_title,
            fire_rate,
            fire_title,
        )

        self.set_inital_values(waste_title, waste_fee)

    def set_inital_values(self, waste_title, waste_fee):
        self.waste_title = None
        self.waste_fee = None

        # set inital
        self.inital_waste_title = waste_title
        self.inital_waste_fee = waste_fee

    def which_modify(self):
        """
        which_modify helps to determine if one should modify the values available options on the cities services

        SPECIFIC TO CITY OF Monroe
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
                print("ERROR IN CLASS 'VillageOfMarvin'")

    def select_special_district(self):

        cls()

        in_special_district = InputHelper.choice_bool(
            f"Is the property subject to {self.inital_waste_title}: ${self.inital_waste_fee:.2f} ?"
        )

        if in_special_district:
            self.waste_title = self.inital_waste_title
            self.waste_fee = self.inital_waste_fee

            cls()

            Printer.short_liner()
            Printer.print_green(
                f"{self.inital_waste_title} - Fee: ${self.waste_fee:.2f} has been added to statement!"
            )
            Printer.short_liner()

        else:
            self.waste_title = None
            self.waste_fee = None

            Printer.short_liner()
            Printer.print_red(
                f"{self.inital_waste_title} - Fee: ${self.inital_waste_fee:.2f} will NOT BE included in statement..."
            )
            Printer.short_liner()

    def generate_CITY_current_default_strs(self):
        super().generate_CITY_current_default_strs()
        current_waste_fee = self.waste_fee if self.waste_fee is not None else None

        current_waste_title = self.waste_title if self.waste_title is not None else None

        # format if not none
        if current_waste_fee is not None:
            current_waste_fee = f"${current_waste_fee:.2f}"
        else:
            current_waste_fee = None

        self.special_district_current_default_str = f"{self.inital_waste_title}: {current_waste_fee} | STANDARD FEE: ${self.inital_waste_fee:.2f}"

    def print_modifiable_info(self):
        """
        print_modifiable_info print all info capable of being modified
        """
        self.generate_CITY_current_default_strs()
        super().print_modifiable_info()

        Printer.print_yellow(self.special_district_current_default_str)

    def generate_city_statistics(self):
        super().generate_city_statistics()

        if self.waste_fee is not None:
            self.city_statistics["SPECIAL_DISTRICT"] = {
                self.waste_title: self.waste_fee
            }
        else:
            self.city_statistics["SPECIAL_DISTRICT"] = None

        return self.city_statistics
