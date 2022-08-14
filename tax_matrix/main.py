"""
    Main Function of Tax Matrix to help produce final product
"""

import src
from src import cls


# print a welcome message
src.utilities.printers.Printer.welcome_to_program(
    src.config.current_version(), src.config.date_revised()
)

src.localities.load_all_counties("inital")


def main():
    """
    Main program that will terminate with statement and statistics
    """

    # return subject class object
    subject = src.classes.propertyClass.Property()

    # get county list
    all_counties = src.classes.Counties.get_all_counties()

    # dict of avalable options
    options_dict = {
        0: "Quit Program & Output Statement",
        1: "Print Statisticts",
        2: "Modify Price",
        3: "Modify County",
        4: "TEMPORARY STRING\n...",
        5: "Modify Countywide Police, Fire, and/or EMS rates",
        6: "Modify City and/or City Options\n...",
        99: "Reload Counties to Default Values",
    }

    main_loop_running = (
        True  # var to keep program running until stop is requested or neccecary
    )
    inital_run_status = (
        True  # var to set the inital run to run through all avaliable options
    )
    subject_has_price = (
        False  # var sets has price var to false to indicate a price has not been loaded
    )

    # main program loop
    while main_loop_running:

        # test if inital run otherwise grab menu option
        if not inital_run_status:
            src.utilities.printers.Printer.welcome_county(
                subject.county.get_county_name()
            )
            # select main menu options
            menu_option = src.utilities.inputs.InputHelper.main_menu_options(
                options_dict
            )
            cls()

        else:
            if inital_run_status is True:
                menu_option = options_dict[2]
                inital_run_status = "Get Price then County"
            elif inital_run_status == "Get Price then County":
                menu_option = options_dict[3]
                inital_run_status = "check special district options"
            elif inital_run_status == "check special district options":
                menu_option = options_dict[4]
                inital_run_status = "Modify Countywide Fire, Police, & EMS"
            elif inital_run_status == "Modify Countywide Fire, Police, & EMS":
                menu_option = options_dict[5]
                inital_run_status = "Do you want a city?"
            elif inital_run_status == "Do you want a city?":
                menu_option = options_dict[6]
                inital_run_status = "continue onwards"
            else:
                menu_option = options_dict[1]  # print stats before continuing
                inital_run_status = False

        # "Quit Program & Output Statement"
        if menu_option == options_dict[0]:
            main_loop_running = False

        # "Print Statisticts"
        elif menu_option == options_dict[1]:
            cls()
            subject.print_current_stats()
            wait()

        # "Modify Price"
        elif menu_option == options_dict[2]:
            if subject_has_price:
                src.utilities.printers.Printer.short_liner()
                src.utilities.printers.Printer.print_yellow(
                    f"Current Price: {subject.get_price_str()}"
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
                cls()
                subject.add_price(price_int, price_str)
                subject_has_price = True

        # "Modify County"
        elif menu_option == options_dict[3]:
            # get county
            county = src.utilities.inputs.InputHelper.county_grabber(all_counties)
            cls()
            if county is None:
                main_loop_running = False
            else:
                # add county
                subject.add_county(county)

                cls()

                options_dict[
                    4
                ] = f"Modify County Special Options - {subject.county.get_special_options_title()}\n..."

        # "Modify County Special Options"
        elif menu_option == options_dict[4]:
            # check for special options
            subject.county.select_special_options()

        # "Modify Countywide Police, Fire, and/or EMS rates"
        elif menu_option == options_dict[5]:
            subject.county.select_county_services()

        # "Modify City and/or City Options"
        elif menu_option == options_dict[6]:
            if inital_run_status == "continue onwards":
                pick_city_bool = src.utilities.inputs.InputHelper.choice_bool(
                    "Do you want to select a city at this time?"
                )
            else:
                pick_city_bool = True

            if pick_city_bool:
                # get all cities
                all_cities = county.get_cities()

                # get city statistics if any
                city = src.utilities.inputs.InputHelper.city_grabber(all_cities)

                cls()

                if city is None:
                    pass  # TODO add optional stuff for if city selection is quitted maybe something that allows for option to change counties or continue with only the current county
                    main_loop_running = False

                else:
                    # add city to subject
                    subject.add_city(city)

                    src.utilities.printers.Printer.welcome_city(city.get_city_name())

                    city.modify_or_keep()

                    cls()

        # "Reload Counties to Default Values"
        elif menu_option == options_dict[99]:
            load = src.utilities.inputs.InputHelper.choice_bool(
                "Are you SURE you want to reload Counties and Cities to default values?"
            )
            if load:
                src.localities.load_all_counties("reload")
                subject = src.classes.Property()
                inital_run_status = True
                subject_has_price = False
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
            src.debugpy.breakpoint()
            src.utilities.printers.Printer.inside_liner(
                "There was an ERROR in main menu selection. :("
            )

    cls()
    # generate statistics
    subject.generate_statistics()
    # statement maker
    statement = f"Taxes are an estimate based on {subject.county.get_county_name()} tax calculator with estimated tax rates as follows: Purchase Price {subject.get_price_str()} {subject.generate_post_price_statement()} as rounded to the nearest dollar."

    # print goodbye
    src.utilities.printers.Printer.end_program_message()

    # print final statement
    src.utilities.printers.Printer.liner()
    src.utilities.printers.Printer.print_green(statement)
    src.utilities.printers.Printer.liner()


def wait():
    """
    wait will wait for any input to continue onwards
    """
    input("press ANY key to Continue\n...\n")
    cls()


###
main()
###
