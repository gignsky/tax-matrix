"""
    generic union county class
"""

from . import debugpy
from . import cls
from . import Printer
from . import InputHelper
from . import general_classes


class CityOfMonroe(general_classes.City):
    """
    CityOfMonroe class specific for city of monroe

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
        special_district_title,
        special_district_rate,
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

        self.set_inital_values(special_district_title, special_district_rate)

        self.special_district_name = None
        self.special_district_rate = None
        self.special_district_current_default_str = None

    def set_inital_values(self, special_district_title, special_district_rate):
        """
        set_inital_values set inital values for special district

        Args:
            special_district_title (str): title
            special_district_rate (float): rate
        """
        self.special_district_name = None
        self.special_district_rate = None

        # set inital special district values
        self.inital_special_district_name = special_district_title
        self.inital_special_district_rate = special_district_rate

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
                print("ERROR IN CLASS 'CityOfMonroe'")

    def select_special_district(self):
        """
        select_special_district
        """

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

    def generate_city_current_default_strs(self):
        """
        generate_city_current_default_strs
        """
        super().generate_city_current_default_strs()
        current_special_district_rate = (
            self.special_district_rate
            if self.special_district_rate is not None
            else None
        )

        # TODO Might be depreciated
        # current_special_district_name = (self.special_district_name
        #                                  if self.special_district_name
        #                                  is not None else None)

        # format if not none
        if current_special_district_rate is not None:
            current_special_district_rate = f"{current_special_district_rate:.4g}"
        else:
            current_special_district_rate = None

        self.special_district_current_default_str = f"{self.inital_special_district_name}: {current_special_district_rate} | STANDARD RATE: {self.inital_special_district_rate}"

    def print_modifiable_info(self):
        """
        print_modifiable_info print all info capable of being modified
        """
        super().generate_city_current_default_strs()
        super().print_modifiable_info()

        Printer.print_yellow(
            f"Special District Title: {self.inital_special_district_name}"
        )
        if self.special_district_rate is not None:
            Printer.print_yellow(
                f"Special District Rate: {self.special_district_rate:.4g}"
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
