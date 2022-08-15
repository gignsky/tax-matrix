"""
   iredell co rates document
"""
import debugpy

from . import classes
from . import Printer
from . import cls
from . import InputHelper


def main():
    """
    main general function for iredell county

    Returns:
        obj: county class
    """
    # INFORMATION:
    county_name = "Iredell Co., NC"
    county_wide_rate_title = "Iredell County Unincorporated Tax Rate"
    county_wide_rate = 0.005375
    county_wide_police_title = f"{county_name} Police"
    county_wide_police_rate = None
    county_wide_fire_title = f"{county_name} Fire"
    county_wide_fire_rate = 0.0009
    county_wide_ems_title = f"{county_name} EMS"
    county_wide_ems_rate = None
    cities = {
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
    special_stuff = True

    # countywide solid waste fee
    special_county_waste_name = "Iredell Co., Solid Waste Fee"
    special_county_waste_fee = 60.00

    # special fire rates - unused with no rates
    special_fire = {
        1: {"East Alexander Fire": 0},
        2: {"Shepherds Fire": 0},
        3: {"Mount Mourne Fire": 0},
        5: {"B&F Fire": 0},
    }

    iredell = Iredell(
        county_name,
        county_wide_rate_title,
        county_wide_rate,
        county_wide_police_title,
        county_wide_police_rate,
        county_wide_fire_title,
        county_wide_fire_rate,
        county_wide_ems_title,
        county_wide_ems_rate,
        cities,
        special_stuff,
        special_county_waste_name,
        special_county_waste_fee,
        special_fire,
    )

    return iredell


class Iredell(classes.County):
    """
    Iredell general class

    Args:
        classes (class): generic county class
    """
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

        self.inital_special_county_waste_name=None
        self.special_county_waste_fee=None
        self.special_fire_title=None
        self.special_fire_rate=None
        self.special_fire_department_default_str=None
        self.special_debt_budget_default_str=None

    def set_inital_values(
        self,
        special_county_waste_name,
        special_county_waste_fee,
    ):
        """
        set_inital_values sets inital waste and special values

        Args:
            special_county_waste_name (str): title
            special_county_waste_fee (float): fee amount
        """
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

        input_loop = True

        while input_loop:

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
                input_loop = False
            elif modify_option == options_dict[1]:
                self.mod_special_waste_fee()
            elif modify_option == options_dict[2]:
                self.mod_special_fire()
            else:
                debugpy.breakpoint()
                print("ERROR IN CLASS 'Union'")

    def mod_special_waste_fee(self):
        """
        mod_special_waste_fee function
        """
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
                "County Waste Fee Updated...\n& it will NOT be included in statement."
            )
            Printer.short_liner()

    def mod_special_fire(self):
        """
        mod_special_fire function
        """
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
                "Special Fire Updated to NOT be included in statement"
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

        self.generate_special_current_default_strs()

        # print gaston co specific info
        Printer.print_yellow(self.special_fire_department_default_str)
        Printer.print_yellow(self.special_debt_budget_default_str)

    def generate_special_current_default_strs(self):
        """
        generate_SPECIAL_current_default_strs
        """
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
    city_name = "Statesville City"
    city_rate = 0.005478
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    # Specific
    waste_title = f"{city_name} Solid Waste Fee"
    waste_fee = 60.00

    city = CityWithWasteFee(
        city_name,
        city_rate,
        city_rate_title,
        police_rate,
        police_rate_title,
        fire_rate,
        fire_rate_title,
        waste_title,
        waste_fee,
    )

    return city


def statesville_downtown():
    # INFORMATION
    city_name = "Statesville Downtown"
    city_rate = 0.001
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    city = classes.City(
        city_name,
        city_rate,
        city_rate_title,
        police_rate,
        police_rate_title,
        fire_rate,
        fire_rate_title,
    )

    return city


