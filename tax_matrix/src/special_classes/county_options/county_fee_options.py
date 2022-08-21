"""
    handles waste fees
"""

from . import LogicalWork
from . import cls
from . import Printer
from . import InputHelper
from . import InputTesters


class FeeOptions:
    """
        handles waste options
    """

    #inital runs
    def __init__(self,fee_options_dictionary):
        self.input_dictionary=fee_options_dictionary
        self.dictionary_of_classes=self.initalize_classes()
        self.stats=None

        self.list_of_fee_floats=[]
        self.list_of_fee_strings=[]

        self.list_of_fee_titles=self.get_item_titles()

        self.update_current_fees()
        self.update_stats()

    def initalize_classes(self):
        """
        initalize_classes initalize classes for inididual fees

        Returns:
            list: list of individual fee item classes
        """
        list_of_all_fee_classes = []
        for index in self.input_dictionary:
            list_of_all_fee_classes.append(IndividualFeeItem(self.input_dictionary, index))

        return list_of_all_fee_classes

    ##get items
    def get_item_titles(self):
        """
        retreive_item_titles add titles to list of titles
        """
        list_to_return=[]

        self.update_current_fees()

        for i in self.dictionary_of_classes:
            list_to_return.append(i.get_title())

        return list_to_return

    def get_stats(self):
        """
        get_stats updates and returns statistics

        Returns:
            dict: county stats
        """
        self.update_stats()
        return self.stats

    #update
    def update_current_fees(self):
        """
        update_current_fees updates current fees
        """
        self.list_of_fee_floats = []
        self.list_of_fee_strings = []

        for i in self.dictionary_of_classes:
            self.list_of_fee_floats.append(i.get_current_fee_float())
            self.list_of_fee_strings.append(i.get_current_fee_string())

    def update_stats(self):
        """
        get_stats updates and returns statistics

        Returns:
            dict: county stats
        """
        self.update_current_fees()
        self.stats={}
        for title, fee_float in zip(self.list_of_fee_titles,self.list_of_fee_floats):
            self.stats[title]=fee_float

    #logic
    def fee_info_dict_with_quit_option(self):
        """
        fee_info_dict_with_quit_option generates dict with quit options from available options of fee areas

        Returns:
            dict: dictionary of modifable fee options
        """
        self.update_current_fees()
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
        prints current conditions of fees
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
            list_of_classes,print_dict=self.fee_info_dict_with_quit_option()

            index_of_selection_in_list_of_classes=InputHelper.input_from_dict_get_index(print_dict,"Which Fee District would you like to modify?",list_of_classes)

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
        get_statistic_outputs for special county fees

        Returns:
            list: list of strings containing active statistics
        """
        self.update_current_fees()

        output_list = []

        for title,fee_float,fee_string in zip(self.list_of_fee_titles,self.list_of_fee_floats,self.list_of_fee_strings):
            if fee_float is not None:
                output_list.append(f"{title} Fee: {fee_string}")

        if len(output_list)!=0:
            return output_list
        else:
            return ["No Special County Fees"]

class IndividualFeeItem:
    """
        handles individual fee items
    """

    def __init__(self,fee_options_dictionary,positional_key):
        self.fee_options_dict = fee_options_dictionary
        self.option_inner_dict = fee_options_dictionary[positional_key]
        self.title = list(self.option_inner_dict.keys())[0]

        self.validate_and_set_default_fee()

        self.current_fee = None

    #modify item
    def modify(self):
        """
        modify choose what to modify
        """
        enable = InputHelper.on_or_off_fee(
            self.title,
            self.default_option_fee,
            self.current_fee,
        )

        cls()

        if enable:
            self.current_fee = self.default_option_fee
        else:
            self.current_fee = None
        Printer.liner()
        if self.current_fee is not None:
            current_fee_to_print = f"${self.current_fee:.2f}"
        else:
            current_fee_to_print = "None"
        Printer.print_green(f"{self.title} updated to: {current_fee_to_print}")

    #validation
    def validate_and_set_default_fee(self):
        """
        validate_and_set_default_fee validates fees and sets default fees
        """
        tmp_default_option_fee = (
            self.option_inner_dict[self.title]
            if self.option_inner_dict[self.title] is not None
            else 0
        )

        if tmp_default_option_fee != 0:
            verified_float = InputTesters.verify_float(tmp_default_option_fee)

            self.default_option_fee = verified_float

        else:
            self.default_option_fee = 0

    #get items
    def get_title(self):
        """
        get_title returns title

        Returns:
            str: title
        """
        return self.title

    def get_default_fee_float(self):
        """
        get_default_fee_float returns fee float

        Returns:
            float: fee float
        """
        return self.default_option_fee

    def get_current_fee_float(self):
        """
        get_current_fee_float returns current fee float

        Returns:
            float: current fee float
        """
        return self.current_fee

    def get_current_fee_string(self):
        """
        get_current_fee_string returns current fee str for output

        Returns:
            str: current fee string
        """
        if self.current_fee is not None:
            return f"${self.current_fee:.2f}"
        else:
            return None

    def get_status_str(self):
        """
        get_status_str returns status string

        Returns:
            str: string with current status
        """
        checked_current_fee, checked_default_fee = self.check_fees_for_none()

        return f"{self.title} - Current Fee: {checked_current_fee} | DEFAULT FEE: {checked_default_fee}"

    #print status string
    def print_status_str(self):
        """
        print_status_str
        """
        checked_current_fee, checked_default_fee = self.check_fees_for_none()

        statement = f"{self.title} - Current Fee: {checked_current_fee} | DEFAULT FEE: {checked_default_fee}"

        if checked_current_fee != "None":
            Printer.print_green(statement)
        else:
            Printer.print_red(statement)

    #check fees
    def check_fees_for_none(self):
        """
        check_fees_for_none checks to see if fees are none

        Returns:
            current,default: str with fee or none
        """
        if self.default_option_fee is not None:
            default = f"${self.default_option_fee:.2f}"
        else:
            default = "None"

        if self.current_fee is not None:
            current = f"${self.current_fee:.2f}"
        else:
            current = "None"

        return current, default
