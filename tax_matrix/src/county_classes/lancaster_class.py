"""
    generic lancaster county class
"""

from . import debugpy
from . import Printer
from . import InputHelper
from . import general_classes


class LancasterCo(general_classes.County):
    """
    LancasterCo special handler

    Args:
        general_classes (class): General County Class
    """

    def __init__(
        self,
        county_name,
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
        special_fees_per_items,
        sales_tax_credit_factors,
    ):
        super().__init__(
            county_name,
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

        # set & configure special dicts
        self.special_fees_per_items_dict = special_fees_per_items
        (
            self.special_fees_per_items_dict_titles,
            self.special_fees_per_items_dict_fees,
            self.special_fees_per_items_dict_item_types,
            self.special_fees_per_items_dict_items,
            self.special_fees_per_items_dict_items_multiple_rates,
            self.special_fees_per_items_dict_items_default_multiple_rate,
            self.special_fees_per_items_dict_items_default_fee,
            self.special_fees_per_items_dict_items_multiple_str,
        ) = self.seperate_per_items(self.special_fees_per_items_dict)
        self.sales_tax_credit_factors_master_dict = sales_tax_credit_factors

        # set

    # configuration of special dict methods
    def seperate_per_items(self, dictionary):
        titles = []
        fees = []
        item_types = []
        items = []
        multiple_values = []
        default_multiple_values = []
        default_fees = []
        multiple_value_strs = []
        for i in dictionary:
            # grab title
            title = i.get_title()
            titles.append(title)

            # grab key
            key_tuple = i[title]

            # tuple item zero
            tuple_0 = key_tuple[0]

            # tuple item one
            tuple_1 = key_tuple[1]

            # get fee amnt
            fee_amnt = tuple_0[1]

            # set fee amnt
            fees.append(None)
            default_fees.append(fee_amnt)

            # get item type
            item_type = tuple_1[0]

            # set item type
            item_types.append(item_type)

            # get multiple rate value
            multiple_rate = tuple_1[1]

            # set multiple rate type
            multiple_values.append(None)
            default_multiple_values.append(multiple_rate)

            # set item default value of 99999 for error throwing
            items.append(999999)

            # set string to none
            multiple_value_strs.append(None)
        return (
            titles,
            fees,
            item_types,
            items,
            multiple_values,
            default_multiple_values,
            multiple_value_strs,
        )

    # deal with special options
    def modify_special_options(self):
        super().modify_special_options()

        # per item fees
        self.per_item_stats = self.modify_per_item_options()

        # tax credit options
        self.tax_credit_stats = self.modify_tax_credit_options()

    # modify
    def modify_per_item_options(self):
        do_modify = InputHelper.choice_bool(
            "Would you like to apply special options that require per item multiplications?"
        )

        if not do_modify:
            return None
        else:
            looping = True

            while looping:
                self.mod_dictionary = self.create_per_item_options_dictionary()
                input_return = InputHelper.input_from_dict(
                    mod_dictionary, "Which Option would you like to modify?"
                )

                if input_return == self.mod_dictionary[0]:
                    looping = False
                elif input_return == self.mod_dictionary[1]:
                    self.modify_per_item(0)
                elif input_return == self.mod_dictionary[2]:
                    self.modify_per_item(1)
                else:
                    debugpy.breakpoint()

    ### Mod per item helper
    def modify_per_item(self, index_value):
        Printer.liner()
        print(self.mod_dictionary[index_value])
        Printer.liner()
        enable = InputHelper.choice_bool("Do you wish to enable this item?")

        if enable:
            self.special_fees_per_items_dict_fees[
                index_value
            ] = self.special_fees_per_items_dict_fees[index_value]

            Printer.liner()
            Printer.print_green(
                f"{self.special_fees_per_items_dict_titles[index_value]} has been enabled with a fee of ${self.special_fees_per_items_dict_fees[index_value]}..."
            )
            Printer.short_liner()

            if (
                self.special_fees_per_items_dict_items_multiple_rates[index_value]
                is None
            ):
                input_int, input_str = InputHelper.per_item_item_input(
                    self.special_fees_per_items_dict_item_types[index_value],
                    self.special_fees_per_items_dict_items_default_multiple_rate[
                        index_value
                    ],
                    self.special_fees_per_items_dict_items_multiple_rates[index_value],
                )

                self.apply_special_fee_per_item_value(index_value, input_int, input_str)
            else:
                choice_return = InputHelper.choice_bool(
                    f"Do you wish to modify the current value of {self.special_fees_per_items_dict_items_multiple_rates[index_value]} {self.special_fees_per_items_dict_item_types[index_value]}(s)?"
                )
                if choice_return:
                    input_int, input_str = InputHelper.per_item_item_input(
                        self.special_fees_per_items_dict_item_types[index_value],
                        self.special_fees_per_items_dict_items_default_multiple_rate[
                            index_value
                        ],
                        self.special_fees_per_items_dict_items_multiple_rates[
                            index_value
                        ],
                    )

                    self.apply_special_fee_per_item_value(
                        index_value, input_int, input_str
                    )
        else:
            self.special_fees_per_items_dict_fees[index_value] = None

    # apply value
    def apply_special_fee_per_item_value(self, index_value, int_value, str_value):
        self.special_fees_per_items_dict_items_multiple_rates[index_value] = int_value
        self.special_fees_per_items_dict_items_multiple_str[index_value] = str_value

    # generate dictionary options
    def create_per_item_options_dictionary(self):
        dict_to_return = {}
        looping = True
        index_value = 0

        while looping:
            if index_value == 0:
                dict_to_return[index_value] = "Quit"
                index_value += 1
            else:
                for (
                    title,
                    fee,
                    item_type,
                    item,
                    multiple,
                    default_multiple,
                    default_fee,
                ) in zip(
                    self.special_fees_per_items_dict_titles,
                    self.special_fees_per_items_dict_fees,
                    self.special_fees_per_items_dict_item_types,
                    self.special_fees_per_items_dict_items,
                    self.special_fees_per_items_dict_items_multiple_rates,
                    self.special_fees_per_items_dict_items_default_multiple_rate,
                    self.special_fees_per_items_dict_items_default_fee,
                ):
                    dict_to_return[
                        index_value
                    ] = f"{title} - Fee: ${fee} - {item_type}: {item} | {multiple} {item_type}(s) | DEFAULT FEE: ${default_fee} - Per {default_multiple} {item_type}(s)"
                    index_value += 1
                looping = False

        return dict_to_return
