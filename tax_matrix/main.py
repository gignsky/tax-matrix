"""
    Main Function of Tax Matrix to help produce final product
"""

import src

# print a welcome message
src.utilities.printers.Printer.welcome_to_program(
    src.config.CURRENT_VERSION(), src.config.DATE_REVISED()
)

load = src.utilities.inputs.InputHelper.choice_bool("Loud Counties and Cities?")
if load:
    src.localities.load_all_counties()
else:
    pass


"""
    NEED TO REWRITE THIS TO START WORKING WITH NEW FOLDERS YAY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""


def main():
    """
    Main program that will terminate with statement and statistics
    """

    MAIN_LOOP = True  # var to keep program running until stop is requested or neccecary

    # main loop
    while MAIN_LOOP:
        """
        main program loop
        """

        # return subject class object
        Subject = src.utilities.classes.Property()

        # get county list
        county_list = src.utilities.classes.Counties.get_all_counties()

        # get county
        county = src.utilities.inputs.InputHelper.county_grabber(county_list)

        if county is None:
            MAIN_LOOP = False
        else:
            # add county
            Subject.add_county(county)

            # get cities
            cities = county.get_cities()

            # get city statistics if any
            city = src.utilities.inputs.InputHelper.city_grabber(cities)

            if city is None:
                pass  # TODO add optional stuff for if city selection is quitted maybe something that allows for option to change counties or continue with only the current county
                MAIN_LOOP = False
            else:
                src.utilities.printers.Printer.welcome_city(city.get_city_name())
                city.modify_or_keep()

            Subject.select_special_options()

    #         # get price
    #         price_float, price_str = (
    #             156,
    #             "156",
    #         )  # src.utilities.inputs.InputHelper.price_grabber()
    #
    #         # add price
    #         Subject.add_price(price_float, price_str)

    src.utilities.printers.Printer.end_program_message()


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
