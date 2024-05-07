"""
    stanly co rates
"""

from . import general_classes
from . import special_classes


def main():
    """
    main info for stanly co
    """

    # INFORMATION:
    county_name = "Stanly Co., NC"
    county_wide_rate_title = "Stanly Co., Unincorporated Tax Rate"
    county_wide_rate = 0.61
    county_wide_police_title = f"{county_name} Police"
    county_wide_police_rate = None
    county_wide_fire_title = f"{county_name} Fire"
    county_wide_fire_rate = None
    county_wide_ems_title = f"{county_name} EMS"
    county_wide_ems_rate = None
    tax_rates_year = 2023
    cities = {
        1: albemarle(),
        2: oakboro(),
        3: badin(),
        4: norwood(),
        5: locust(),
        6: stanfield(),
        7: new_london(),
        8: richfield(),
        9: red_cross(),
        10: misenheimer(),
    }

    # special fire rates
    special_fire = {
        1: {"West Stanly Fire": 0.11},
        2: {"Center Fire": 0.1},
        3: {"Endy Fire": 0.1},
        4: {"Ridgecrest Fire": 0.11},
        5: {"Aquadale Fire": 0.1},
        6: {"Eastside Fire": 0.1},
        7: {"Oakboro Fire": 0.06},
        8: {"New London Fire": 0.075},
        9: {"Southside Fire": 0.15},
        10: {"Bethany Fire": 0.0775},
        11: {"Richfield-Misenheimer Fire": 0.07},
        12: {"Millingport Fire": 0.1},
        13: {"Badin/Yadkin Valley Fire": 0.0803},
        14: {"Norwood Special Fire": 0.1},
        15: {"Municipal Service Dist. Fire": 0.1},
    }

    # solid waste fees
    special_waste = {
        1: {"Solid Waste Fee - County": 97.00},
        2: {"Solid Waste Fee - Locust": 120.00},
    }

    special_stuff = [special_waste, special_fire]

    stanly = general_classes.County(
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
        tax_rates_year,
    )

    return stanly


def albemarle():
    """
    City Class
    """
    # INFORMATION
    city_name = "Albemarle"
    city_rate = 0.61
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


def oakboro():
    """
    City Class
    """
    # INFORMATION
    city_name = "Oakboro"
    city_rate = 0.41
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


def badin():
    """
    City Class
    """
    # INFORMATION
    city_name = "Badin"
    city_rate = 0.4475
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = 0.0803
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


def norwood():
    """
    City Class
    """
    # INFORMATION
    city_name = "Norwood"
    city_rate = 0.39
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


def locust():
    """
    City Class
    """
    # INFORMATION
    city_name = "Locust"
    city_rate = 0.36
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = 0.11
    fire_rate_title = f"{city_name} Fire"

    # waste options
    waste_title = "Solid Waste Fee - Locust"
    waste_fee = 120.00

    city = special_classes.CityWithWasteFee(
        city_name,
        city_rate,
        city_rate_title,
        police_rate,
        police_rate_title,
        fire_rate,
        fire_rate_title,
        waste_title,
        waste_fee,
    )

    return city


def stanfield():
    """
    City Class
    """
    # INFORMATION
    city_name = "Stanfield"
    city_rate = 0.32
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = 0.11
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


def new_london():
    """
    City Class
    """
    # INFORMATION
    city_name = "New London"
    city_rate = 0.16
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = 0.075
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


def richfield():
    """
    City Class
    """
    # INFORMATION
    city_name = "Richfield"
    city_rate = 0.22
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = 0.07
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


def red_cross():
    """
    City Class
    """
    # INFORMATION
    city_name = "Red Cross"
    city_rate = 0.16
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


def misenheimer():
    """
    City Class
    """
    # INFORMATION
    city_name = "Misenheimer"
    city_rate = 0.22
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
