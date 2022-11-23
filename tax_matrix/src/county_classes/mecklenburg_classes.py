"""
    classes specific to mecklenburg county
"""

from . import cls
from . import debugpy

from . import InputHelper
from . import Printer

from . import general_classes


class CityOfCharlotte(general_classes.City):
    """
    CityOfCharlotte city of charlotte specific classes

    Args:
        classes (obj): generic county class
    """

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

        # initalize to fix errors
        self.special_district_current_default_str = None

    def select_special_district(self):
        """
        select_special_district select if using special district
        """

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
        input_loop = True

        while input_loop:
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
                    input_loop = False
            else:
                pass

    def which_modify(self):
        """
        which_modify helps to determine if one should modify the values available options on the cities services

        SPECIFIC TO CITY OF CHARLOTTE
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
                print("ERROR IN CLASS 'CityOfCharlotte'")

    def print_modifiable_info(self):
        """
        print_modifiable_info print all info capable of being modified
        """
        super().generate_city_current_default_strs()
        super().print_modifiable_info()
        self.generate_city_current_default_strs()

        Printer.print_yellow(f"Special District Title: {self.special_district_title}")
        Printer.print_yellow(self.special_district_current_default_str)

    def generate_city_current_default_strs(self):
        super().generate_city_current_default_strs()
        current_special_district = (
            self.special_district_rate
            if self.special_district_rate is not None
            else None
        )
        # TODO Maybe depreciated
        # current_special_district_title = (
        #     self.special_district_title
        #     if self.special_district_title is not None
        #     else None
        # )

        # inital_special_district = self.inital_special_district_rate = None
        # inital_special_district_title = None

        # format if not none
        if current_special_district is not None:
            current_special_district = f"{current_special_district:.4g}"
        else:
            current_special_district = None

        title = (
            self.special_district_title
            if self.special_district_title is not None
            else "Special District"
        )

        self.special_district_current_default_str = (
            f"{title}: {current_special_district}"
        )

    def print_all_info(self):
        """
        print_all_info print all county info
        """
        print(f"City Name: {self.city_name}")
        print(f"City Rate: {self.city_wide_rate}")
        print(f"City Rate Title: {self.city_wide_rate_title}")
        print(f"Police Rate: {self.police_rate}")
        print(f"Police Rate Title: {self.police_title}")
        print(f"Fire Rate: {self.fire_rate}")
        print(f"Fire Rate Title: {self.fire_title}")

    #     def print_city_selected_info(self):
    #         # Print super class info
    #         super().print_city_selected_info()
    #
    #         Printer.print_green(f"{self.get_city_name()} Specific Info...")
    #         # print City of Charlotte specific info (special districts)
    #         Printer.print_yellow(
    #             f"Special District: {self.special_district_title} | Default: {None}"
    #         )
    #         Printer.print_yellow(
    #             f"Special District Rate: {self.special_district_rate} | Default: {None}"
    #         )

    def generate_city_statistics(self):
        super().generate_city_statistics()

        if self.special_district_rate is not None:
            self.city_statistics["SPECIAL_DISTRICT"] = {
                self.special_district_title: self.special_district_rate
            }
        else:
            self.city_statistics["SPECIAL_DISTRICT"] = None

        return self.city_statistics

    # TODO Check for neccecity of this method remianing, or is this supposed to be unused and removed?
    # def generate_CITY_substatements(self, city_stats, countywide_only, city_exists):
    #     return super().generate_CITY_substatements(
    #         city_stats, countywide_only, city_exists
    #     )
