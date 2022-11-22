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
    subject = src.general_classes.property_class.Property()

    # get county list
    all_counties = src.general_classes.Counties.get_all_counties()

    # set inital values
    main_loop_running = (
        True  # var to keep program running until stop is requested or necessary
    )

    inital_run_status = (
        True  # var to set the inital run to run through all available options
    )

    subject_has_price = (
        False  # var sets has price var to false to indicate a price has not been loaded
    )

    # dict of available options
    options_dict = {
        0: "Quit Program & Output Statement",
        1: "Print Statistics & Statement\n...",
        2: "Modify Price\n...",
        3: "Modify County\n...",
        4: "Modify Residential Status (Primary Residence / Investment)\n...",
        5: "Modify Countywide Police, Fire, and/or EMS rates",
        6: "Modify County Special Options - Fees & Rates (or Sales Tax Credit Factors LANCASTER ONLY)\n...",
        7: "Modify City and/or City Options\n...",
        99: "Reload Counties to Default Values",
    }

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
            inital_run_status, menu_option = inital_run_stack(
                inital_run_status, options_dict, subject
            )

        # "Quit Program & Output Statement"
        if menu_option == options_dict[0]:
            main_loop_running = False

        # "Print Statistics & statement"
        elif menu_option == options_dict[1]:
            cls()
            subject.print_current_stats()

            src.utilities.Printer.print_cyan("...\n Statement to output:")
            statement = generate_statement(subject)
            src.utilities.Printer.print_green(statement)

            src.utilities.LogicalWork.wait()

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

                if subject.county.get_state() != "SC":
                    subject.add_residency("RESET")

                cls()

        # Modify Residency for SC ONLY
        elif menu_option == options_dict[4]:
            src.utilities.inputs.InputHelper.grab_residency(subject)
            cls()
        # "Modify Countywide Police, Fire, and/or EMS rates"
        elif menu_option == options_dict[5]:
            subject.county.select_countywide_services()

        # "Modify County Special Options"
        elif menu_option == options_dict[6]:
            # check for special options
            subject.county.modify_special_options()

        # "Modify City and/or City Options"
        elif menu_option == options_dict[7]:
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
                    subject.reset_city()

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
                subject = src.general_classes.Property()
                inital_run_status = True
                subject_has_price = False
                subject.add_residency("RESET")
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
    # statement making
    statement = generate_statement(subject)

    # print goodbye
    src.utilities.printers.Printer.end_program_message()

    # print final statement
    src.utilities.printers.Printer.liner()
    src.utilities.printers.Printer.print_green(statement)
    src.utilities.printers.Printer.liner()

    src.utilities.LogicalWork.wait()


def generate_statement(subject):
    """
    generate_statement generates final statement for output

    Args:
        subject (class): class containing all subject information

    Returns:
        str: final output statement
    """

    # generate statistics
    subject.generate_statistics()

    statement = f"Taxes are an estimate based on {subject.county.get_county_name()} tax calculator with estimated tax rates as follows: Purchase Price {subject.get_price_str()} / 100 = {subject.get_price_str_divided_by_100()} {subject.generate_post_price_statement()} as rounded to the nearest dollar."

    return statement


def inital_run_stack(inital_run_status, options_dict, subject_class):
    """
    inital_run_stack runs menu selection for inital run of script

    Args:
        inital_run_status (bool): true/false
        options_dict (dict): dictionary of options

    Returns:
        value_from_dict: returns value from options dict and new inital_run_status
    """

    if inital_run_status is True:
        menu_option = options_dict[2]
        inital_run_status = "Get Price then County"
    elif inital_run_status == "Get Price then County":
        menu_option = options_dict[3]
        inital_run_status = "sc_residency_check"
    elif inital_run_status == "sc_residency_check":
        if subject_class.county.get_state() == "SC":
            menu_option = options_dict[4]
            inital_run_status = "check special district options"
        else:
            menu_option = options_dict[5]
            inital_run_status = "Modify Countywide Fire, Police, & EMS"
    elif inital_run_status == "check special district options":
        menu_option = options_dict[5]
        inital_run_status = "Modify Countywide Fire, Police, & EMS"
    elif inital_run_status == "Modify Countywide Fire, Police, & EMS":
        menu_option = options_dict[6]
        inital_run_status = "Do you want a city?"
    elif inital_run_status == "Do you want a city?":
        menu_option = options_dict[7]
        inital_run_status = "continue onwards"
    else:
        menu_option = options_dict[1]  # print stats before continuing
        inital_run_status = False
    return inital_run_status, menu_option


###
main()
###
