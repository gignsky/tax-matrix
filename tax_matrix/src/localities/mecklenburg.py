"""
    meck co rates document
"""


from . import classes
from ..special_county_classes import mecklenburg_classes

def main():
    """
    main main initialization function for meck co

    Returns:
        class: class object containing county
    """

    # INFORMATION:
    county_name = "Mecklenburg Co., NC"
    county_wide_rate_title = "Mecklenburg County Unincorporated Tax Rate"
    county_wide_rate = 0.006169
    county_wide_police_title = f"{county_name} Police"
    county_wide_police_rate = None
    county_wide_fire_title = f"{county_name} Fire"
    county_wide_fire_rate = None
    county_wide_ems_title = f"{county_name} EMS"
    county_wide_ems_rate = None
    cities = {
        1: charlotte(),
        2: city_of_charlotte(),
        3: town_of_cornelius(),
        4: town_of_davidson(),
        5: town_of_huntersville(),
        6: town_of_matthews(),
        7: town_of_mint_hill(),
        8: town_of_pineville(),
        9: stallings(),
    }
    special_stuff = True
    waste_options = {
        1: {"Mecklenburg Single- & Multi- Family Solid Waste Fee": 39.50},
        2: {"Charlotte Single- & Multi- Family Solid Waste Fee": 86.06},
        3: {"Huntersville Single- & Multi- Family Solid Waste Fee": 126.00},
    }
    meck_services = {
        1: {"Police District Unincorporated Area (ETJ) For Charlotte": 0.001781},
        2: {
            "Fire District Unincorporated Area (ETJ) For Charlotte (Includes Pineville Sphere)": 0.001015
        },
        3: {"Police District Unincorporated Area (ETJ) For Cornelius": 0.00229},
        4: {"Fire District Unincorporated Area (ETJ) For Cornelius": 0.000612},
        5: {"Police District Unincorporated Area (ETJ) For Davidson": 0.001432},
        6: {"Fire District Unincorporated Area (ETJ) For Davidson": 0.00089},
        7: {"Police District Unincorporated Area (ETJ) For Huntersville": 0.001584},
        8: {"Fire District Unincorporated Area (ETJ) For Huntersville": 0.000663},
        9: {"Police District Unincorporated Area (ETJ) For Mint Hill": 0.001558},
        10: {"Fire District Unincorporated Area (ETJ) For Mint Hill": 0.00075},
        11: {"Police District Unincorporated Area (ETJ) For Pineville": 0.001637},
    }

    meck = mecklenburg_classes.Mecklenburg(
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
        waste_options,
        meck_services,
    )

    return meck

# consider moving below classes to antoher file or folder would need to loaded prior to to localities folder


def charlotte():
    # INFORMATION
    city_name = "Charlotte"
    city_rate = 0.003481
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

def city_of_charlotte():
    # INFORMATION
    city_name = "City of Charlotte"
    city_rate = 0.003481
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"
    special_districts = {
        1: {"District 1": {0.000136: "City of Charlotte District 1"}},
        2: {"District 2": {0.000363: "City of Charlotte District 2"}},
        3: {"District 3": {0.000474: "City of Charlotte District 3"}},
        4: {"District 4": {0.00039: "City of Charlotte District 4"}},
        5: {"District 5": {0.000279: "City of Charlotte District 5"}},
        6: {"District 6": {0.0004: "City of Charlotte District 6 (SouthPark)"}},
    }

    city = mecklenburg_classes.CityOfCharlotte(
        city_name,
        city_rate,
        city_rate_title,
        police_rate,
        police_rate_title,
        fire_rate,
        fire_rate_title,
        special_districts,
    )

    return city



def town_of_cornelius():
    # INFORMATION
    city_name = "Town of Cornelius"
    city_rate = 0.00232
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


def town_of_davidson():
    # INFORMATION
    city_name = "Town of Davidson"
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


def town_of_huntersville():
    # INFORMATION
    city_name = "Town of Huntersville"
    city_rate = 0.0024
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


def town_of_matthews():
    # INFORMATION
    city_name = "Town of Matthews"
    city_rate = 0.00295
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


def town_of_mint_hill():
    # INFORMATION
    city_name = "Town of Mint Hill"
    city_rate = 0.00255
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


def town_of_pineville():
    # INFORMATION
    city_name = "Town of Pineville"
    city_rate = 0.0033
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


def stallings():
    # INFORMATION
    city_name = "Stallings"
    city_rate = 0.00186
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
