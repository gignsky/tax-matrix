"""
    General logic for entire program
"""

from . import debugpy
from . import cls

# from . import counties


class LogicalWork:
    """
    General logical functions for all of the program, note all items in class are "Static Methods"
    """

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

        index_value = 1
        if city_or_county == "COUNTY":
            for i in list_to_dict:
                dictionary[index_value] = i
                index_value += 1
        elif city_or_county == "CITY":
            for i in list_to_dict:
                var_from_i = list_to_dict[i]
                dictionary[index_value] = var_from_i
                index_value += 1

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

        index_value = 1
        if city_or_county == "COUNTY":
            dict_with_names[0] = "Quit Program"
            for i in class_dict:
                name = i.get_county_name()
                dict_with_names[index_value] = name
                index_value += 1
        elif city_or_county == "CITY":
            dict_with_names[0] = "None of the below"
            for i in class_dict:
                variable_from_i = class_dict[i]
                name = variable_from_i.get_city_name()
                dict_with_names[index_value] = name
                index_value += 1

        return dict_with_names

    @staticmethod
    def no_index_dict_to_two_lists(working_dict):
        """
        no_index_dict_to_two_lists generates two lists from a dictionary with no index values

        i.e. {key:value,key1:value1,...,keyN:valueN}

        Args:
            working_dict (dict): dict to work on must NOT contain index

        Returns:
            list1: list of keys from dict
            list2: list of values from dict
        """
        list1 = []
        list2 = []

        if working_dict is not None:
            for i in working_dict:
                list1.append(i)
                list2.append(working_dict[i])

        if list1 is not None and list2 is not None:
            return list1, list2
        else:
            return None

    @staticmethod
    def with_index_dict_to_two_lists(working_dict):
        """
        with_index_dict_to_two_lists generate two lists from a dictionary with index values

        ***Note:  a check that the dict is not None is also preformed this will return a None value in BOTH lists

        Args:
            working_dict (dict): dictionary to mod, MUST include index values

        Returns:
            list1: list of keys from inner dicts while stripping key values
            list2: list of values from inner dicts while stripping key values
        """
        list1 = []
        list2 = []

        if working_dict is not None:
            for i in working_dict:
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
        """
        check_countywide_only checks if county only has a countywide rate after options selected

        Args:
            county_dict (dict): county_services_dict

        Returns:
            bool: True if only countywide rate; False if NOT countywide only rate
        """
        _, county_values = LogicalWork.no_index_dict_to_two_lists(county_dict)

        try:
            county_second_value = county_values[1]
        except KeyError:
            county_second_value = None

        except IndexError:
            county_second_value = None

        if county_second_value is not None:
            return False  # returns false if second value could be found or city values are found
        else:
            return True

    @staticmethod
    def check_city_exists(city_dict):
        """
        check_city_exists checks to see if a city exists in selection

        Args:
            city_dict (dict): city services dict

        Returns:
            bool: True / False
        """
        if city_dict is not None:
            _, city_values = LogicalWork.no_index_dict_to_two_lists(city_dict)
        else:
            return False

        try:
            first_city_value = city_values[0]
        except KeyError:
            return False

        first_city_value_key = list(first_city_value)[0]

        if first_city_value[first_city_value_key] is None:
            return False
        else:
            return True

    @staticmethod
    def check_county_services_exist(county_services_list):
        """
        check_county_services_exist checks if countyservices are present by checking the "INITAL" value against None

        Args:
            county_services_list (list): list of county services

        Returns:
            bool: True / False
        """
        for i in county_services_list:
            key = list(i.keys())[0]
            tmp_dict = i[key]
            inital_rate = tmp_dict["INITAL"]

            if inital_rate is not None:
                return True

        return False

    # TODO see if ever referenced
    # old might be unused
    #     @staticmethod
    #     def create_options_dict_from_county_services_list_WITH_quit(county_services_list):
    #         index = 0
    #         return_dict = {}
    #         if index != 0:
    #             for i in county_services_list:
    #                 title = i.keys()
    #                 inital_rate = title["INITAL"]
    #                 current_rate = title["CURRENT"]
    #
    #                 if inital_rate is not None:
    #                     statement = f"{title} Current Rate: {current_rate} | Default Rate: {inital_rate}"
    #                     return_dict[index] = {
    #                         statement: {title: {current_rate: inital_rate}}
    #                     }
    #                     index += 1
    #         else:
    #             return_dict[index] = "Quit"
    #
    #         if len(return_dict) == 1:
    #             return None
    #         else:
    #             return return_dict

    @staticmethod
    def create_options_dict_from_county_services_list_with_quit(county_services_list):
        """
        create_options_dict_from_county_services_list_WITH_quit creates dict for input_from_dict with a quit option from a list of county services, intended to be used with police/fire rates for each county I think

        Args:
            county_services_list (list): list of county services

        Returns:
            dict: will return dict with options if county services exist; else, will return a value of 'None'
        """
        index = 0
        return_dict = {}
        running = True
        while running:
            if index != 0:
                for i in county_services_list:
                    title = list(i.keys())[0]
                    inner_dict = i[title]
                    inital_rate = inner_dict["INITAL"]

                    if inital_rate is not None:
                        return_dict[index] = i
                        index += 1

                running = False
            else:
                return_dict[index] = "Quit"
                index += 1

        if len(return_dict) == 1:
            return None
        else:
            return return_dict

    @staticmethod
    def create_options_dict_from_county_services_list_no_quit(county_services_list):
        """
        create_options_dict_from_county_services_list_NO_quit creates dict with NO quit option from a list of county services, intended to be used with police/fire rates for each county I think

        I think this is used for generating a pretty output statement to be used with print_dict

        Args:
            county_services_list (list): list of county services

        Returns:
            dict: will return dict with options
        """
        return_list = []
        for i in county_services_list:
            title = list(i.keys())[0]
            inner_dict = i[title]
            inital_rate = inner_dict["INITAL"]
            current_rate = inner_dict["CURRENT"]

            if inital_rate is not None:
                return_list.append(
                    f"{title} Current Rate: {current_rate} | Default Rate: {inital_rate}"
                )

        return return_list

    @staticmethod
    def wait():
        """
        wait will wait for any input to continue onwards
        """
        input("press ANY key to Continue\n...\n")
        cls()

    @staticmethod
    def sc_county_wide_rate_musher(
        overall_title, overall_rate, list_of_inner_titles, list_of_inner_rates
    ):

        list_of_statements_to_mush = ()

        for title, rate in zip(list_of_inner_titles, list_of_inner_rates):
            list_of_statements_to_mush.append(f"({rate} - {title})")

        num_of_statements = len(list_of_statements_to_mush)
        statement_to_mush = ""

        for statement in list_of_statements_to_mush:
            if num_of_statements == 1:
                statement_to_mush = f"{statement})"
            else:
                statement_to_mush = f"{statement_to_mush} + {statement}"

            num_of_statements += 1

        overall_statement_for_county = (
            f"[{overall_rate} - {overall_title} ({statement_to_mush})]"
        )

        return overall_statement_for_county
