"""
   iredell co rates document
"""
import debugpy

from . import classes
from . import Printer
from . import cls
from . import InputHelper


def main():
    # INFORMATION:
    COUNTY_NAME = "Iredell Co., NC"
    COUNTY_WIDE_RATE_TITLE = "Iredell County Unincorporated Tax Rate"
    COUNTY_WIDE_RATE = 0.005375
    COUNTY_WIDE_POLICE_TITLE = f"{COUNTY_NAME} Police"
    COUNTY_WIDE_POLICE_RATE = None
    COUNTY_WIDE_FIRE_TITLE = f"{COUNTY_NAME} Fire"
    COUNTY_WIDE_FIRE_RATE = 0.0009
    COUNTY_WIDE_EMS_TITLE = f"{COUNTY_NAME} EMS"
    COUNTY_WIDE_EMS_RATE = None
    CITIES = {
        1: statesville_city(),
        2: statesville_downtown(),
        3: woods_municipal_ser(),
        4: troutman(),
        5: harmony(),
        6: mooresville_town(),
        7: mooresville_downtown(),
        8: mooresville_school(),
        9: love_valley(),
        10: davidson_town(),
    }
    SPECIAL_STUFF = True

    # countywide solid waste fee
    special_county_waste_name = "Iredell Co., Solid Waste Fee"
    special_county_waste_fee = 60.00

    # special fire rates - unused with no rates
    SPECIAL_FIRE = {
        1: {"East Alexander Fire": 0},
        2: {"Shepherds Fire": 0},
        3: {"Mount Mourne Fire": 0},
        5: {"B&F Fire": 0},
    }

    iredell = Iredell(
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
        special_county_waste_name,
        special_county_waste_fee,
        SPECIAL_FIRE,
    )

    return iredell


class Iredell(classes.County):
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
        special_county_waste_name,
        special_county_waste_fee,
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
            special_county_waste_name,
            special_county_waste_fee,
        )

    def set_inital_values(
        self,
        special_county_waste_name,
        special_county_waste_fee,
    ):
        # waste fee
        self.special_county_waste_name = None
        self.special_county_waste_fee = None

        self.inital_special_county_waste_name = special_county_waste_name
        self.inital_special_county_waste_fee = special_county_waste_fee

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
                1: f"{self.inital_special_county_waste_name}: ${self.special_county_waste_fee} | DEFAULT FEE: ${self.inital_special_county_waste_fee}",
                2: "Modify Special Fire Districts for Iredell Co.",
            }

            modify_option = InputHelper.input_from_dict(
                options_dict, "Do you wish to modify any of the below options?"
            )

            cls()

            if modify_option == options_dict[0]:
                INPUT_LOOP = False
            elif modify_option == options_dict[1]:
                self.mod_special_waste_fee()
            elif modify_option == options_dict[2]:
                self.mod_special_fire()
            else:
                debugpy.breakpoint()
                print("ERROR IN CLASS 'Union'")

    def mod_special_waste_fee(self):

        include = None
        while include is None:
            Printer.short_liner()
            Printer.print_green(self.inital_special_county_waste_name)
            Printer.short_liner()
            Printer.print_yellow(f"CURRENT RATE: {self.special_county_waste_fee}")
            Printer.print_yellow(
                f"DEFAULT RATE: {self.inital_special_county_waste_fee}"
            )
            Printer.short_liner()

            include = InputHelper.choice_bool_with_header(
                f"Is the property subject to the {self.inital_special_county_waste_name}?"
            )

        cls()

        if include:
            self.inital_special_county_waste_name = (
                self.inital_special_county_waste_name
            )
            self.special_county_waste_fee = self.inital_special_county_waste_fee
            Printer.short_liner()
            Printer.print_green(
                f"County Waste Fee Updated...\n& it WILL now be included in statement - Fee: ${self.special_county_waste_fee:.2f}"
            )
            Printer.short_liner()
        else:
            self.inital_special_county_waste_name = None
            self.special_county_waste_fee = None
            Printer.short_liner()
            Printer.print_green(
                f"County Waste Fee Updated...\n& it will NOT be included in statement."
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

        # county waste fee
        if self.special_county_waste_fee is not None:
            self.county_statistics[
                self.inital_special_county_waste_name
            ] = self.special_county_waste_fee

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

        # county waste fee
        current_waste_fee = (
            self.special_county_waste_fee
            if self.special_county_waste_fee is not None
            else None
        )

        if current_waste_fee is not None:
            current_waste_fee = f"${current_waste_fee:.2f}"
        else:
            current_waste_fee = None

        if current_waste_fee is not None:
            self.special_debt_budget_default_str = (
                f"{self.inital_special_county_waste_name}: {current_waste_fee}"
            )
        else:
            self.special_debt_budget_default_str = "No County Waste Fee Selected."

    def get_special_options_title(self):
        return "Special Fire Departments & Countywide Waste Fee"


def statesville_city():
    # INFORMATION
    CITY_NAME = "Statesville City"
    CITY_RATE = 0.005478
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = None
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = None
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    # Specific
    WASTE_TITLE = f"{CITY_NAME} Solid Waste Fee"
    WASTE_FEE = 60.00

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


def statesville_downtown():
    # INFORMATION
    CITY_NAME = "Statesville Downtown"
    CITY_RATE = 0.001
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


def woods_municipal_ser():
    # INFORMATION
    CITY_NAME = "Woods Municipal Ser."
    CITY_RATE = 0.0021
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


def troutman():
    # INFORMATION
    CITY_NAME = "Troutman"
    CITY_RATE = 0.0052
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


def harmony():
    # INFORMATION
    CITY_NAME = "Harmony"
    CITY_RATE = 0.0014
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


def mooresville_town():
    # INFORMATION
    CITY_NAME = "Mooresville Town"
    CITY_RATE = 0.0058
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = None
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = None
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    # Specific
    WASTE_TITLE = f"{CITY_NAME} Solid Waste Fee"
    WASTE_FEE = 120.00

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


def mooresville_downtown():
    # INFORMATION
    CITY_NAME = "Mooresville Downtown"
    CITY_RATE = 0.0016
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = None
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = None
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    # Specific
    WASTE_TITLE = f"{CITY_NAME} Solid Waste Fee"
    WASTE_FEE = 120.00

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


def mooresville_school():
    # INFORMATION
    CITY_NAME = "Mooresville School"
    CITY_RATE = 0.00185
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = None
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = None
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    # Specific
    WASTE_TITLE = f"{CITY_NAME} Solid Waste Fee"
    WASTE_FEE = 120.00

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


def love_valley():
    # INFORMATION
    CITY_NAME = "Love Valley"
    CITY_RATE = 0.0025
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


def davidson_town():
    # INFORMATION
    CITY_NAME = "Davidson Town"
    CITY_RATE = 0.00325
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