def woods_municipal_ser():
    # INFORMATION
    city_name = "Woods Municipal Ser."
    city_rate = 0.0021
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    city = classes.City(
        city_name,
        city_rate,
        city_rate_title,
        police_rate,
        police_rate_title,
        fire_rate,
        fire_rate_title,
    )

    return city


def troutman():
    # INFORMATION
    city_name = "Troutman"
    city_rate = 0.0052
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    city = classes.City(
        city_name,
        city_rate,
        city_rate_title,
        police_rate,
        police_rate_title,
        fire_rate,
        fire_rate_title,
    )

    return city


def harmony():
    # INFORMATION
    city_name = "Harmony"
    city_rate = 0.0014
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    city = classes.City(
        city_name,
        city_rate,
        city_rate_title,
        police_rate,
        police_rate_title,
        fire_rate,
        fire_rate_title,
    )

    return city


def mooresville_town():
    # INFORMATION
    city_name = "Mooresville Town"
    city_rate = 0.0058
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    # Specific
    waste_title = f"{city_name} Solid Waste Fee"
    waste_fee = 120.00

    city = CityWithWasteFee(
        city_name,
        city_rate,
        city_rate_title,
        police_rate,
        police_rate_title,
        fire_rate,
        fire_rate_title,
        waste_title,
        waste_fee,
    )

    return city


def mooresville_downtown():
    # INFORMATION
    city_name = "Mooresville Downtown"
    city_rate = 0.0016
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    # Specific
    waste_title = f"{city_name} Solid Waste Fee"
    waste_fee = 120.00

    city = CityWithWasteFee(
        city_name,
        city_rate,
        city_rate_title,
        police_rate,
        police_rate_title,
        fire_rate,
        fire_rate_title,
        waste_title,
        waste_fee,
    )

    return city


def mooresville_school():
    # INFORMATION
    city_name = "Mooresville School"
    city_rate = 0.00185
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    # Specific
    waste_title = f"{city_name} Solid Waste Fee"
    waste_fee = 120.00

    city = CityWithWasteFee(
        city_name,
        city_rate,
        city_rate_title,
        police_rate,
        police_rate_title,
        fire_rate,
        fire_rate_title,
        waste_title,
        waste_fee,
    )

    return city


def love_valley():
    # INFORMATION
    city_name = "Love Valley"
    city_rate = 0.0025
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    city = classes.City(
        city_name,
        city_rate,
        city_rate_title,
        police_rate,
        police_rate_title,
        fire_rate,
        fire_rate_title,
    )

    return city


def davidson_town():
    # INFORMATION
    city_name = "Davidson Town"
    city_rate = 0.00325
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    city = classes.City(
        city_name,
        city_rate,
        city_rate_title,
        police_rate,
        police_rate_title,
        fire_rate,
        fire_rate_title,
    )

    return city


class CityWithWasteFee(classes.City):
    """
    CityWithWasteFee class for cities with waste fees

    Args:
        classes (class): generic city class
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

        self.current_waste_title=None
        self.waste_title = None
        self.waste_fee = None
        self.special_district_current_default_str=None

        self.set_inital_values(waste_title, waste_fee)

    def set_inital_values(self, waste_title, waste_fee):
        """
        set_inital_values set inital values
        """
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
        mod_loop = True

        print("Note a value of 'None' will not appear in final statement")

        inital_run = True
        while mod_loop:
            if inital_run:  # run on first time
                inital_run = False
            else:
                super().update_police_and_fire_rates_for_string(
                    self.police_rate, self.fire_rate
                )

            self.generate_city_current_default_strs()

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
                mod_loop = False
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
        """
        select_special_district
        """
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

    def generate_city_current_default_strs(self):
        super().generate_city_current_default_strs()
        current_waste_fee = self.waste_fee if self.waste_fee is not None else None

        #TODO might be depreciated
        # current_waste_title = self.waste_title if self.waste_title is not None else None

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
        self.generate_city_current_default_strs()
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
