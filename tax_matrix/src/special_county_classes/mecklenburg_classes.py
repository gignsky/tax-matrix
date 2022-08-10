"""
    classes specific to mecklenburg county
"""

from . import cls
from . import debugpy

from . import InputHelper
from . import InputTesters
from . import Printer

from . import classes

class Mecklenburg(classes.County):
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
        waste_options,
        meck_services,
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
        # initalize dict of all options and services
        self.waste_options = waste_options
        self.meck_services = meck_services

        self.inital_waste_fee_setup(waste_options)
        self.inital_meck_services_setup(meck_services)

    def update_all_local_county_services(self):
        self.update_current_fees()
        self.update_current_rates()

    def inital_waste_fee_setup(self, waste_options):
        list_of_all_fee_classes = self.initalize_waste_fees(waste_options)

        self.meck_waste_class = list_of_all_fee_classes[0]
        self.clt_waste_class = list_of_all_fee_classes[1]
        self.huntersville_waste_class = list_of_all_fee_classes[2]

        self.list_of_waste_option_titles = [
            self.meck_waste_class.get_title(),
            self.clt_waste_class.get_title(),
            self.huntersville_waste_class.get_title(),
        ]

        self.update_current_fees()

    def update_current_fees(self):
        self.list_of_waste_options_fee_floats = [
            self.meck_waste_class.get_current_fee_float(),
            self.clt_waste_class.get_current_fee_float(),
            self.huntersville_waste_class.get_current_fee_float(),
        ]

        self.list_of_waste_options_fee_strings = [
            self.meck_waste_class.get_current_fee_string(),
            self.clt_waste_class.get_current_fee_string(),
            self.huntersville_waste_class.get_current_fee_string(),
        ]

    def initalize_waste_fees(self, waste_options):
        list_of_all_fee_classes = []
        for index in waste_options:
            list_of_all_fee_classes.append(WasteOption(waste_options, index))

        return list_of_all_fee_classes

    def inital_meck_services_setup(self, meck_services):
        list_of_all_services = self.initalize_service_rates(meck_services)

        self.police_clt_class = list_of_all_services[0]
        self.fire_clt_class = list_of_all_services[1]
        self.police_cornelius_class = list_of_all_services[2]
        self.fire_cornelius_class = list_of_all_services[3]
        self.police_davidson_class = list_of_all_services[4]
        self.fire_davidson_class = list_of_all_services[5]
        self.fire_huntersvile_class = list_of_all_services[6]
        self.police_huntersvile_class = list_of_all_services[7]
        self.fire_mint_hill_class = list_of_all_services[8]
        self.police_mint_hill_class = list_of_all_services[9]
        self.police_pineville_class = list_of_all_services[10]

        self.list_of_meck_service_titles = [
            self.police_clt_class.get_title(),
            self.fire_clt_class.get_title(),
            self.police_cornelius_class.get_title(),
            self.fire_cornelius_class.get_title(),
            self.police_davidson_class.get_title(),
            self.fire_davidson_class.get_title(),
            self.fire_huntersvile_class.get_title(),
            self.police_huntersvile_class.get_title(),
            self.fire_mint_hill_class.get_title(),
            self.police_mint_hill_class.get_title(),
            self.police_pineville_class.get_title(),
        ]

        self.update_current_rates()

    def update_current_rates(self):
        self.list_of_meck_services_rate_floats = [
            self.police_clt_class.get_current_rate_float(),
            self.fire_clt_class.get_current_rate_float(),
            self.police_cornelius_class.get_current_rate_float(),
            self.fire_cornelius_class.get_current_rate_float(),
            self.police_davidson_class.get_current_rate_float(),
            self.fire_davidson_class.get_current_rate_float(),
            self.fire_huntersvile_class.get_current_rate_float(),
            self.police_huntersvile_class.get_current_rate_float(),
            self.fire_mint_hill_class.get_current_rate_float(),
            self.police_mint_hill_class.get_current_rate_float(),
            self.police_pineville_class.get_current_rate_float(),
        ]

        self.list_of_meck_services_rate_strings = [
            self.police_clt_class.get_current_rate_string(),
            self.fire_clt_class.get_current_rate_string(),
            self.police_cornelius_class.get_current_rate_string(),
            self.fire_cornelius_class.get_current_rate_string(),
            self.police_davidson_class.get_current_rate_string(),
            self.fire_davidson_class.get_current_rate_string(),
            self.fire_huntersvile_class.get_current_rate_string(),
            self.police_huntersvile_class.get_current_rate_string(),
            self.fire_mint_hill_class.get_current_rate_string(),
            self.police_mint_hill_class.get_current_rate_string(),
            self.police_pineville_class.get_current_rate_string(),
        ]

    def initalize_service_rates(self, meck_services):
        list_of_all_rate_classes = []
        for index in meck_services:
            list_of_all_rate_classes.append(MeckService(meck_services, index))

        return list_of_all_rate_classes

    def select_special_options(self):
        """
        select_special_options options for waste and meck services to be added
        """

        INPUT_LOOP = True

        while INPUT_LOOP:
            self.print_special_stuff_options()

            modify = InputHelper.choice_bool(
                "Would you like to modify use any of the above Waste or Mecklenburg Services Fees and Rates?"
            )

            cls()

            if modify is not None:
                if modify:
                    self.which_modify_special_services()
                else:
                    INPUT_LOOP = False
            else:
                pass

    def print_special_stuff_options(self):
        Printer.short_liner()
        self.meck_waste_class.print_status_str()
        self.clt_waste_class.print_status_str()
        self.huntersville_waste_class.print_status_str()
        Printer.print_cyan("...")
        self.police_clt_class.print_status_str()
        self.fire_clt_class.print_status_str()
        self.police_cornelius_class.print_status_str()
        self.fire_cornelius_class.print_status_str()
        self.police_davidson_class.print_status_str()
        self.fire_davidson_class.print_status_str()
        self.fire_huntersvile_class.print_status_str()
        self.police_huntersvile_class.print_status_str()
        self.fire_mint_hill_class.print_status_str()
        self.police_mint_hill_class.print_status_str()
        self.police_pineville_class.print_status_str()
        Printer.short_liner()

    def which_modify_special_services(self):
        """
        which_modify helps to determine if one should modify the values available options on the County services

        SPECIFIC TO MECKLENBURG COUNTY
        """
        MOD_LOOP = True

        print("Note a value of 'None' will not appear in final statement")

        list_of_classes = [
            self.meck_waste_class,
            self.clt_waste_class,
            self.huntersville_waste_class,
            self.police_clt_class,
            self.fire_clt_class,
            self.police_cornelius_class,
            self.fire_cornelius_class,
            self.police_davidson_class,
            self.fire_davidson_class,
            self.fire_huntersvile_class,
            self.police_huntersvile_class,
            self.fire_mint_hill_class,
            self.police_mint_hill_class,
            self.police_pineville_class,
        ]

        while MOD_LOOP:
            self.update_all_local_county_services()

            mod_dict = {0: f"Quit"}

            index = 1
            for i in list_of_classes:
                mod_dict[index] = i.get_status_str()
                index += 1

            which_modify = InputHelper.input_from_dict(
                mod_dict,
                "Please Select Number from below options to modify or Quit: ",
            )

            cls()

            # quit
            if which_modify == mod_dict[0]:
                MOD_LOOP = False

            # to modify
            elif which_modify in mod_dict.values():
                for key, value in mod_dict.items():
                    if value == which_modify:
                        dict_key = key

                list_key = dict_key - 1

                class_to_mod = list_of_classes[list_key]

                class_to_mod.modify()

            else:
                debugpy.breakpoint()
                print("ERROR IN CLASS 'Mecklenburg'")

    def print_county_selected_info(self):
        # Print super class info
        super().print_county_selected_info()

        Printer.print_green(f"{self.get_county_name()} Specific Info...")

        # print Mecklenburg specific info (waste and police/fire)
        self.print_special_stuff_options()

    def generate_county_statistics(self):
        super().generate_county_statistics()

        for title, fee_string in zip(
            self.list_of_waste_option_titles, self.list_of_waste_options_fee_floats
        ):
            self.county_statistics[title] = fee_string
            # Printer.print_yellow(f"{title}: {fee_string}")

        # Printer.print_cyan("...")

        for title, rate_string in zip(
            self.list_of_meck_service_titles, self.list_of_meck_services_rate_floats
        ):
            self.county_statistics[title] = rate_string
            # Printer.print_yellow(f"{title}: {rate_string}")

        return self.county_statistics

    def get_special_options_title(self):
        return "Waste Fees & Meck Police/Fire"

