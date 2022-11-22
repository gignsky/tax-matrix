"""
    meck co rates document
"""


from . import general_classes
from . import county_classes


def main():
    """
    main main initialization function for meck co

    Returns:
        class: class object containing county
    """

    # INFORMATION:
    county_name = "Mecklenburg Co., NC"
    county_state = "NC"
    county_wide_rate_title = "Mecklenburg County Unincorporated Tax Rate"
    county_wide_rate = 0.6169
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
    waste_options = {
        1: {"Mecklenburg Single- & Multi- Family Solid Waste Fee": 39.50},
        2: {"Charlotte Single- & Multi- Family Solid Waste Fee": 86.06},
        3: {"Huntersville Single- & Multi- Family Solid Waste Fee": 126.00},
    }
    meck_services = {
        1: {"Police District Unincorporated Area (ETJ) For Charlotte": 0.1781},
        2: {
            "Fire District Unincorporated Area (ETJ) For Charlotte (Includes Pineville Sphere)": 0.1015
        },
        3: {"Police District Unincorporated Area (ETJ) For Cornelius": 0.229},
        4: {"Fire District Unincorporated Area (ETJ) For Cornelius": 0.0612},
        5: {"Police District Unincorporated Area (ETJ) For Davidson": 0.1432},
        6: {"Fire District Unincorporated Area (ETJ) For Davidson": 0.089},
        7: {"Police District Unincorporated Area (ETJ) For Huntersville": 0.1584},
        8: {"Fire District Unincorporated Area (ETJ) For Huntersville": 0.0663},
        9: {"Police District Unincorporated Area (ETJ) For Mint Hill": 0.1558},
        10: {"Fire District Unincorporated Area (ETJ) For Mint Hill": 0.075},
        11: {"Police District Unincorporated Area (ETJ) For Pineville": 0.1637},
    }

    special_stuff = [waste_options, meck_services]

    meck = general_classes.County(
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

    return meck


# consider moving below classes to antoher file or folder would need to loaded prior to to localities folder


def charlotte():
    """
    City Class
    """
    # INFORMATION
    city_name = "Charlotte"
    city_rate = 0.3481
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


def city_of_charlotte():
    """
    City Class
    """
    # INFORMATION
    city_name = "City of Charlotte"
    city_rate = 0.3481
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"
    special_districts = {
        1: {"District 1": {0.0136: "City of Charlotte District 1"}},
        2: {"District 2": {0.0363: "City of Charlotte District 2"}},
        3: {"District 3": {0.0474: "City of Charlotte District 3"}},
        4: {"District 4": {0.039: "City of Charlotte District 4"}},
        5: {"District 5": {0.0279: "City of Charlotte District 5"}},
        6: {"District 6": {0.04: "City of Charlotte District 6 (SouthPark)"}},
    }

    city = county_classes.mecklenburg_classes.CityOfCharlotte(
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
    """
    City Class
    """
    # INFORMATION
    city_name = "Town of Cornelius"
    city_rate = 0.232
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


def town_of_davidson():
    """
    City Class
    """
    # INFORMATION
    city_name = "Town of Davidson"
    city_rate = 0.325
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


def town_of_huntersville():
    """
    City Class
    """
    # INFORMATION
    city_name = "Town of Huntersville"
    city_rate = 0.24
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


def town_of_matthews():
    """
    City Class
    """
    # INFORMATION
    city_name = "Town of Matthews"
    city_rate = 0.295
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


def town_of_mint_hill():
    """
    City Class
    """
    # INFORMATION
    city_name = "Town of Mint Hill"
    city_rate = 0.255
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


def town_of_pineville():
    """
    City Class
    """
    # INFORMATION
    city_name = "Town of Pineville"
    city_rate = 0.33
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


def stallings():
    """
    City Class
    """
    # INFORMATION
    city_name = "Stallings"
    city_rate = 0.186
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
