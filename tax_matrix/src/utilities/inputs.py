"""
    Class to help with inputs
"""

#TODO FIX UP IMPORTS
import debugpy
from .testers import InputTesters
from .printers import Printer
from .logic import LogicalWork
from . import cls


class InputHelper:
    """
    generic input functions

    ***NOTE: all items in this class are "Static Methods"
    """

    @staticmethod
    def input_from_dict_get_index(dictionary, prompt, list_for_index):
        """
        input_from_dict grabs input from dictionary of options and returns value associated with dictionary item after testing it

        Args:
            dictionary (dict): dictionary of options
            prompt (str): prompt of what you are selecting in the dict placed prior to options with "Please Enter Value associated with your selection" printed for input
            list_for_index (list): a list of items to be associated with dictionary value that is selected by nature of the same index value entered by user

        Returns:
            dict[item]: item associated with selection
        """
        input_loop = True

        while input_loop:
            Printer.inside_liner(prompt)

            Printer.print_dict_containing_index(dictionary)

            Printer.liner()
            inputted_value = input(
                "Please ENTER Value associated with your selection: "
            )
            Printer.liner()

            value = InputTesters.verify_dict_selection(inputted_value, dictionary)
            if value is not None:
                index_value = int(inputted_value)
                return_item = list_for_index[index_value]
                input_loop = False

        return return_item

    @staticmethod
    def input_from_dict(dictionary, prompt):
        """
        input_from_dict grabs input from dictionary of options and returns value associated with dictionary item after testing it

        Args:
            dictionary (dict): dictionary of options
            prompt (str): prompt of what you are selecting in the dict placed prior to options with "Please Enter Value associated with your selection" printed for input

        Returns:
            dict[item]: item associated with selection
        """
        input_loop = True

        while input_loop:
            Printer.inside_liner(prompt)

            Printer.print_dict_containing_index(dictionary)

            Printer.liner()
            inputted_value = input(
                "Please ENTER Value associated with your selection: "
            )
            Printer.liner()

            value = InputTesters.verify_dict_selection(inputted_value, dictionary)
            if value is not None:
                input_loop = False

        return value

    @staticmethod
    def input_from_dict_with_inner_dict(dictionary, prompt):
        """
        input_from_dict grabs input from dictionary of options and returns value associated with dictionary item after testing it

        Args:
            dictionary (dict): dictionary of options
            prompt (str): prompt of what you are selecting in the dict placed prior to options with "Please Enter Value associated with your selection" printed for input

        Returns:
            dict[item]: item associated with selection
        """
        input_loop = True

        while input_loop:
            Printer.inside_liner(prompt)

            Printer.print_dict_with_inner_dict_and_index(dictionary)

            Printer.liner()
            inputted_value = input(
                "Please ENTER Value associated with your selection: "
            )
            Printer.liner()

            value = InputTesters.verify_dict_selection(inputted_value, dictionary)
            if value is not None:
                input_loop = False

        return value

    @staticmethod
    def input_from_dict_with_statement(dictionary, prompt):
        """
        input_from_dict grabs input from dictionary of options and returns value associated with dictionary item after testing it

        Args:
            dictionary (dict): dictionary of options
            prompt (str): prompt of what you are selecting in the dict placed prior to options with "Please Enter Value associated with your selection" printed for input

        Returns:
            dict[item]: item associated with selection
        """

        if dictionary is not None:

            input_loop = True

            while input_loop:
                Printer.inside_liner(prompt)

                Printer.print_dict_with_statement(dictionary)

                Printer.liner()
                inputted_value = input(
                    "Please ENTER Value associated with your selection: "
                )
                Printer.liner()

                value = InputTesters.verify_dict_selection(inputted_value, dictionary)

                if value is not None:
                    input_loop = False

            return value

        else:
            Printer.short_liner()
            Printer.print_red("NO options to modify...")
            Printer.short_liner()

    @staticmethod
    def choice_bool(question):
        """
        main will grab true or false from user (1 or 0) in order to determine how the user wishes to move forwards
        Returns:
            Bool
        """

        input_loop = True
        while input_loop:

            Printer.inside_liner(question)

            prompt = " Select '0' for NO and '1' for YES: "
            inputted_value = input(prompt)

            Printer.liner()

            bool_value = InputTesters.verify_bool(inputted_value)

            if bool_value is None:
                Printer.print_red(
                    f"'{inputted_value}' is not valid, please enter 1 or 0"
                )

            else:
                input_loop = False
                cls()

        return bool_value

    @staticmethod
    def choice_bool_with_header(question):
        """
        main will grab true or false from user (1 or 0) in order to determine how the user wishes to move forwards RETURNS NONE AND ERROR MESSAGE SO HEADER CAN BE RESTATED
        Returns:
            Bool
        """

        input_loop = True
        while input_loop:

            Printer.inside_liner(question)

            prompt = " Select '0' for NO and '1' for YES: "
            inputted_value = input(prompt)

            Printer.liner()

            bool_value = InputTesters.verify_bool(inputted_value)

            if bool_value is None:
                cls()
                Printer.print_red(
                    f"'{inputted_value}' is not valid, please enter 1 or 0"
                )
                return None

            else:
                input_loop = False
                cls()

        return bool_value

    @staticmethod
    def on_or_off_rate(pre_prompt, inital_rate, current_rate):
        """
        on_or_off checks if user would like to include the rate of for teh pre_prompted selection

        Args:
            pre_prompt (str): label of rate i.e. "POLICE" or "FIRE"
            rate (float): accurate rate of the pre_prompt
            current_rate (float): current rate being used
        """
        input_loop = True

        cls()

        while input_loop:
            Printer.short_liner()
            Printer.print_yellow(f"Current {pre_prompt} Rate: {current_rate}")
            Printer.short_liner()

            Printer.print_cyan(
                "Would you like to use the following rate in your statement?"
            )

            Printer.short_liner()
            Printer.print_green(f"{pre_prompt} Rate: {inital_rate}")
            Printer.short_liner()

            Printer.liner()
            inputted_value = input(
                "ENTER '1' to include above rate, and '0' to NOT include above rate: "
            )

            bool_value = InputTesters.verify_bool(inputted_value)

            if bool_value is not None:
                input_loop = False

        return bool_value

    @staticmethod
    def on_or_off_fee(pre_prompt, fee, current_fee):
        """
        on_or_off checks if user would like to include the rate of for teh pre_prompted selection

        Args:
            pre_prompt (str): label of rate i.e. "POLICE" or "FIRE"
            rate (float): accurate rate of the pre_prompt
            current_rate (float): current rate being used
        """
        input_loop = True

        cls()

        while input_loop:
            if current_fee is None:
                Printer.short_liner()
                Printer.print_yellow(f"Current {pre_prompt}: {None}")
                Printer.short_liner()
            else:
                Printer.short_liner()
                Printer.print_yellow(f"Current {pre_prompt}: {current_fee:.2f}")
                Printer.short_liner()

            Printer.print_cyan(
                "Would you like to use the following rate in your statement?"
            )

            Printer.short_liner()
            Printer.print_green(f"{pre_prompt}: ${fee:.2f}")
            Printer.short_liner()

            inputted_value = input(
                "ENTER '1' to include above rate, and '0' to NOT include above rate: "
            )

            Printer.liner()

            bool_value = InputTesters.verify_bool(inputted_value)

            if bool_value is not None:
                input_loop = False

        return bool_value

    @staticmethod
    def price_grabber():
        """
        request contract price from user


        Returns:
            int: prompted sales price
            str: pretty string with $ and commas with truncated cents
        """

        input_loop = True
        while input_loop:
            Printer.liner()

            # set prompt for
            prompt = "Please ENTER the final contract sale price of the subject home: "
            inputted_item = input(prompt)

            price_int = InputTesters.verify_int(inputted_item)

            if price_int is not None:
                price_pretty = f"${price_int:6,.0f}"
                input_loop = False

        Printer.liner()
        return price_int, price_pretty

    @staticmethod
    def county_grabber(county_list):
        """
        county_grabber gathers all county titles and then requests input from user to select county then returns county object

        Args:
            county_list (list): list of avaliable county objects

        Returns:
            object: selected county object
        """
        county_dict = LogicalWork.convert_list_to_dict("COUNTY", county_list)
        county_dict_with_names = LogicalWork.convert_class_dict_to_dict_with_names(
            "COUNTY", county_list
        )

        input_loop = True
        while input_loop:
            # print counties
            Printer.liner()
            Printer.print_dict_containing_index(county_dict_with_names)
            Printer.liner()
            # set prompt for
            prompt = "Please Enter the number associated with the county your subject is in: "
            inputted_item = input(prompt)

            if inputted_item == "0":
                return None
            else:
                county_var = InputTesters.verify_dict_selection(
                    inputted_item, county_dict
                )

            if county_var is not None:
                input_loop = False

        return county_var

    @staticmethod
    def city_grabber(city_list):
        """
        city_grabber gets list of all cities in county and requests selection from user before returning city object if selected

        Args:
            city_list (list): list of all city objects

        Returns:
            object: returns class object for city if selected; else returns 'None'
        """
        city_dict = LogicalWork.convert_list_to_dict("CITY", city_list)
        city_dict_with_names = LogicalWork.convert_class_dict_to_dict_with_names(
            "CITY", city_dict
        )

        input_loop = True
        while input_loop:
            # print counties
            Printer.liner()
            Printer.print_dict_containing_index(city_dict_with_names)
            Printer.liner()
            # set prompt for
            prompt = (
                "Please Enter the number associated with the City your subject is in: "
            )
            inputted_item = input(prompt)

            Printer.liner()

            city_var = InputTesters.verify_dict_selection(inputted_item, city_dict)

            if inputted_item == "0":
                return None
            else:
                city_var = InputTesters.verify_dict_selection(inputted_item, city_dict)

            if city_var is not None:
                input_loop = False

        return city_var

    @staticmethod
    def main_menu_options(options_dict):
        """
        main_menu_options gathers option for selection for main menu

        Args:
            options_dict (dict): dictionary of available options

        Returns:
            dict_value: value from dict to be used to select appropriate menu item in main.py
        """

        inputted_value = InputHelper.input_from_dict(
            options_dict,
            "Please ENTER number associated with the option you wish to select",
        )

        return inputted_value

    @staticmethod
    def per_item_item_input(item_type,default_multiple,current_multiple):
        cls()
        if item_type == "sqft":
            question="Please enter subject's Square Footage:"
        elif: item_type == "unit":
            question="Please enter quanity of units on subject property:"
        else:
            debugpy.breakpoint()

        while True:
            input_return=input(question)

            test_return=InputTesters.verify_int(input_return)

            if test_return is not None:
                if item_type == "sqft":
                    str_return=f"{test_return:,.0f} sqft"
                elif: item_type == "unit":
                    if test_return==1:
                        str_return=f"{test_return:.0f} unit"
                    else:
                        str_return=f"{test_return:.0f} units"
                return test_return,str_return
