"""
    Testing for all needs (most often it's inputs)
"""

from .printers import Printer
from . import Fore
from . import cls


class InputTesters:
    """
    InputTesters contains testing functions to help with inputs
    """

    #     @staticmethod
    #     def verify_float(float_value):
    #         try:
    #             float_value == float(float_value)
    #             float = float_value
    #         except:
    #             Printer.liner()
    #
    #             print(Fore.RED + f"entered value of '{float_value}' is not a float :(")
    #
    #             print(Fore.RESET + "please try again and enter an float")
    #
    #             Printer.liner()
    #
    #             float = None
    #
    #         return float

    @staticmethod
    def verify_int(int_value):
        """
        Verify that input is an interager

        Args:
            x (str): variable to check

        Returns:
            int or None: will return int if item is a valid interager otherwise will retrun None so loop can be restarted
        """

        if int_value != "":

            try:
                value = int(int_value)
            except TypeError:
                Printer.liner()

                print(Fore.RED + f"value of '{int_value}' is not an int :(")

                print(Fore.RESET + "please try again and enter an int")

                Printer.liner()

                value = None

        else:
            Printer.liner()

            print(Fore.RED + f"value of '{int_value}' is not an int :(")

            print(Fore.RESET + "please try again and enter an int")

            Printer.liner()

            value = None

        return value

    @staticmethod
    def verify_bool(bool_value):
        """
        verify_bool will check if an item is 1 or 0 and then associated with true or False

        Args:
            bool_value (str): user inputted string

        Returns:
            bool: true or false value
        """
        # try:
        check_var = InputTesters.verify_int(bool_value)
        # except:
        #     return None
        if check_var != 0 and check_var != 1:
            return None
        else:
            try:
                value = bool(check_var)
            except ValueError:
                Printer.liner()

                print(
                    Fore.RED
                    + f"Your input of '{check_var}' is neither ONE (1) nor ZERO (0),"
                )

                print(Fore.RESET + "Please try again!")

                Printer.liner()

                value = None

            return value

    @staticmethod
    def verify_float(float_value):
        """
        Verify that input is an float

        Args:
            x (str): variable to check

        Returns:
            int or None: will return int if item is a valid interager otherwise will retrun None so loop can be restarted
        """

        try:
            value = float(float_value)

        except ValueError:
            Printer.liner()

            print(Fore.RED + f"value of '{float_value}' is not a float :(")

            print(Fore.RESET + "please try again and enter an float")

            Printer.liner()

            value = None

        #         try:
        #             value=InputTesters.verify_int(float_value)
        #             value=float(value)
        #
        #         except:
        #             Printer.liner()
        #
        #             print(Fore.RED + f"value of '{float_value}' is not an int :(")
        #
        #             print(Fore.RESET + "please try again and enter an int")
        #
        #             Printer.liner()
        #
        #             value = None

        return value

    @staticmethod
    def verify_dict_selection(index_value, dictionary):
        """
        verify_dict_selection verifies if selection int is indeed an int and then if it is inside of the dictionary.

        Args:
            index_value (str): string from user input.
            dictionary (dict): dictionary to verify with

        Returns:
            item: item from dictionary assuming everything matches if not it will return a None value.
        """
        key_value = InputTesters.verify_int(index_value)

        if key_value is not None:
            try:
                value = dictionary[key_value]
            except KeyError:
                cls()

                Printer.liner()

                print(
                    Fore.RED
                    + f"Your input of '{index_value}' is not within the list of avaliable options"
                )

                print(Fore.RESET + "Please try again!")

                Printer.liner()

                value = None

            return value