class WasteOption:
    def __init__(self, waste_options_dict, positional_key):
        self.waste_options_dict = waste_options_dict
        self.option_inner_dict = waste_options_dict[positional_key]
        self.title = list(self.option_inner_dict.keys())[0]

        self.validate_and_set_default_fee()

        self.current_fee = None

    def validate_and_set_default_fee(self):
        tmp_default_option_fee = (
            self.option_inner_dict[self.title]
            if self.option_inner_dict[self.title] is not None
            else 0
        )

        if tmp_default_option_fee != 0:
            verified_float = InputTesters.verify_float(tmp_default_option_fee)

            self.default_option_fee = verified_float

        else:
            self.default_option_fee = 0

    def get_title(self):
        return self.title

    def get_default_fee_float(self):
        return self.default_option_fee

    def get_current_fee_float(self):
        return self.current_fee

    def get_current_fee_string(self):
        if self.current_fee is not None:
            return f"${self.current_fee:.2f}"
        else:
            return None

    def get_status_str(self):
        checked_current_fee, checked_default_fee = self.check_fees_for_none()

        return f"{self.title} - Current Fee: {checked_current_fee} | DEFAULT FEE: {checked_default_fee}"

    def print_status_str(self):
        checked_current_fee, checked_default_fee = self.check_fees_for_none()

        statement = f"{self.title} - Current Fee: {checked_current_fee} | DEFAULT FEE: {checked_default_fee}"

        if checked_current_fee != "None":
            Printer.print_green(statement)
        else:
            Printer.print_red(statement)

    def check_fees_for_none(self):
        if self.default_option_fee is not None:
            default = f"${self.default_option_fee:.2f}"
        else:
            default = "None"

        if self.current_fee is not None:
            current = f"${self.current_fee:.2f}"
        else:
            current = "None"

        return current, default

    def modify(self):
        enable = InputHelper.on_or_off_fee(
            self.title,
            self.default_option_fee,
            self.current_fee,
        )

        cls()

        if enable:
            self.current_fee = self.default_option_fee
        else:
            self.current_fee = None
        Printer.liner()
        if self.current_fee is not None:
            current_fee_to_print = f"${self.current_fee:.2f}"
        else:
            current_fee_to_print = "None"
        Printer.print_green(f"{self.title} updated to: {current_fee_to_print}")

