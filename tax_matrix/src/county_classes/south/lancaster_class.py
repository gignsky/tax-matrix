"""
    generic lancaster county class
"""

# from . import debugpy
from . import InputHelper
from . import Printer
from . import cls
from . import general_classes

# TODO Integrate residency with statement


class LancasterCo(general_classes.County):
    """
    LancasterCo special handler

    Args:
        general_classes (class): General County Class
    """

    def __init__(
        self,
        county_name,
        county_state,
        county_wide_rate_title,
        county_wide_rate,
        county_wide_police_title,
        county_wide_police_rate,
        county_wide_fire_title,
        county_wide_fire_rate,
        county_wide_ems_title,
        county_wide_ems_rate,
        cities,
        special_stuff,
        sales_tax_credit_factors,
    ):
        super().__init__(
            county_name,
            county_state,
            county_wide_rate_title,
            county_wide_rate,
            county_wide_police_title,
            county_wide_police_rate,
            county_wide_fire_title,
            county_wide_fire_rate,
            county_wide_ems_title,
            county_wide_ems_rate,
            cities,
            special_stuff,
        )

        # Inital configure of stcf classes
        self.inital_stcf_config(sales_tax_credit_factors)

    # inital setup and configs
    def inital_stcf_config(self, inital_dict):
        """
        inital_stcf_config inital config of classes pertaining to stcf config

        Args:
            inital_dict (dictionary): dict of possible sales tax credit factors for use

        Sets:
            self.stcf_class_list (list): Creates list of stcf classes
        """
        if inital_dict is not None:

            # initialize return list
            self.stcf_class_list = []

            # initialize lists for zipping
            title_list = []
            rate_list = []

            # populate lists
            for i in inital_dict:
                inner_dict = inital_dict[i]
                inner_title = list(inner_dict.keys())[0]
                title_list.append(inner_title)
                rate_list.append(inner_dict[inner_title])

            # use list to create classes
            for title, rate in zip(title_list, rate_list):
                self.stcf_class_list.append(SalesTaxCreditFactors(title, rate))

            # EOL

        else:
            self.stcf_class_list = None

    # modify items
    def modify_special_options(self):
        """
        modify_special_options run normal modify then check with then proceeded to modify sales tax credit options
        """
        # run base command
        super().modify_special_options()

        # present option to continue with sales tax credit options
        looper = InputHelper.choice_bool(
            "Would you like to modify Sales Tax Credit Factors?"
        )

        self.modify_sales_tax_credit_factors(looper)

        cls()

    def modify_sales_tax_credit_factors(self, looper):
        """
        modify_sales_tax_credit_factors

        Args:
            looper (bool): true or false on whether to continue in modifying stcf
        """
        while looper:
            current_rate_options_dict = self.generate_current_options_dict()

            choice_associated_dict_item = InputHelper.input_from_dict(
                current_rate_options_dict, "Sales Tax Credit Factor to Modify..."
            )

            # if option is quit end loop
            if choice_associated_dict_item == "Quit...":
                looper = False
            # if option is something else find the key associated with it
            else:
                # loop through options dict # TODO CONSIDER USING DICT ITEMS *************** (per pylint)
                for i in current_rate_options_dict:
                    # check if returned dict item is same as i key value
                    if current_rate_options_dict[i] == choice_associated_dict_item:
                        # if this is true ask to modify...
                        modify_choice_bool = InputHelper.choice_bool_with_header(
                            f"Is the property subject to a the following Sales Tax Credit Factor?\n...\n{current_rate_options_dict[i]}"
                        )

                        self.stcf_class_list[i - 1].mod_used_rate(modify_choice_bool)

    # generate items
    def generate_current_options_dict(self):
        """
        generate_current_options_dict generates dictionary with current value of rate and default rate for choice selection

        Returns:
            dict: dictionary containing quit option and options pertaining to class item in self.stcf_class_list
        """
        # initialize options dict
        options_dict = {0: "Quit..."}

        # append items to options dict with fstring
        for i in range(len(self.stcf_class_list)):
            class_item = self.stcf_class_list[i]
            string = f"{class_item.title} - Default Rate: {class_item.rate} | Current Rate: {class_item.used_rate}"

            options_dict[i + 1] = string

        # return final dict
        return options_dict

    def generate_county_statistics(self):
        #RUN SUPER
        super().generate_county_statistics()

        self.stcf_stats_dict={}
        for item in self.stcf_class_list:
            self.stcf_stats_dict[item.title]=item.used_rate

# Sales Tax Credit Factors Class
class SalesTaxCreditFactors:
    """
    class for individual sales tax credit factors
    """

    def __init__(self, title, rate):
        self.title = title
        self.rate = rate
        self.used_rate = None

    # get methods
    def get_title(self):
        """
        get_title returns title

        Returns:
            str: title of stcf rate
        """
        return self.title

    def get_default_rate(self):
        """
        get_default_rate returns base tax rate

        Returns:
            float: six digit after the decimal rate that is default
        """
        return self.rate

    def get_used_rate(self):
        """
        get_used_rate returns rate this being used

        Returns:
            float / None: returns None if not used or a float if it is in use currently
        """
        return self.used_rate

    # modify item
    def mod_used_rate(self, active_bool):
        """
        mod_used_rate modifies currently in use rate

        Args:
            active_bool (bool): true / false used to either activate or deactivate used rate

        Sets:
            self.used_rate (float / None): will be set to self.rate if bool is true or none if bool is false
        """
        if active_bool:
            self.used_rate = self.rate

        else:
            self.used_rate = None

        cls()

        Printer.liner()
        Printer.print_cyan(
            f"{self.title} currently used rate updated to {self.used_rate}"
        )
        Printer.liner()
