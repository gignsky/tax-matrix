"""
    handles county special items
"""

from . import cls
from . import InputHelper
from . import Printer
from . import FeeOptions
from . import RateOptions

class SpecialItems:
    """
        handles county special items
    """

    def __init__(self,fee_options_dictionary,rate_districts_dictionary):
        self.fee_dictionary=fee_options_dictionary
        self.rate_dictionary=rate_districts_dictionary

        #initalize classes
        self.fee_class=None
        self.rate_class=None
        self.initalize_fees()
        self.initalize_rates()

        #statistics
        self.fee_stats=None
        self.rate_stats=None

    #initalize stats
    def initalize_fees(self):
        """
        initalize_waste
        """
        if self.fee_dictionary is not None:
            self.fee_class=FeeOptions(self.fee_dictionary)
        else:
            self.fee_class=None

    def initalize_rates(self):
        """
        initalize_fire
        """
        if self.rate_dictionary is not None:
            self.rate_class=RateOptions(self.rate_dictionary)
        else:
            self.rate_class=None

    #modify
    def general_modify_decisions(self):
        """
        general_modify_decisions determine if any options are modifyable and allow user to modify if they appear
        """

        available_items_to_modify=self.determine_modable_items()

        if len(available_items_to_modify) !=0:
            looper=True
            while looper:
                user_input=InputHelper.choice_bool(f"Would you like to modify Special {available_items_to_modify}?")

                if not user_input:
                    looper=False
                    cls()
                else:
                    for i in available_items_to_modify:
                        cls()
                        Printer.liner()
                        user_input=None
                        if i == "FEES":
                            self.fee_class.print_current_conditions()
                            user_input=InputHelper.choice_bool("Would you like to Modify Fees?")

                            if user_input:
                                self.mod_fee()

                        elif i == "RATES":
                            self.rate_class.print_current_conditions()
                            user_input=InputHelper.choice_bool("Would you like to Modify Special Rates?")

                            if user_input:
                                self.mod_rate()

            cls()

        else:
            Printer.liner()
            Printer.print_red("No Special Options Available")
            Printer.liner()

    def mod_fee(self):
        """
        mod_waste
        """
        self.fee_stats=self.fee_class.modify()

    def mod_rate(self):
        """
        mod_fire
        """
        self.rate_stats=self.rate_class.modify()

    #get stats
    def get_stats(self):
        """
        get_stats returns stats for fees and rates if they exist
        """
        stats_to_return=[]

        if self.fee_stats is not None:
            stats_to_return.append(self.fee_stats)
        else:
            stats_to_return.append("No Fee Stats Available")

        if self.rate_stats is not None:
            stats_to_return.append(self.rate_stats)
        else:
            stats_to_return.append("No Rate Stats Available")

        return stats_to_return

    #logic
    def determine_modable_items(self):
        """
        determine_modable_items

        Returns:
            list: list of fire and waste that can be modified
        """
        available_to_modify=[]
        if self.fee_dictionary is not None:
            available_to_modify.append("FEES")
        if self.rate_dictionary is not None:
            available_to_modify.append("RATES")

        return available_to_modify

    #all outputs
    ##outputs for stat output
    def generate_statistics_statement(self):
        """
        generate_statistics_statement for rates and fees inside county

        Returns:
            list: list of fees and rates statistics strings for only active fees and rates
        """
        if self.fee_class is not None:
            fee_statement=self.fee_class.get_statistic_outputs()
        else:
            fee_statement=None

        if self.rate_class is not None:
            rate_statement=self.rate_class.get_statistic_outputs()
        else:
            rate_statement=None

        return [fee_statement,rate_statement]

    ##outputs for statement
    def generate_output_statement_statement(self):
        """
        generate_output_statement_statement for final statement

        Returns:
            dict: dict containing either active stats or a value of None
        """
        dict_to_return={}
        list_of_stats=self.get_stats()

        for i in list_of_stats:
            if type(i) is dict:
                dict_to_return.update(i)

        if len(dict_to_return) !=0:
            return dict_to_return

        else:
            return None
