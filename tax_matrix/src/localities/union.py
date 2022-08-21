"""
    union co rates document
"""

from . import general_classes
from . import special_classes
from . import county_classes

def main():
    """
    main main info for union County

    Returns:
        obj: county class
    """

    # INFORMATION:
    county_name = "Union Co., NC"
    county_wide_rate_title = "Union County General Government Fund Tax Rate"
    county_wide_rate = 0.004819
    county_wide_police_title = f"{county_name} Police"
    county_wide_police_rate = None
    county_wide_fire_title = f"{county_name} Fire"
    county_wide_fire_rate = None
    county_wide_ems_title = f"{county_name} EMS"
    county_wide_ems_rate = None
    cities = {
        1: village_of_marvin(),
        2: city_of_monroe(),
        3: town_of_wingate(),
        4: town_of_marshville(),
        5: town_of_waxhaw(),
        6: town_of_indian_trail(),
        7: town_of_stallings(),
        8: town_of_weddington(),
        9: village_of_lake_park(),
        10: town_of_fairview(),
        11: town_of_hemby_bridge(),
        12: village_of_wesley_chapel(),
        13: town_of_unionville(),
        14: town_of_mineral_springs(),
        15: town_of_mint_hill(),
    }


    # special fire rates
    special_fire = {
        1: {
            "Griffith Road": 0.0002
        },
        2: {
            "Stack Road": 0.000348
        },
        3: {
            "Springs": 0.000464
        },
        4: {
            "Fairview": 0.000503
        },
        5: {
            "New Salem": 0.000384
        },
        6: {
            "Beaver Lane": 0.000671
        },
        7: {
            "Bakers": 0.000343
        },
        8: {
            "Stallings": 0.000478
        },
        9: {
            "Unionville": 0.000614
        },
        10: {
            "Wingate": 0.00067
        },
        11: {
            "Hemby Bridge": 0.000441
        },
        12: {
            "Allens Crossroads": 0.000689
        },
        13: {
            "Jackson": 0.000399
        },
        14: {
            "Wesley Chapel": 0.000375
        },
        15: {
            "Lanes Creek": 0.000546
        },
        16: {
            "Waxhaw": 0.000419
        },
        17: {
            "Sandy Ridge": 0.000329
        },
        18: {
            "Providence": 0.000375
        },
    }

    # Special Stuff Ttiles & Rates
    special_debt_fund={
        19: {"Debt Budgetary Fund":0.001061}}

    all_rate_options=special_fire
    all_rate_options.update(special_debt_fund)

    special_stuff = [None,all_rate_options]

    union = general_classes.County(
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

    return union

def village_of_marvin():
    """
        City Class
    """
    # INFORMATION
    city_name = "Village of Marvin"
    city_rate = 0.0006
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    # Specific
    waste_title = f"{city_name} Solid Waste Fee"
    waste_fee = 244.00

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

def city_of_monroe():
    """
        City Class
    """
    # INFORMATION
    city_name = "City of Monroe"
    city_rate = 0.005025
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    # specific
    special_district_title = "Downtown Special District"
    special_district_rate = 0.001950

    city = county_classes.union_classes.CityOfMonroe(
        city_name,
        city_rate,
        city_rate_title,
        police_rate,
        police_rate_title,
        fire_rate,
        fire_rate_title,
        special_district_title,
        special_district_rate,
    )

    return city

def town_of_wingate():
    """
        City Class
    """
    # INFORMATION
    city_name = "Town of Wingate"
    city_rate = 0.0034
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

def town_of_marshville():
    """
        City Class
    """
    # INFORMATION
    city_name = "Town of Marshville"
    city_rate = 0.0049
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

def town_of_waxhaw():
    """
        City Class
    """
    # INFORMATION
    city_name = "Tax of Waxhaw"
    city_rate = 0.00385
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

def town_of_indian_trail():
    """
        City Class
    """
    # INFORMATION
    city_name = "Town of Indian Trail"
    city_rate = 0.00185
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

def town_of_stallings():
    """
        City Class
    """
    # INFORMATION
    city_name = "Town of Stallings"
    city_rate = 0.00186
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

def town_of_weddington():
    """
        City Class
    """
    # INFORMATION
    city_name = "Town of Weddington"
    city_rate = 0.00048
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

def village_of_lake_park():
    """
        City Class
    """
    # INFORMATION
    city_name = "Village of Lake Park"
    city_rate = 0.002025
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

def town_of_fairview():
    """
        City Class
    """
    # INFORMATION
    city_name = "Town of Fairview"
    city_rate = 0.0002
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

def town_of_hemby_bridge():
    """
        City Class
    """
    # INFORMATION
    city_name = "Town of Hemby Bridge"
    city_rate = 0
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

def village_of_wesley_chapel():
    """
        City Class
    """
    # INFORMATION
    city_name = "Village of Wesley Chapel"
    city_rate = 0.000129
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

def town_of_unionville():
    """
        City Class
    """
    # INFORMATION
    city_name = "Town of Unionville"
    city_rate = 0.0002
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

def town_of_mineral_springs():
    """
        City Class
    """
    # INFORMATION
    city_name = "Town of Mineral Springs"
    city_rate = 0.00021
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
    city_rate = 0
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
