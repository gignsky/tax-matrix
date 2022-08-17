"""
    gaston county specific class
"""

from . import cls
from . import InputHelper
from . import InputTesters
from . import Printer
from . import general_classes

class Gaston(general_classes.County):
    """
    Gaston county specific class

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
        county_fire_services,
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

        # initalize dict of all county fire rates
        self.county_fire_services = county_fire_services
        self.participating_fire_department_title = None
        self.participating_fire_department_rate = None
        self.special_fire_department_default_str=None

    def select_special_options(self):
        """
        select_special_options options for all county fire departments to be added
        """

        input_loop = True

        while input_loop:

            include = None
            while include is None:
                Printer.print_special_service_dict_with_single_option_and_quit_option(
                    self.county_fire_services, quit_option=False
                )

                include = InputHelper.choice_bool_with_header(
                    "Is the property subject to any of the above specific fire departments that are not attached to cities?"
                )

            cls()

            self.select_fire_department(include)
            Printer.short_liner()
            if self.participating_fire_department_rate is not None:
                Printer.print_green(
                    f"Added '{self.participating_fire_department_title} - {self.participating_fire_department_rate}' to statement"
                )
            else:
                Printer.print_yellow("NO general county Fire Department in statement")
            Printer.short_liner()
            input_loop = False

    def select_fire_department(self, include):
        """
        which_modify helps to determine if one should modify the values available options on the County services

        SPECIFIC TO GASTON COUNTY
        """

        mod_loop = True

        while mod_loop:
            if include:
                Printer.print_special_service_dict_with_single_option_and_quit_option(
                    self.county_fire_services, quit_option=True
                )

                option = input(
                    "Please ENTER number associated with Fire Department the property is subject to: "
                )

            else:
                self.participating_fire_department_rate = None
                self.participating_fire_department_title = None
                break

            cls()

            option_int = InputTesters.verify_int(option)

            if option_int is 0:
                break
            else:
                selected_fire_dept_dict = InputTesters.verify_dict_selection(
                    option_int, self.county_fire_services
                )

                if selected_fire_dept_dict is not None:
                    # quit if zero otherwise continue
                    if option_int != 0:
                        title = list(selected_fire_dept_dict.keys())[0]
                        rate = selected_fire_dept_dict[title]

                        if self.participating_fire_department_rate is not None:
                            self.participating_fire_department_rate = None
                            self.participating_fire_department_title = None

                        self.participating_fire_department_rate = rate
                        self.participating_fire_department_title = title

                    mod_loop = False

    def generate_county_statistics(self):
        super().generate_county_statistics()

        if self.participating_fire_department_rate is not None:
            self.county_statistics[
                self.participating_fire_department_title
            ] = self.participating_fire_department_rate
        else:
            pass

        return self.county_statistics

    def print_county_selected_info(self):
        super().print_county_selected_info()

        Printer.print_green(f"{self.get_county_name()} Specific Info")

        self.generate_special_current_default_strs()

        # print gaston co specific info
        Printer.print_yellow(self.special_fire_department_default_str)

    def generate_special_current_default_strs(self):
        """
        generate_SPECIAL_current_default_strs
        """
        current_fire_department = (
            self.participating_fire_department_rate
            if self.participating_fire_department_rate is not None
            else None
        )

        if current_fire_department is not None:
            current_fire_department = f"{current_fire_department:.6g}"
        else:
            current_fire_department = None

        if current_fire_department is not None:
            self.special_fire_department_default_str = f"Special Fire District for Gaston County: {self.participating_fire_department_title} - Rate: {current_fire_department}"
        else:
            self.special_fire_department_default_str = (
                "No Special Fire District Selected."
            )

    def get_special_options_title(self):
        return "Special Fire Departments"
