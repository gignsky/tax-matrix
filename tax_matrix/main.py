"""
    Main Function of Tax Matrix to help produce final product
"""

import src

# print a welcome message
src.utilities.printers.Printer.welcome_to_program(
    src.config.CURRENT_VERSION(), src.config.DATE_REVISED()
)

src.localities.load_all_counties("inital")


"""
    NEED TO REWRITE THIS TO START WORKING WITH NEW FOLDERS YAY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""


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
        1: "Reload Counties to Default Values",
        2: "Modify Price",
        3: "Modify County",
        4: "Modify County Special Options",
        5: "Modify City and/or City Options",
    }

    MAIN_LOOP = True  # var to keep program running until stop is requested or neccecary
    INITAL_RUN = True  # var to set the inital run to run through all avaliable options

    # main loop
    while MAIN_LOOP:
        """
        main program loop
        """

        # test if inital run otherwise grab menu option
        if not INITAL_RUN:
            # print current statistics
            Subject.print_current_stats()

            # select main menu options
            menu_option = src.utilities.inputs.InputHelper.main_menu_options(
                options_dict
            )
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

        # reload all counties to default
        elif menu_option == options_dict[1]:
            load = src.utilities.inputs.InputHelper.choice_bool(
                "Are you SURE you want to reload Counties and Cities to default values?"
            )
            if load:
                src.localities.load_all_counties("reload")
            else:
                pass

        # price options
        elif menu_option == options_dict[2]:
            # get price
            price_int, price_str = (
                100000,
                "$100,000",
            )  # src.utilities.inputs.InputHelper.price_grabber()

            # add price
            Subject.add_price(price_int, price_str)

        # county options
        elif menu_option == options_dict[3]:
            # get county
            county = src.utilities.inputs.InputHelper.county_grabber(all_counties)
            if county is None:
                MAIN_LOOP = False
            else:
                # add county
                Subject.add_county(county)

        # special options
        elif menu_option == options_dict[4]:
            # check for special options
            Subject.select_special_options()

        # city options
        elif menu_option == options_dict[5]:
            # get all cities
            all_cities = county.get_cities()

            # get city statistics if any
            city = src.utilities.inputs.InputHelper.city_grabber(all_cities)

            if city is None:
                pass  # TODO add optional stuff for if city selection is quitted maybe something that allows for option to change counties or continue with only the current county
                MAIN_LOOP = False
            else:
                src.utilities.printers.Printer.welcome_city(city.get_city_name())
                city.modify_or_keep()

            # add city to subject
            Subject.add_city(city)

        # error
        else:
            src.utilities.printers.Printer.inside_liner(
                "There was an ERROR in main menu selection. :("
            )

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


# def main():
#     """
#     Main program that will terminate with statement and statistics
#     """
#     program_loop = (
#         True  # var to keep program running until stop is requested or neccecary
#     )
#
#     # main program loop that will end when program is quitted or reaches a final output
#     while program_loop:
#         """
#         Run main program
#         """
#         # print a welcome
#         src.utilities.printers.welcome(
#             src.config.CURRENT_VERSION(), src.config.DATE_REVISED()
#         )
#
#         (
#             price_float,
#             price_pretty,
#         ) = src.utilities.inputs.price_grabber()  # get price of home
#
#         county_loop = (
#             True  # var to keep county loop running until stop is requested or neccecary
#         )
#
#         # county loop that allows for jumping back and forth between counties
#         while county_loop:
#             county_name, county_id, county_state = src.utilities.logic.county_finder()
#             statement, stats = src.utilities.logic.county_controller(
#                 price_float, price_pretty, county_name, county_state
#             )
#
#             if statement == None and stats == None:
#                 county_loop, program_loop = False
#                 print("Program EXITED...")
#                 break
#
#         if statement == None:
#             break


main()
