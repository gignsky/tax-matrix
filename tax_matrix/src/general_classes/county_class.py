"""
    generic county class
"""

from . import LogicalWork
from . import Printer
from . import InputHelper
from . import cls
from . import debugpy
from . import SpecialItems


class County:
    """
    generic county class
    """

    def __init__(
        self,
        county_name,
        county_state,
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
    ):
        self.county_name = county_name
        self.county_state = county_state
        self.county_wide_rate_title = county_wide_rate_title
        self.county_wide_rate = county_wide_rate
        self.county_wide_fire_title = county_wide_fire_title
        self.county_wide_fire_rate = county_wide_fire_rate
        self.county_wide_police_title = county_wide_police_title
        self.county_wide_police_rate = county_wide_police_rate
        self.county_wide_ems_title = county_wide_ems_title
        self.county_wide_ems_rate = county_wide_ems_rate
        self.all_cities = all_cities
        self.city = None
        self.special_stuff = special_stuff

        # set county service inital options
        self.county_wide_fire_rate_inital = self.county_wide_fire_rate
        self.county_wide_police_rate_inital = self.county_wide_police_rate
        self.county_wide_ems_rate_inital = self.county_wide_ems_rate

        self.update_county_services()

        self.county_services_exists = LogicalWork.check_county_services_exist(
            self.county_services
        )

        # Printer.inside_liner(f"Initalized {county_name} and all cities and towns")

        # inital error fixes to define initally
        self.special_stuff_class = self.initalize_special_stuff_class()
        self.county_statistics = {}
        self.county_services_modify_options_with_no_quit = None

    def initalize_special_stuff_class(self):
        """
        initalize_special_stuff_class

        Returns:
            class or None: returns class for specialItems
        """
        if self.special_stuff is not None:
            item = SpecialItems(self.special_stuff[0], self.special_stuff[1])
        else:
            item = None

        return item

    # add items
    def add_city(self, city):
        """
        add_city allows adding city to county class

        Args:
            city (obj): object containing selected city
        """
        self.city = city

    # remove items
    def remove_city(self):
        """
        remove_city removes city and resets the city value to None; no conditions
        """
        self.city = None

    # get items
    def get_county_name(self):
        """
        get_county_name

        Returns:
            str: county name
        """
        return self.county_name

    def get_county_wide_rate(self):
        """
        get_county_wide_rate

        Returns:
            str: str with county wide rate
        """
        print(f"County Rate is: {self.county_wide_rate}")
        return self.county_wide_rate

    def get_cities(self):
        """
        get_cities returns all cities

        Returns:
            list: list of all cities
        """
        return self.all_cities

    def get_special_options_title(self):
        """
        get_special_options_title

        Returns:
            str: none or error
        """
        if self.special_stuff is None:
            return "None"
        else:
            # debugpy.breakpoint()
            return f"ERROR | SPECIAL OPTIONS NOT CONFIGURED IN {self.get_county_name()}'s Class"

    def get_state(self):
        """
        get_state

        Returns:
            str: two letter state string
        """
        return self.county_state

    # modify items
    def which_modify_county_services(self):
        """
        which_modify_county_services
        """
        mod_loop = True

        print("Note a value of 'None' will not appear in final statement")

        while mod_loop:
            self.update_county_services()
            self.county_services_modify_options_with_no_quit = (
                LogicalWork.create_options_dict_from_county_services_list_with_quit(
                    self.county_services
                )
            )

            which_modify = InputHelper.input_from_dict_with_statement(
                self.county_services_modify_options_with_no_quit,
                "Available County Services to Modify: ",
            )

            # cls()

            if which_modify is not None:
                # quit
                if "Quit" == which_modify:
                    mod_loop = False

                else:
                    # statement = list(which_modify.keys())[0]
                    self.modify_countywide_services(which_modify)
            else:
                mod_loop = False

    def modify_countywide_services(self, dictionary):
        """
        modify_county_service will modify county services

        Args:
            dictionary (dict): dictionary with service to modify
        """
        title = list(dictionary.keys())[0]
        rate_dict = dictionary[title]
        current_rate = list(rate_dict.keys())[0]
        inital_rate = rate_dict[current_rate]

        # police
        if "Police" in title:
            return_bool = InputHelper.on_or_off_rate(title, inital_rate, current_rate)
            if return_bool:
                self.county_wide_police_rate = inital_rate
            else:
                self.county_wide_police_rate = None

        # fire
        elif "Fire" in title:
            return_bool = InputHelper.on_or_off_rate(title, inital_rate, current_rate)
            if return_bool:
                self.county_wide_fire_rate = inital_rate
            else:
                self.county_wide_fire_rate = None

        # ems
        elif "EMS" in title:
            return_bool = InputHelper.on_or_off_rate(title, inital_rate, current_rate)
            if return_bool:
                self.county_wide_ems_rate = inital_rate
            else:
                self.county_wide_ems_rate = None

        # error
        else:
            debugpy.breakpoint()
            Printer.print_red("There is an ERROR in county service modification")

    # update items
    def update_county_services(self):
        """
        update_county_services
        """
        # county service combination help
        self.county_services = [
            {
                self.county_wide_fire_title: {
                    "INITAL": self.county_wide_fire_rate_inital,
                    "CURRENT": self.county_wide_fire_rate,
                }
            },
            {
                self.county_wide_police_title: {
                    "INITAL": self.county_wide_police_rate_inital,
                    "CURRENT": self.county_wide_police_rate,
                }
            },
            {
                self.county_wide_ems_title: {
                    "INITAL": self.county_wide_ems_rate_inital,
                    "CURRENT": self.county_wide_ems_rate,
                }
            },
        ]

    # logic
    def check_contains_fees(self, county_keys, county_values):
        """
        check_contains_fees checks if items contain fees

        Args:
            county_keys (list): list of county keys
            county_values (list): list of county values

        Returns:
            bool: true or false
        """
        for key, value in zip(county_keys, county_values):
            if "Fee" in key:
                if value is not None:
                    return True

        return False

    # select items
    def select_city(self):
        """
        select_city helps select all cities

        Returns:
            obj: city object
        """
        city = InputHelper.input_from_dict(self.all_cities, "")
        return city

    def modify_special_options(self):
        """
        select_special_options placeholder for ensuring functionality with countys not containing special options
        """
        if self.special_stuff is not None:
            self.special_stuff_class.general_modify_decisions()
        else:
            Printer.short_liner()
            Printer.print_red(f"NO SPECIAL OPTIONS FOR {self.get_county_name()}")
            Printer.short_liner()

    def select_countywide_services(self):
        """
        select_county_services placeholder for ensuring functionality with countys not containing services
        """
        if not self.county_services_exists:  # no county services
            Printer.short_liner()
            Printer.print_red(f"NO COUNTY SERVICE OPTIONS FOR {self.get_county_name()}")
            Printer.short_liner()
        else:  # there are options to modify

            input_loop = True
            while input_loop:
                self.print_county_selected_info()

                if self.county_services_modify_options_with_no_quit is not None:
                    modify = InputHelper.choice_bool(
                        "Would you like to modfy use of any of the above rates?"
                    )

                    cls()

                    if modify is not None:
                        if modify:
                            self.which_modify_county_services()
                        else:
                            input_loop = False
                    else:
                        pass

                else:
                    input_loop = False

    # outputs
    def print_county_selected_info(self):
        """
        print_county_selected_info
        """
        Printer.print_green("County...")
        Printer.print_yellow(f"County Name: {self.county_name}")
        Printer.print_yellow(f"Countywide Tax Rate: {self.county_wide_rate}")

        self.update_county_services()

        self.county_services_modify_options_with_no_quit = (
            LogicalWork.create_options_dict_from_county_services_list_no_quit(
                self.county_services
            )
        )

        Printer.print_cyan("...")

        # countywide services fire/police/ems stuff
        if self.county_services_modify_options_with_no_quit is None:
            Printer.print_red(
                f"NO COUNTYWIDE SERVICE OPTIONS FOR {self.get_county_name()}"
            )
        else:
            for item in self.county_services_modify_options_with_no_quit:
                Printer.print_yellow(item)

        # special rates and fees
        if self.special_stuff is not None:
            special_rates_and_fees_statement_list = (
                self.special_stuff_class.generate_statistics_statement()
            )

            for item in special_rates_and_fees_statement_list:
                if item is not None:
                    for subitem in item:
                        Printer.print_yellow(subitem)

        else:
            Printer.print_red("No Special County Fees/Rates")

    # generate items
    def generate_county_only_statement_no_fee(self):
        """
        generate_county_only_statement_no_fee
        """
        titles, rates = LogicalWork.no_index_dict_to_two_lists(self.county_statistics)

        items_added = 0
        for title, rate in zip(titles, rates):
            if items_added != 0:
                if "Fee" not in title:
                    if rate is not None:
                        return_statement = (
                            return_statement
                            + LogicalWork.substatement_maker(rate, title)
                        )
                        items_added += 1
            else:
                return_statement = f"({rate} - {title})"
                items_added += 1

        return return_statement, items_added

    ##generate items - rates
    def generate_county_statistics(self):
        """
        generate_county_statistics

        Returns:
            TODO FIGURE OUT: item with all county statistics
        """
        # get county stats
        self.county_statistics = {}

        if self.county_wide_rate is not None:
            self.county_statistics[self.county_wide_rate_title] = self.county_wide_rate
        else:
            pass
        if self.county_wide_fire_rate is not None:
            self.county_statistics[
                self.county_wide_fire_title
            ] = self.county_wide_fire_rate
        else:
            pass
        if self.county_wide_police_rate is not None:
            self.county_statistics[
                self.county_wide_police_title
            ] = self.county_wide_police_rate
        else:
            pass
        if self.county_wide_ems_rate is not None:
            self.county_statistics[
                self.county_wide_ems_title
            ] = self.county_wide_ems_rate
        else:
            pass

        if self.special_stuff is not None:
            special_stuff_dict = (
                self.special_stuff_class.generate_output_statement_statement()
            )
            if special_stuff_dict is not None:
                self.county_statistics.update(special_stuff_dict)

        return self.county_statistics

    def generate_county_multiply_rate(self, county_keys, county_values):
        """
        generate_county_multiply_rate

        Args:
            county_keys (list): list of county keys
            county_values (list): list of county values

        Returns:
            float: multiply rate
        """
        county_multiply_rate = 0.0
        for key, rate in zip(county_keys, county_values):
            if "Fee" not in key:  # only add items that don't have fee
                if rate is not None:  # only add items with None
                    county_multiply_rate += rate

        return county_multiply_rate

    ##generate items - fees
    def generate_county_fees_string(self, county_keys, county_values):
        """
        generate_county_fees_string generates string if fees are found for county

        Args:
            county_keys (list): list of county keys
            county_values (list): list of county values

        Returns:
            str: string containing all county fees
        """
        county_fee_string = ""
        for key, fee in zip(county_keys, county_values):
            if "Fee" in key:
                if fee is not None:
                    county_fee_string = (
                        county_fee_string
                        + LogicalWork.substatement_maker(f"${fee:,.2f}", key)
                    )

        return county_fee_string

    def generate_county_total_fees(self, county_keys, county_values):
        """
        generate_county_total_fees generate value of all county fees

        Args:
            county_keys (list): list of county keys
            county_values (list): list of county values

        Returns:
            float: value of all county fees
        """
        total_of_fees = 0
        for key, fee in zip(county_keys, county_values):
            if "Fee" in key:
                if fee is not None:
                    total_of_fees += fee

            elif fee is not None:
                if type(fee) is dict:
                    check_str = list(fee.keys())[0]
                    if "Fee" in check_str:
                        inner_fee = fee[check_str]
                        total_of_fees += inner_fee

        return total_of_fees
