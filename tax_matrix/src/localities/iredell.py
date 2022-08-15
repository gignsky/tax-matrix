"""
   iredell co rates document
"""

from . import classes
from . import special_classes

def main():
    """
    main general function for iredell county

    Returns:
        obj: county class
    """
    # INFORMATION:
    county_name = "Iredell Co., NC"
    county_wide_rate_title = "Iredell County Unincorporated Tax Rate"
    county_wide_rate = 0.005375
    county_wide_police_title = f"{county_name} Police"
    county_wide_police_rate = None
    county_wide_fire_title = f"{county_name} Fire"
    county_wide_fire_rate = 0.0009
    county_wide_ems_title = f"{county_name} EMS"
    county_wide_ems_rate = None
    cities = {
        1: statesville_city(),
        2: statesville_downtown(),
        3: woods_municipal_ser(),
        4: troutman(),
        5: harmony(),
        6: mooresville_town(),
        7: mooresville_downtown(),
        8: mooresville_school(),
        9: love_valley(),
        10: davidson_town(),
    }
    special_stuff = True

    # countywide solid waste fee
    special_county_waste_name = "Iredell Co., Solid Waste Fee"
    special_county_waste_fee = 60.00

    # special fire rates - unused with no rates
    special_fire = {
        1: {"East Alexander Fire": 0},
        2: {"Shepherds Fire": 0},
        3: {"Mount Mourne Fire": 0},
        5: {"B&F Fire": 0},
    }

    iredell = special_classes.iredell_classes.Iredell(
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
        special_county_waste_name,
        special_county_waste_fee,
        special_fire,
    )

    return iredell



def statesville_city():
    """
        City Class
    """
    # INFORMATION
    city_name = "Statesville City"
    city_rate = 0.005478
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    # Specific
    waste_title = f"{city_name} Solid Waste Fee"
    waste_fee = 60.00

    city = special_classes.city_with_waste_fee.CityWithWasteFee(
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


def statesville_downtown():
    """
        City Class
    """
    # INFORMATION
    city_name = "Statesville Downtown"
    city_rate = 0.001
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    city = classes.City(
        city_name,
        city_rate,
        city_rate_title,
        police_rate,
        police_rate_title,
        fire_rate,
        fire_rate_title,
    )

    return city


def woods_municipal_ser():
    """
        City Class
    """
    # INFORMATION
    city_name = "Woods Municipal Ser."
    city_rate = 0.0021
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    city = classes.City(
        city_name,
        city_rate,
        city_rate_title,
        police_rate,
        police_rate_title,
        fire_rate,
        fire_rate_title,
    )

    return city


def troutman():
    """
        City Class
    """
    # INFORMATION
    city_name = "Troutman"
    city_rate = 0.0052
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    city = classes.City(
        city_name,
        city_rate,
        city_rate_title,
        police_rate,
        police_rate_title,
        fire_rate,
        fire_rate_title,
    )

    return city


def harmony():
    """
        City Class
    """
    # INFORMATION
    city_name = "Harmony"
    city_rate = 0.0014
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    city = classes.City(
        city_name,
        city_rate,
        city_rate_title,
        police_rate,
        police_rate_title,
        fire_rate,
        fire_rate_title,
    )

    return city


def mooresville_town():
    """
        City Class
    """
    # INFORMATION
    city_name = "Mooresville Town"
    city_rate = 0.0058
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    # Specific
    waste_title = f"{city_name} Solid Waste Fee"
    waste_fee = 120.00

    city = special_classes.city_with_waste_fee.CityWithWasteFee(
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


def mooresville_downtown():
    """
        City Class
    """
    # INFORMATION
    city_name = "Mooresville Downtown"
    city_rate = 0.0016
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    # Specific
    waste_title = f"{city_name} Solid Waste Fee"
    waste_fee = 120.00

    city = special_classes.city_with_waste_fee.CityWithWasteFee(
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


def mooresville_school():
    """
        City Class
    """
    # INFORMATION
    city_name = "Mooresville School"
    city_rate = 0.00185
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    # Specific
    waste_title = f"{city_name} Solid Waste Fee"
    waste_fee = 120.00

    city = special_classes.city_with_waste_fee.CityWithWasteFee(
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


def love_valley():
    """
        City Class
    """
    # INFORMATION
    city_name = "Love Valley"
    city_rate = 0.0025
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    city = classes.City(
        city_name,
        city_rate,
        city_rate_title,
        police_rate,
        police_rate_title,
        fire_rate,
        fire_rate_title,
    )

    return city


def davidson_town():
    """
        City Class
    """
    # INFORMATION
    city_name = "Davidson Town"
    city_rate = 0.00325
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    city = classes.City(
        city_name,
        city_rate,
        city_rate_title,
        police_rate,
        police_rate_title,
        fire_rate,
        fire_rate_title,
    )

    return city
