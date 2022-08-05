"""
    General logic for entire program
    vscode-fold=2
"""

import debugpy
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
            debugpy.breakpoint()
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
    def check_countywide_only(county_dict):
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

    @staticmethod
    def check_county_services_exist(county_services_list):
        for i in county_services_list:
            key = list(i.keys())[0]
            tmp_dict = i[key]
            inital_rate = tmp_dict["INITAL"]

            if inital_rate is not None:
                return True

        return False

    @staticmethod
    def create_options_dict_from_county_services_list_WITH_quit(county_services_list):
        index = 0
        return_dict = {}
        if index != 0:
            for i in county_services_list:
                title = i.keys()
                inital_rate = title["INITAL"]
                current_rate = title["CURRENT"]

                if inital_rate is not None:
                    statement = f"{title} Current Rate: {current_rate} | Default Rate: {inital_rate}"
                    return_dict[index] = {
                        statement: {title: {current_rate: inital_rate}}
                    }
                    index += 1
        else:
            return_dict[index] = "Quit"

        if len(return_dict) == 1:
            return None
        else:
            return return_dict

    @staticmethod
    def create_options_dict_from_county_services_list_NO_quit(county_services_list):
        return_list = []
        for i in county_services_list:
            title = i.keys()
            inital_rate = title["INITAL"]
            current_rate = title["CURRENT"]

            if inital_rate is not None:
                return_list.append(
                    f"{title} Current Rate: {current_rate} | Default Rate: {inital_rate}"
                )

        return return_list
