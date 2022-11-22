"""
    lancaster county taxes
"""

from . import general_classes
from . import county_classes


def main():
    """
    main info for lancaster co
    """

    # INFORMATION:
    county_name = "Lancaster Co., SC"
    county_state = "SC"
    county_wide_rate_title = "Lancaster County Base Millage"
    county_wide_rate = 0
    county_wide_police_title = f"{county_name} Police"
    county_wide_police_rate = None
    county_wide_fire_title = f"{county_name} Fire"
    county_wide_fire_rate = None
    county_wide_ems_title = f"{county_name} EMS"
    county_wide_ems_rate = None

    cities = {
        1: municipal_lancaster(),
        2: kershaw(),
    }

    # special rates
    special_rates = {
        1: {"County Operations": 84.3},
        2: {"County Debt": 9.6},
        3: {"Capital Improvement": 4.8},
        4: {
            "School Operating": 171.8
        },  # NOTE CREDIT ALWAYS APPLIED ON RESIDENTIAL (0.04) PROPERTIES
        5: {"School Debt": 65},
        6: {"USC-Lancaster": 4.6},
        7: {"Courthouse Security": 3.6},
    }

    # special fees
    special_fees = None

    special_stuff = [special_fees, special_rates]

    # NOTE multiplied by base purchase price rate not any multiple rate
    sales_tax_credit_factors = {
        1: {"Local Option Sales Tax Credit Factors (Lancaster - County)": 0.000784},
        2: {"Local Option Sales Tax Credit Factors (Lancaster - City)": 0.003728},
        3: {"Local Option Sales Tax Credit Factors (Kershaw - City)": 0.003520},
    }

    lancaster = county_classes.lancaster_class.LancasterCo(
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
    )

    return lancaster


def municipal_lancaster():
    """
    City Class
    """
    # INFORMATION
    city_name = "Lancaster"
    city_rate = 178.8
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    city = general_classes.City(
        city_name,
        city_rate,
        city_rate_title,
        police_rate,
        police_rate_title,
        fire_rate,
        fire_rate_title,
    )

    return city


def kershaw():
    """
    City Class
    """
    # INFORMATION
    city_name = "Kershaw"
    city_rate = 95.6
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    city = general_classes.City(
        city_name,
        city_rate,
        city_rate_title,
        police_rate,
        police_rate_title,
        fire_rate,
        fire_rate_title,
    )

    return city