class MeckService:
    def __init__(self, meck_services_dict, positional_key):
        self.meck_services_dict = meck_services_dict
        self.service_inner_dict = meck_services_dict[positional_key]
        self.service_title = list(self.service_inner_dict.keys())[0]

        self.validate_and_set_default_rate()

        self.current_rate = None

    def validate_and_set_default_rate(self):
        tmp_default_service_rate = (
            self.service_inner_dict[self.service_title]
            if self.service_inner_dict[self.service_title] is not None
            else 0
        )

        if tmp_default_service_rate != 0:
            verified_float = InputTesters.verify_float(tmp_default_service_rate)

            self.default_service_rate = verified_float

        else:
            self.default_service_rate = 0

    def get_title(self):
        return self.service_title

    def get_default_rate_float(self):
        return self.default_service_rate

    def get_current_rate_float(self):
        return self.current_rate

    def get_current_rate_string(self):
        if self.current_rate is not None:
            return f"{self.current_rate:.6g}"
        else:
            return None

    def get_status_str(self):
        checked_current_rate, checked_default_rate = self.check_rates_for_none()

        return f"{self.service_title} - Current Rate: {checked_current_rate} | DEFAULT RATE: {checked_default_rate}"

    def print_status_str(self):
        checked_current_rate, checked_default_rate = self.check_rates_for_none()

        statement = f"{self.service_title} - Current Rate: {checked_current_rate} | DEFAULT RATE: {checked_default_rate}"
        if checked_current_rate != "None":
            Printer.print_green(statement)
        else:
            Printer.print_red(statement)

    def check_rates_for_none(self):
        if self.default_service_rate is not None:
            default = f"{self.default_service_rate:.6g}"
        else:
            default = "None"

        if self.current_rate is not None:
            current = f"{self.current_rate:.6g}"
        else:
            current = "None"

        return current, default

    def modify(self):
        enable = InputHelper.on_or_off_rate(
            self.service_title, self.default_service_rate, self.current_rate
        )

        cls()

        if enable:
            self.current_rate = self.default_service_rate
        else:
            self.current_rate = None
        Printer.liner()
        if self.current_rate is not None:
            current_rate_to_print = f"{self.current_rate:.6g}"
        else:
            current_rate_to_print = "None"
        Printer.print_green(
            f"{self.service_title} Rate updated to: {current_rate_to_print}"
        )

class CityOfCharlotte(classes.City):
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

    def select_special_district(self):

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
        INPUT_LOOP = True

        while INPUT_LOOP:
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
                    INPUT_LOOP = False
            else:
                pass

    def which_modify(self):
        """
        which_modify helps to determine if one should modify the values available options on the cities services

        SPECIFIC TO CITY OF CHARLOTTE
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
                print("ERROR IN CLASS 'CityOfCharlotte'")

    def print_modifiable_info(self):
        """
        print_modifiable_info print all info capable of being modified
        """
        super().generate_CITY_current_default_strs()
        super().print_modifiable_info()
        self.generate_CITY_current_default_strs()

        Printer.print_yellow(f"Special District Title: {self.special_district_title}")
        Printer.print_yellow(self.special_district_current_default_str)

    def generate_CITY_current_default_strs(self):
        super().generate_CITY_current_default_strs()
        current_special_district = (
            self.special_district_rate
            if self.special_district_rate is not None
            else None
        )
        current_special_district_title = (
            self.special_district_title
            if self.special_district_title is not None
            else None
        )

        inital_special_district = self.inital_special_district_rate = None
        inital_special_district_title = None

        # format if not none
        if current_special_district is not None:
            current_special_district = f"{current_special_district:.6g}"
        else:
            current_special_district = None

        title = (
            self.special_district_title
            if self.special_district_title is not None
            else "Special District"
        )

        self.special_district_current_default_str = f"{title}: {current_special_district} | STANDARD RATE: {self.inital_special_district_rate}"

    def print_all_info(self):
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

    # def generate_CITY_substatements(self, city_stats, countywide_only, city_exists):
    #     return super().generate_CITY_substatements(
    #         city_stats, countywide_only, city_exists
    #     )
