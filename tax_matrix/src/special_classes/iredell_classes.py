"""
    iredell co specific class
"""

import debugpy
from . import classes
from . import Printer
from . import cls
from . import InputHelper

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
