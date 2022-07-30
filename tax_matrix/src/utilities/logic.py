"""
    General logic for entire program
"""

from . import printers

# from . import counties


class LogicalWork:
    @staticmethod
    def substatement_maker(rate, location):
        """
        main substatement generator

        Args:
            rate (float): float of rate that needs to be calculated
            location (str): descriptor of additional rate

        Returns:
            str: substatement - final
        """
        return f" + ({rate} - {location})"

    @staticmethod
    def convert_list_to_dict(city_or_county, list_to_dict):
        """
        convert_list_to_dict converts dictionary to a list using index values to allow for selection

        Args:
            city_or_county (str): specifies if this is for a city or county dictionary
            list_to_dict (list): list of county or cities to be converted to a dictionary

        Returns:
            _type_: _description_
        """
        dictionary = {}

        INDEX_VALUE = 1
        if city_or_county == "COUNTY":
            for i in list_to_dict:
                dictionary[INDEX_VALUE] = i
                INDEX_VALUE += 1
        elif city_or_county == "CITY":
            for i in list_to_dict:
                var_from_i = list_to_dict[i]
                dictionary[INDEX_VALUE] = var_from_i
                INDEX_VALUE += 1

        else:
            print("ERROR WITH LiST IN LOGIC.py")

        return dictionary

    @staticmethod
    def convert_class_dict_to_dict_with_names(city_or_county, class_dict):
        """
        convert_class_dict_to_dict_with_names addes names next to index values and a 0 value for the selection of ability to either quit or select no city

        Args:
            city_or_county (str): city or county in all caps to specify which version to use
            class_dict (dicitonary): dictionary of classes for selection

        Returns:
            dict: dictionary of indexes and names
        """
        dict_with_names = {}

        INDEX_VALUE = 1
        if city_or_county == "COUNTY":
            dict_with_names[0] = "Quit Program"
            for i in class_dict:
                name = i.get_county_name()
                dict_with_names[INDEX_VALUE] = name
                INDEX_VALUE += 1
        elif city_or_county == "CITY":
            dict_with_names[0] = "None of the below"
            for i in class_dict:
                variable_from_i = class_dict[i]
                name = variable_from_i.get_city_name()
                dict_with_names[INDEX_VALUE] = name
                INDEX_VALUE += 1

        return dict_with_names

    @staticmethod
    def no_index_dict_to_two_lists(dict):
        list1 = []
        list2 = []

        for i in dict:
            list1.append(i)
            list2.append(dict[i])

        return list1, list2

    @staticmethod
    def with_index_dict_to_two_lists(dict):
        list1 = []
        list2 = []

        if dict is not None:
            for i in dict:
                if i is not None:
                    key = list(i.keys())
                    value = i[key[0]]
                    list1.append(key)
                    list2.append(value)
        else:
            list1 = None
            list2 = None

        return list1, list2

    @staticmethod
    def check_county_only(county_dict):
        _, county_values = LogicalWork.no_index_dict_to_two_lists(county_dict)

        try:
            county_second_value = county_values[1]
        except:
            county_second_value = None

        if county_second_value is not None:
            return False  # returns false if second value could be found or city values are found
        else:
            return True

    @staticmethod
    def check_city_exists(city_dict):
        if city_dict is not None:
            _, city_values = LogicalWork.no_index_dict_to_two_lists(city_dict)
        else:
            return False

        try:
            first_city_value = city_values[0]
        except:
            return False

        first_city_value_key = list(first_city_value)[0]

        if first_city_value[first_city_value_key] is None:
            return False
        else:
            return True


#     @staticmethod
#     def county_controller(price_float, price_pretty, county_name, county_state):
#         """
#         POSSIBLY DEPRECIATED _THINK ABOUT DELETING!!!
#         county controller should do something about controlling what county is selected might be DEPRECITATED but copied for simplicity
#         """
#         printers.Printer.welcome_county(county_name, county_state, price_pretty)
#
#         # convert string to function
#         if county_state == "SC":
#             # strip ', ' from SC titles
#             fixed_county_name = county_name.replace(", ", "")
#         else:
#             fixed_county_name = county_name
#
#         # convert to lower case
#         fixed_county_name = fixed_county_name.lower()
#
#         # convert string to callable function
#         functional_str = getattr(datasheets, fixed_county_name)
#
#         # call county page
#         statement, stats = functional_str(price_float, price_pretty)
#
#     @staticmethod
#     def county_finder():
#         """
#         MIGHT BE DEPRECIATED_THINK ABOUT REVISING AND OR DELETING!!!!!!
#         find county that subject is located in
#
#         Returns:
#             str,int,str: name of county, index key of county in counties dict, & state of county in capital str format
#         """
#         counties_dict = counties.counties_dict()
#
#         loop_on = (
#             True  # set var too keep loop going to ensure that entered var is valid
#         )
#
#         while loop_on:
#             # prompt for county selection
#             prompt = "Please Select County in which the Subject Property Resides via ENTERING the ASSOCIATED NUMBER: "
#
#             # grab inputted value from list of counties
#             inputted_value = input_from_dict(counties_dict, prompt)
#
#             # verify that inputted value is an int
#             county_key = verify_int(inputted_value)
#
#             if county_key != None:
#                 try:
#                     # set county name to associated name
#                     county_name = counties_dict[county_key]
#
#                     # determine county state
#                     if "sc" in county_name:
#                         county_state = "SC"
#                     else:
#                         county_state = "NC"
#
#                     loop_on = False  # end loop and allow for return
#                 except:
#                     print(
#                         f"An Error has occured, most likely the inputted value of '{county_key}' is outside the range of avaliable counties... please try again"
#                     )
#
#         # return final values to main
#         return county_name, county_key, county_state
