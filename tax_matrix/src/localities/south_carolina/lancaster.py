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
    county_name = "Lancaster Co., NC"
    county_wide_rate_title = "Lancaster County Base Millage"
    county_wide_rate = 0
    county_wide_police_title = f"{county_name} Police"
    county_wide_police_rate = None
    county_wide_fire_title = f"{county_name} Fire"
    county_wide_fire_rate = None
    county_wide_ems_title = f"{county_name} EMS"
    county_wide_ems_rate = None

    cities = {
        1: kershaw(),
        2: municipal_lancaster(),
        3: reid_point(),
    }

    # special rates
    special_rates = {
        1: {"County Base Millage Rate - County Operations": 0.0843},
        2: {"County Base Millage Rate - County Debt Service": 0.0085},
        3: {"County Base Millage Rate - Capital Improvement": 0.0048},
        4: {"County Base Millage Rate - Courthouse Fire Security": 0.0036},
        5: {"School District Millage Rate - School Operating": 0.1685},
        6: {"School District Millage Rate - Debt Service": 0.065},
        7: {"School District Millage Rate - USC-Lancaster": 0.0046},
    }

    # special fees
    special_fees = {
        1: {"#10 Indian Land Fire Fee": 90.00},
        2: {"Brookchase Road Bond (District 87) Fee": 225.00},
    }

    special_stuff = [special_fees, special_rates]

#     # special fees per a unit item
#     special_fees_per_items = {
#         1: {
#             "#14 (Pleasant Valley) Fire District Fee (per 2,500 sqft)": [
#                 {"fee": 90.00},
#                 {"sqft": 2500},
#             ]
#         },
#         2: {"Storm Water (Countywide, per unit) Fee": [{"fee": 60.00}, {"unit": 1}]},
#     }
#
#     sales_tax_credit_factors = {
#         1: {"Local Option Sales Tax Credit Factors (Kershaw - City)": 0.00352},
#         2: {"Local Option Sales Tax Credit Factors (Kershaw - County)": 0.000869},
#         3: {"Local Option Sales Tax Credit Factors (Lancaster - City)": 0.003608},
#         4: {"Local Option Sales Tax Credit Factors (Lancaster - County)": 0.000869},
#     }

    lancaster = county_classes.lancaster_class.LancasterCo(
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
        # special_fees_per_items,
        # sales_tax_credit_factors,
    )

    return lancaster


def kershaw():
    """
    City Class
    """
    # INFORMATION
    city_name = "Kershaw"
    city_rate = 0.0959
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


def municipal_lancaster():
    """
    City Class
    """
    # INFORMATION
    city_name = "Lancaster"
    city_rate = 0.1759
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


def reid_point():
    """
    City Class
    """
    # INFORMATION
    city_name = "Reid Point (Special Purpose District)"
    city_rate = 0.035
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
