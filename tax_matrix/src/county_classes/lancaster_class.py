"""
    generic lancaster county class
"""

# from . import debugpy
# from . import Printer
# from . import InputHelper
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
        # TODO UNCOMMENT WHEN THING IS WORKED ON
        self.stcf_dict = sales_tax_credit_factors

    def modify_special_options(self):

        #run base command
        super()

        #present option to continue with sales tax credit options
        looper=LogicalWork.choice_bool("Would you like to modify Sales Tax Credit Factors?")

        while looper:
            
