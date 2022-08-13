"""
    generic city class
"""

from . import Printer
from . import InputHelper
from . import debugpy
from . import cls
from . import LogicalWork


class City:

    def __init__(
        self,
        city_name,
        city_wide_rate,
        city_wide_rate_title,
        police_rate,
        police_title,
        fire_rate,
        fire_title,
    ):
        self.city_name = city_name
        self.city_wide_rate = city_wide_rate
        self.city_wide_rate_title = city_wide_rate_title
        self.police_rate = police_rate
        self.police_title = police_title
        self.fire_rate = fire_rate
        self.fire_title = fire_title
        Printer.print_green(
            f"New City and/or Town of {self.city_name} has been loaded into Memory"
        )

        # saves for inital values
        self.inital_police_rate = self.police_rate
        self.inital_fire_rate = self.fire_rate

    def get_city_name(self):
        return self.city_name

    def modify_or_keep(self):
        INPUT_LOOP = True

        while INPUT_LOOP:
            Printer.short_liner()
            self.print_modifiable_info()
            Printer.short_liner()

            modify = InputHelper.choice_bool(
                "Would you like to disable any of the above Police and/or Fire rates?\n **Please note that any item showing a rate of 'None' will\n NOT appear in the final statement and is already disabled**"
            )

            if modify is not None:
                if modify:
                    self.which_modify()
                else:
                    INPUT_LOOP = False

    def get_police_and_fire_strings(self):
        return self.police_current_default_str, self.fire_current_default_str

    def update_police_and_fire_rates_for_string(self, police_rate, fire_rate):
        self.police_rate = police_rate
        self.fire_rate = fire_rate

    def which_modify(self):
        """
        which_modify helps to determine if one should modify the values available options on the cities services
        """
        MOD_LOOP = True

        print("Note a value of 'None' will not appear in final statement")

        while MOD_LOOP:
            self.generate_CITY_current_default_strs()
            mod_dict = {
                0: "Quit",
                1: self.police_current_default_str,
                2: self.fire_current_default_str,
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
            else:
                debugpy.breakpoint()
                print("ERROR IN CLASS 'City'")

    def modify_police(self):
        enable = InputHelper.on_or_off_rate(
            "Police", self.inital_police_rate, self.police_rate
        )
        if enable:
            self.police_rate = self.inital_police_rate
        else:
            self.police_rate = None

        cls()
        Printer.print_green(f"Police Rate updated to: {self.police_rate}")

    def modify_fire(self):
        enable = InputHelper.on_or_off_rate(
            "Fire", self.inital_fire_rate, self.fire_rate
        )
        if enable:
            self.fire_rate = self.inital_fire_rate
        else:
            self.fire_rate = None

        cls()
        Printer.print_green(f"Fire Rate updated to: {self.fire_rate}")

    def print_modifiable_info(self):
        """
        print_modifiable_info print all info capable of being modified
        """
        self.generate_CITY_current_default_strs()

        Printer.print_green(self.city_name)
        if self.city_wide_rate is not None:
            Printer.print_green(f"City Rate: {self.city_wide_rate:.6g}")
        else:
            Printer.print_green("City has no citywide rate")
        Printer.print_yellow(f"Police Rate Title: {self.police_title}")
        Printer.print_yellow(self.police_current_default_str)
        Printer.print_yellow(f"Fire Rate Title: {self.fire_title}")
        Printer.print_yellow(self.fire_current_default_str)

    def generate_CITY_current_default_strs(self):
        current_police = self.police_rate if self.police_rate is not None else None
        current_fire = self.fire_rate if self.fire_rate is not None else None
        inital_police = (
            self.inital_police_rate if self.inital_police_rate is not None else None
        )
        inital_fire = (
            self.inital_fire_rate if self.inital_fire_rate is not None else None
        )

        # format if not none
        if current_police is not None:
            current_police = f"{current_police:.6g}"
        else:
            current_police = None

        if current_fire is not None:
            current_fire = f"{current_fire:.6g}"
        else:
            current_fire = None

        if inital_police is not None:
            inital_police = f"{inital_police:.6g}"
        else:
            inital_police = None

        if inital_fire is not None:
            inital_fire = f"{inital_fire:.6g}"
        else:
            inital_fire = None

        #TODO Start here for pylint then work your way down to finish up pylnting all of the classes and then localities, then work on porting locality classes over to the special_county_classes folder, maybe one with a special class for waste options

        self.police_current_default_str = (
            f"Police Rate: {current_police} | STANDARD RATE: {self.inital_police_rate}"
        )
        self.fire_current_default_str = (
            f"Fire Rate: {current_fire} | STANDARD RATE: {self.inital_fire_rate}"
        )

    # def print_city_selected_info(self):
    #     Printer.print_green("City...")
    #     Printer.print_yellow(f"City Name: {self.city_name}")
    #     Printer.print_yellow(f"Citywide Tax Rate: {self.city_wide_rate}")
    #     Printer.print_yellow(
    #         f"City Police Rate: {self.police_rate} | Default: {self.inital_police_rate:.6g}"
    #     )
    #     Printer.print_yellow(
    #         f"City Fire Rate: {self.fire_rate} | Default: {self.inital_fire_rate:.6g}"
    #     )

    def generate_city_statistics(self):
        self.city_statistics = {}
        if self.city_wide_rate is not None:
            self.city_statistics["CITYWIDE"] = {
                self.city_wide_rate_title: self.city_wide_rate
            }
        else:
            self.city_statistics["CITYWIDE"] = None
        if self.police_rate is not None:
            self.city_statistics["POLICE"] = {self.police_title: self.police_rate}
        else:
            self.city_statistics["POLICE"] = None
        if self.fire_rate is not None:
            self.city_statistics["FIRE"] = {self.fire_title: self.fire_rate}
        else:
            self.city_statistics["FIRE"] = None

        return self.city_statistics

    def generate_CITY_substatements(self, city_stats, with_county_no_city, city_exists):
        _, dicts_values = LogicalWork.no_index_dict_to_two_lists(city_stats)
        city_keys, city_values = LogicalWork.with_index_dict_to_two_lists(dicts_values)
        return_statement = ""

        if not with_county_no_city:
            if city_exists:
                for title, rate in zip(city_keys, city_values):
                    if type(title) is list:
                        title = str(title[0])

                    if "Fee" not in title:
                        substatement = (
                            return_statement
                            + LogicalWork.substatement_maker(rate, title)
                        )
                        return_statement += substatement
        else:
            Printer.liner()
            debugpy.breakpoint()
            Printer.print_red("ERROR IN SUBSTATEMENT GENERATOR")
            Printer.liner()

        return return_statement

    def check_contains_fees(self, city_keys, city_values):
        for key, value in zip(city_keys, city_values):
            if "Fee" in key:
                return True

            if value is not None:
                check_str = list(value.keys())[0]
                if "Fee" in check_str:
                    return True

        return False

    def generate_city_fees_string(self, city_keys, city_values):
        city_fee_string = ""
        if city_keys is not None:
            for key, fee in zip(city_keys, city_values):
                if "Fee" in key:
                    city_fee_string = city_fee_string + LogicalWork.substatement_maker(
                        f"${fee:,.2f}", key
                    )

                elif fee is not None:
                    if type(fee) is dict:
                        check_str = list(fee.keys())[0]
                        inner_fee = fee[check_str]

                        if "Fee" in check_str:
                            city_fee_string = (
                                city_fee_string
                                + LogicalWork.substatement_maker(
                                    f"${inner_fee:,.2f}", check_str
                                )
                            )

        return city_fee_string

    def generate_city_total_fees(self, city_keys, city_values):
        total_of_fees = 0
        for key, fee in zip(city_keys, city_values):
            if "Fee" in key:
                if "Fee" in check_str:
                    total_of_fees += fee

            elif fee is not None:
                if type(fee) is dict:
                    check_str = list(fee.keys())[0]
                    if "Fee" in check_str:
                        inner_fee = fee[check_str]
                        total_of_fees += inner_fee

        return total_of_fees
