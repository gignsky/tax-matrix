"""
    handles county fire services/districts
"""

from . import cls
from . import InputHelper
from . import InputTesters
from . import Printer
from . import LogicalWork

class RateOptions:
    """
        handles rate based services/districts
    """

    #initalize
    def __init__(self,rate_options_dictionary):
        self.stats=None

        self.input_dictionary=rate_options_dictionary
        self.dictionary_of_classes=self.initalize_classes()

        self.list_of_rate_floats=[]
        self.list_of_rate_strings=[]

        self.list_of_titles=self.get_item_titles()

        self.update_current_rates()
        self.update_stats()

    def initalize_classes(self):
        """
        initalize_classes initalize classes for inididual rates

        Returns:
            list: list of individual rate item classes
        """
        list_of_all_rate_classes = []

        for index in self.input_dictionary:
            list_of_all_rate_classes.append(IndividualRateOptions(self.input_dictionary, index))

        return list_of_all_rate_classes

    #get items
    def get_item_titles(self):
        """
        initalize_classes initalize titles for inididual rates

        Returns:
            list: list of individual item titles
        """
        list_of_titles=[]

        # self.update_current_rates()

        for i in self.dictionary_of_classes:
            list_of_titles.append(i.get_title())

        return list_of_titles

    def get_stats(self):
        """
        get_stats updates and returns statistics

        Returns:
            dict: county stats
        """
        self.update_stats()
        return self.stats

    #update
    def update_current_rates(self):
        """
        update_current_rates update current default rates
        """

        self.list_of_rate_floats=[]
        self.list_of_rate_strings=[]

        for i in self.dictionary_of_classes:
            self.list_of_rate_strings.append(i.get_current_rate_string())
            self.list_of_rate_floats.append(i.get_current_rate_float())

    def update_stats(self):
        """
        get_stats updates and returns statistics

        Returns:
            dict: county stats
        """

        self.update_current_rates()
        self.stats={}
        for title, rate_float in zip(self.list_of_titles,self.list_of_rate_floats):
            self.stats[title]=rate_float

    #logic
    def rate_info_dict_with_quit_option(self):
        """
        fire_info_dict_with_quit_option generates dict with quit options from available options of fire areas

        Returns:
            dict: dictionary of modifable fire options
        """

        self.update_current_rates()
        return_dict={0:"Quit"}
        index_value=1
        list_of_classes=["Quit"]
        for i in self.dictionary_of_classes:
            list_of_classes.append(i)
            return_dict[index_value]=i.get_status_str()
            index_value+=1

        return list_of_classes,return_dict

    #print current stats
    def print_current_conditions(self):
        """
        prints current conditions of rates
        """
        for i in self.dictionary_of_classes:
            i.print_status_str()

    #modify
    def modify(self):
        """
        modify helps to modify individual item within all options
        """
        looping=True

        while looping:
            list_of_classes,print_dict=self.rate_info_dict_with_quit_option()

            index_of_selection_in_list_of_classes=InputHelper.input_from_dict_get_index(print_dict,"Which rate based district would you like to modify?",list_of_classes)

            if index_of_selection_in_list_of_classes == "Quit":
                looping=False
                cls()
                self.print_current_conditions()
                LogicalWork.wait()

            else:
                index_of_selection_in_list_of_classes.modify()

        self.update_stats()
        return self.stats

    #outputs
    def get_statistic_outputs(self):
        """
        get_statistic_outputs for special county rates

        Returns:
            list: list of strings containing active statistics
        """
        self.update_current_rates()

        output_list = []

        for title,rate_float,rate_string in zip(self.list_of_titles,self.list_of_rate_floats,self.list_of_rate_strings):
            if rate_float is not None:
                output_list.append(f"{title} Rate: {rate_string}")

        if len(output_list)!=0:
            return output_list
        else:
            return ["No Special County Rates"]

class IndividualRateOptions:
    """
        handles individual rate based services/districts
    """

    #initalize
    def __init__(self,rate_options_dictionary,positional_key):
        self.rate_options_dictionary = rate_options_dictionary
        self.option_inner_dict = rate_options_dictionary[positional_key]
        self.title = list(self.option_inner_dict.keys())[0]

        self.default_option_rate=None

        self.validate_and_set_default_rate()

        self.current_rate = None

    #modify
    def modify(self):
        """
        modify choose what to modify
        """
        enable = InputHelper.on_or_off_rate(
            self.title,
            self.default_option_rate,
            self.current_rate,
        )

        cls()

        if enable:
            self.current_rate = self.default_option_rate
        else:
            self.current_rate = None
        Printer.liner()
        if self.current_rate is not None:
            current_rate_to_print = f"{self.current_rate:.6g}"
        else:
            current_rate_to_print = "None"
        Printer.print_green(f"{self.title} updated to: {current_rate_to_print}")

    #validation
    def validate_and_set_default_rate(self):
        """
        validate_and_set_default_rate validates rates and sets default rates
        """
        tmp_default_option_rate = (
            self.option_inner_dict[self.title]
            if self.option_inner_dict[self.title] is not None
            else 0
        )

        if tmp_default_option_rate != 0:
            verified_float = InputTesters.verify_float(tmp_default_option_rate)

            self.default_option_rate = verified_float

        else:
            self.default_option_rate = 0

    #get items
    def get_title(self):
        """
        get_title returns title

        Returns:
            str: title
        """
        return self.title

    def get_default_rate_float(self):
        """
        get_default_rate_float returns rate float

        Returns:
            float: rate float
        """
        return self.default_option_rate

    def get_current_rate_float(self):
        """
        get_current_rate_float

        Returns:
            float: current rate float
        """
        return self.current_rate

    def get_current_rate_string(self):
        """
        get_current_rate_string

        Returns:
            str: str with current rate to .6g
        """
        if self.current_rate is not None:
            return f"{self.current_rate:.6g}"
        else:
            return None

    def get_status_str(self):
        """
        get_status_str returns status string

        Returns:
            str: string with current status
        """
        checked_current_rate, checked_default_rate = self.check_rates_for_none()

        return f"{self.title} - Current Rate: {checked_current_rate} | DEFAULT RATE: {checked_default_rate}"

    #print status string
    def print_status_str(self):
        """
        print_status_str
        """
        checked_current_rate, checked_default_rate = self.check_rates_for_none()

        statement = f"{self.title} - Current Rate: {checked_current_rate} | DEFAULT FEE: {checked_default_rate}"

        if checked_current_rate != "None":
            Printer.print_green(statement)
        else:
            Printer.print_red(statement)


    #check rates
    def check_rates_for_none(self):
        """
        check_rates_for_none checks to see if rates are none

        Returns:
            current,default: str with rate or none
        """
        if self.default_option_rate is not None:
            default = f"{self.default_option_rate:.6g}"
        else:
            default = "None"

        if self.current_rate is not None:
            current = f"{self.current_rate:.6g}"
        else:
            current = "None"

        return current, default
