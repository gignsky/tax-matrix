"""
    class for cities with waste fee
"""

import debugpy
from . import classes
from . import Printer
from . import cls
from . import InputHelper


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
