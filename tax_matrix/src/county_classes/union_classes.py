

import debugpy
from . import Printer
from . import InputHelper
from . import cls
from . import general_classes

class Union(general_classes.County):
    """
    Union county specific class for union co

    Args:
        classes (obj): main county class obj
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

        #set inital values
        self.debt_budgetary_fund_title = None
        self.debt_budgetary_fund_rate = None
        self.special_fire_title = None
        self.special_fire_rate = None
        self.special_fire_department_default_str = None
        self.special_debt_budget_default_str = None

    def set_inital_values(
        self,
        debt_budgetary_fund_title,
        debt_budgetary_fund_rate,
    ):
        """
        set_inital_values sets inital values for county specific rates

        Args:
            debt_budgetary_fund_title (str): title
            debt_budgetary_fund_rate (float): rate
        """
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

        input_loop = True

        while input_loop:

            options_dict = {
                0: "Return to Main Menu",
                1:
                f"{self.inital_debt_budgetary_fund_title} - Rate: {self.debt_budgetary_fund_rate} | DEFAULT RATE: {self.inital_debt_budgetary_fund_rate}",
                2: "Modify Special Fire Districts for Union Co.",
            }

            modify_option = InputHelper.input_from_dict(
                options_dict,
                "Do you wish to modify any of the below options?")

            cls()

            if modify_option == options_dict[0]:
                input_loop = False
            elif modify_option == options_dict[1]:
                self.mod_budgetary_fund()
            elif modify_option == options_dict[2]:
                self.mod_special_fire()
            else:
                debugpy.breakpoint()
                print("ERROR IN CLASS 'Union'")

    def mod_budgetary_fund(self):
        """
        mod_budgetary_fund modify budgetary rate for entire county
        """
        include = None
        while include is None:
            Printer.short_liner()
            Printer.print_green(self.inital_debt_budgetary_fund_title)
            Printer.short_liner()
            Printer.print_yellow(
                f"CURRENT RATE: {self.debt_budgetary_fund_rate}")
            Printer.print_yellow(
                f"DEFAULT RATE: {self.inital_debt_budgetary_fund_rate}")
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
                "Debt Budgetary Fund Updated...\n& it will NOT be included in statement."
            )
            Printer.short_liner()

    def mod_special_fire(self):
        """
        mod_special_fire modify special fire rate
        """
        include = None
        while include is None:
            Printer.print_special_service_dict_with_single_option_and_quit_option(
                self.special_fire_dict, quit_option=False)

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
                    Printer.print_yellow(
                        "No Special Fire Rate Currently Selected")

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
                "Special Fire Updated to NOT be included in statement")
            Printer.short_liner()

    def generate_county_statistics(self):
        super().generate_county_statistics()

        # debt budget fund
        if self.debt_budgetary_fund_rate is not None:
            self.county_statistics[
                self.debt_budgetary_fund_title] = self.debt_budgetary_fund_rate

        # special fire
        if self.special_fire_rate is not None:
            self.county_statistics[
                self.special_fire_title] = self.special_fire_rate

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
        generate_SPECIAL_current_default_strs generate spcial default string for special rates
        """
        # special fire districts
        current_fire_department = (self.special_fire_rate
                                   if self.special_fire_rate is not None else
                                   None)

        if current_fire_department is not None:
            current_fire_department = f"{current_fire_department:.6g}"
        else:
            current_fire_department = None

        if current_fire_department is not None:
            self.special_fire_department_default_str = f"Special Fire District for Union County: {self.special_fire_title} - Rate: {current_fire_department}"
        else:
            self.special_fire_department_default_str = (
                "No Special Fire District Selected.")

        # debt tax
        current_debt_budget = (self.debt_budgetary_fund_rate
                               if self.debt_budgetary_fund_rate is not None
                               else None)

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
                    self.police_rate, self.fire_rate)

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
                mod_dict,
                "Please Select Number from below options to modify or Quit: ")

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
        current_special_district_rate = (self.special_district_rate
                                         if self.special_district_rate
                                         is not None else None)

        #TODO Might be depreciated
        # current_special_district_name = (self.special_district_name
        #                                  if self.special_district_name
        #                                  is not None else None)

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
        super().generate_city_current_default_strs()
        super().print_modifiable_info()

        Printer.print_yellow(
            f"Special District Title: {self.inital_special_district_name}")
        if self.special_district_rate is not None:
            Printer.print_yellow(
                f"Special District Rate: {self.special_district_rate:.6g}")
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
