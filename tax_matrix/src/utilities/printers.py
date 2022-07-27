"""
    contains classes designed to assist in general printing outputs
"""

from . import Fore, tprint


class Printer:
    @staticmethod
    def liner():
        LINER = "=========================================================================================="

        print(Fore.CYAN + LINER)
        print(Fore.RESET)

    @staticmethod
    def inside_liner(line):
        Printer.liner()
        print(line)
        Printer.liner()

    @staticmethod
    def print_dict(dictionary_value):
        """
        Print a dict with key values next to dict content per value:

        KEY VALUE. ITEM NAME

        Args:
            any dict
        """

        for key in dictionary_value:
            print(f"{key}. {dictionary_value[key]}")

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
