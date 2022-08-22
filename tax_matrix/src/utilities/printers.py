"""
    contains classes designed to assist in general printing outputs
"""
from . import Fore, tprint


class Printer:
    """
    generic printer for all your printing needs, this is a class full of static methods only
    """

    @staticmethod
    def liner():
        """
        liner prints LONG solid cyan line
        """
        liner = "=========================================================================================="

        print(Fore.CYAN + liner)
        print(Fore.RESET)

    @staticmethod
    def short_liner():
        """
        short_liner prints SHORT light-yellow line
        """
        short_liner = "=========================================="
        print(Fore.LIGHTYELLOW_EX + short_liner)
        print(Fore.RESET)

    @staticmethod
    def inside_liner(line):
        """
        inside_liner prints item inside line TODO depreciate

        Args:
            line (str): string to print
        """
        Printer.liner()
        print(line)
        Printer.liner()

    @staticmethod
    def print_green(line):
        """
        print_green prints passed item in green

        Args:
            line (str): string to print
        """
        print(Fore.GREEN + line)
        print(Fore.RESET)

    @staticmethod
    def print_yellow(line):
        """
        print_yellow prints passed item in yellow

        Args:
            line (str): string to print
        """
        print(Fore.YELLOW + line)
        print(Fore.RESET)

    @staticmethod
    def print_red(line):
        """
        print_red prints passed item in Red

        Args:
            line (str): string to print
        """
        print(Fore.RED + line)
        print(Fore.RESET)

    @staticmethod
    def print_cyan(line):
        """
        print_cyan prints passed item in Cyan

        Args:
            line (str): string to Print
        """
        print(Fore.CYAN + line)
        print(Fore.RESET)

    @staticmethod
    def print_dict_containing_index(dictionary_value):
        """
        Print a dict with index values next to dict content per value:

        KEY VALUE. ITEM NAME

        Args:
            any dict
        """

        for index_num in dictionary_value:
            print(f"{index_num}. {dictionary_value[index_num]}")

    @staticmethod
    def print_dict_with_inner_dict_and_index(dictionary_value):
        """
        Print a dict with index values next to dict content (which is printed nicely) per item:

        INDEX_NUM. INNER_DICT_KEY : INNER_DICT_VALUE

        Args:
            any dict
        """

        for key in dictionary_value:
            inner_dict = dictionary_value[key]

            inner_key = list(inner_dict.keys())[0]
            inner_value = inner_dict[inner_key]

            print(f"{key}. {inner_key} : {inner_value}")

    @staticmethod
    def print_dict_with_statement(dictionary_value):
        """
        Print a dict with key values next to dict content per value:

        KEY VALUE. ITEM NAME

        Args:
            any dict
        """

        for key in dictionary_value:
            statement = dictionary_value[key]
            print(f"{key}. {statement}")

    @staticmethod
    def print_special_service_dict_with_single_option_and_quit_option(
        dictionary, quit_option
    ):
        """
        Print a dict with key values next to dict content per value:

        KEY VALUE. ITEM TITLE - RATE: RATE

        Args:
            any dict
        """

        if quit_option:
            print("0. Quit")

        for key in dictionary:
            item_in_dict = dictionary[key]
            title = list(item_in_dict.keys())[0]
            rate = item_in_dict[title]

            print(f"{key}. {title} - Rate: {rate}")

    @staticmethod
    def welcome_to_program(version, date):
        """
        welcome message for entire script

        Args:
            version (str) : version of script
            rev_date (str) : most recent revision date
        """

        Printer.liner()

        print(Fore.GREEN + "Welcome to the NEW & REVISED")

        tprint("Tax Matrix!")

        Printer.liner()

        print(Fore.RED + f"Current Version: {version}; as Revised On: {date}")

        Printer.liner()

    @staticmethod
    def welcome_county(county):
        """
        Welcome Message for Counties

        Args:
            name (str): county name
        """

        Printer.liner()

        # print welcome line
        print(Fore.BLUE + "Welcome to the Tax Matrix for:")

        # print pretty ascii art for county name
        tprint(county)

        # print price
        # print(f"Subject Sale Price: {price_pretty}")

        Printer.liner()

    @staticmethod
    def end_program_message():
        """
        end_program_message Print thank you message
        """
        Printer.liner()

        print(Fore.RED + "Thank you for using the NEW & REVISED")

        tprint("Tax Matrix!")

        Printer.liner()

    @staticmethod
    def welcome_city(city):
        """
        welcome_city welcomes user to city

        Args:
            city (str): name of city
        """
        Printer.liner()

        # print welcome line
        print(Fore.BLUE + "Welcome to the Tax Matrix for:")

        # print pretty ascii art for county name
        tprint(city)

        # print price
        # print(f"Subject Sale Price: {price_pretty}")

        Printer.liner()
