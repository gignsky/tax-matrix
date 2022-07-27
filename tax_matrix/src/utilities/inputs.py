"""
    Class to help with inputs
"""

from .testers import InputTesters
from .printers import Printer
from .logic import LogicalWork


class InputHelper:
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
        INPUT_LOOP = True

        while INPUT_LOOP:
            Printer.liner()

            print(prompt)

            print()

            Printer.print_dict(dictionary)

            Printer.liner()

            inputted_value = input(
                "Please ENTER Value associated with your selection: "
            )

            Printer.liner()

            try:
                InputTesters.verify_int(inputted_value) is not None
                INPUT_LOOP = False
            except:
                pass

        return dictionary[inputted_value]

    @staticmethod
    def option_bool(question):
        """
        main will grab true or false from user (1 or 0) in order to determine how the user wishes to move forwards
        Returns:
            Bool
        """

        INPUT_LOOP = True
        while INPUT_LOOP:
            Printer.liner()

            print(question)

            Printer.liner()
            prompt = " Select '0' for NO and '1' for YES: "
            inputted_value = input(prompt)

            Printer.liner()

            bool_value = InputTesters.verify_bool(inputted_value)

            try:
                bool_value is not None
                INPUT_LOOP = False
            except:
                pass

        return bool_value

    @staticmethod
    def price_grabber():
        """
        request contract price from user


        Returns:
            float: prompted sales price
            str: pretty string with $ and commas with truncated cents
        """

        INPUT_LOOP = True
        while INPUT_LOOP:
            Printer.liner()

            # set prompt for
            prompt = "Please ENTER the final contract sale price of the subject home: "
            inputted_item = input(prompt)

            price_int = InputTesters.verify_int(inputted_item)

            if price_int != None:
                price_pretty = f"${price_int:6,.0f}"
                INPUT_LOOP = False

        Printer.liner()
        return price_int, price_pretty

    @staticmethod
    def county_grabber(county_list):
        county_dict = LogicalWork.convert_list_to_dict("COUNTY", county_list)
        county_dict_with_names = LogicalWork.convert_class_dict_to_dict_with_names(
            "COUNTY", county_list
        )

        INPUT_LOOP = True
        while INPUT_LOOP:
            Printer.liner()

            # print counties
            Printer.print_dict(county_dict_with_names)

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

            if county_var != None:
                INPUT_LOOP = False

        return county_var

    @staticmethod
    def city_grabber(city_list):
        city_dict = LogicalWork.convert_list_to_dict("CITY", city_list)
        city_dict_with_names = LogicalWork.convert_class_dict_to_dict_with_names(
            "CITY", city_dict
        )

        INPUT_LOOP = True
        while INPUT_LOOP:
            Printer.liner()

            # print counties
            Printer.print_dict(city_dict_with_names)

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

            if city_var != None:
                INPUT_LOOP = False

        return city_var
