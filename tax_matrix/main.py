"""
    Main Function of Tax Matrix to help produce final product
    vscode-fold=3
"""

import debugpy
import src
from src import cls

# print a welcome message
src.utilities.printers.Printer.welcome_to_program(
    src.config.CURRENT_VERSION(), src.config.DATE_REVISED()
)

src.localities.load_all_counties("inital")


def main():
    """
    Main program that will terminate with statement and statistics
    """

    # return subject class object
    Subject = src.utilities.classes.Property()

    # get county list
    all_counties = src.utilities.classes.Counties.get_all_counties()

    # dict of avalable options
    options_dict = {
        0: "Quit Program & Output Statement",
        1: "Print Statisticts",
        2: "Modify Price",
        3: "Modify County",
        4: "Modify County Special Options",
        5: "Modify City and/or City Options\n...",
        99: "Reload Counties to Default Values",
    }

    MAIN_LOOP = True  # var to keep program running until stop is requested or neccecary
    INITAL_RUN = True  # var to set the inital run to run through all avaliable options
    HAS_PRICE = (
        False  # var sets has price var to false to indicate a price has not been loaded
    )

    # main loop
    while MAIN_LOOP:
        """
        main program loop
        """

        # test if inital run otherwise grab menu option
        if not INITAL_RUN:
            # select main menu options
            menu_option = src.utilities.inputs.InputHelper.main_menu_options(
                options_dict
            )
            cls()

        else:
            if INITAL_RUN == True:
                menu_option = options_dict[2]
                INITAL_RUN = "Get Price then County"
            else:
                menu_option = options_dict[3]
                INITAL_RUN = False

        # quit
        if menu_option == options_dict[0]:
            MAIN_LOOP = False

        # print current statistics
        elif menu_option == options_dict[1]:
            src.utilities.printers.Printer.liner()
            Subject.print_current_stats()
            src.utilities.printers.Printer.liner()
            wait()

        # price options
        elif menu_option == options_dict[2]:
            if HAS_PRICE:
                src.utilities.printers.Printer.short_liner()
                src.utilities.printers.Printer.print_yellow(
                    f"Current Price: {Subject.get_price_str()}"
                )
                src.utilities.printers.Printer.short_liner()
                src.utilities.printers.Printer.print_yellow(
                    "If you would like to keep this price input '0'"
                )
                src.utilities.printers.Printer.short_liner()

            # get price
            price_int, price_str = src.utilities.inputs.InputHelper.price_grabber()

            if price_int == 0:
                pass
            else:
                # add price
                Subject.add_price(price_int, price_str)
                HAS_PRICE = True

        # county options
        elif menu_option == options_dict[3]:
            # get county
            county = src.utilities.inputs.InputHelper.county_grabber(all_counties)
            cls()
            if county is None:
                MAIN_LOOP = False
            else:
                # add county
                Subject.add_county(county)

        # special options
        elif menu_option == options_dict[4]:
            # check for special options
            Subject.county.select_special_options()

        # city options
        elif menu_option == options_dict[5]:
            # get all cities
            all_cities = county.get_cities()

            # get city statistics if any
            city = src.utilities.inputs.InputHelper.city_grabber(all_cities)

            cls()

            if city is None:
                pass  # TODO add optional stuff for if city selection is quitted maybe something that allows for option to change counties or continue with only the current county
                MAIN_LOOP = False

            else:
                # add city to subject
                Subject.add_city(city)

                src.utilities.printers.Printer.welcome_city(city.get_city_name())

                city.modify_or_keep()

                cls()

        # reload all counties to default
        elif menu_option == options_dict[99]:
            load = src.utilities.inputs.InputHelper.choice_bool(
                "Are you SURE you want to reload Counties and Cities to default values?"
            )
            if load:
                src.localities.load_all_counties("reload")
                Subject = src.utilities.classes.Property()
                INITAL_RUN = True
                HAS_PRICE = False
                cls()
                src.utilities.printers.Printer.short_liner()
                src.utilities.printers.Printer.print_green("Counties & Cities RELOADED")
                src.utilities.printers.Printer.short_liner()
            else:
                cls()
                src.utilities.printers.Printer.short_liner()
                src.utilities.printers.Printer.print_red(
                    "Counties & Cities NOT reloaded"
                )
                src.utilities.printers.Printer.short_liner()

        # error
        else:
            debugpy.breakpoint()
            src.utilities.printers.Printer.inside_liner(
                "There was an ERROR in main menu selection. :("
            )

    cls()
    # generate statistics
    Subject.generate_statistics()
    # statement maker
    statement = f"Taxes are an estimate based on {Subject.county.get_county_name()} tax calculator with estimated tax rates as follows: Purchase Price {Subject.get_price_str()} {Subject.generate_post_price_statement()} as rounded to the nearest dollar."

    # print goodbye
    src.utilities.printers.Printer.end_program_message()

    # print final statement
    src.utilities.printers.Printer.liner()
    src.utilities.printers.Printer.print_green(statement)
    src.utilities.printers.Printer.liner()


def wait():
    input("press ANY key to Continue")
    cls()


###
main()
###
