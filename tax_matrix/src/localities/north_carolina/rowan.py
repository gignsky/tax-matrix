"""
    rowan co rates document
"""


from . import general_classes


def main():
    """
    main contents of rowan county

    Returns:
        obj: county object
    """
    # INFORMATION:
    county_name = "Rowan Co., NC"
    county_wide_rate_title = "Rowan County Unincorporated Tax Rate"
    county_wide_rate = 0.6575
    county_wide_police_title = f"{county_name} Police"
    county_wide_police_rate = None
    county_wide_fire_title = f"{county_name} Fire"
    county_wide_fire_rate = None
    county_wide_ems_title = f"{county_name} EMS"
    county_wide_ems_rate = None
    tax_rates_year = 2021
    cities = {
        1: city_of_salisbury(),
        2: town_of_spencer(),
        3: town_of_east_spencer(),
        4: town_of_cleveland(),
        5: town_of_china_grove(),
        6: town_of_landis(),
        7: town_of_faith(),
        8: town_of_rockwell(),
        9: town_of_granite_quarry(),
        10: city_of_kannapolis(),
    }

    county_fire_services = {
        1: {"Enochville Fire District": 0.08},
        2: {"South Salisbury Fire District": 0.09},
        3: {"Rockwell Rural Fire District": 0.09},
        4: {"Pooletown Fire District": 0.09},
        5: {"Miller Ferry Fire District": 0.0875},
        6: {"Union Fire District": 0.035},
        7: {"Mt. Mitchell Fire District": 0.0726},
        8: {"Ellis Fire District": 0.085},
        9: {"Franklin Fire District": 0.09},
        10: {"Cleveland Community Fire": 0.0936},
        11: {"Atwell Fire District": 0.0975},
        12: {"Bostian Heights Fire District": 0.09},
        13: {"Locke Fire District": 0.0975},
        14: {"Liberty Fire District": 0.0537},
        15: {"East Gold Hill FSD": 0.08},
        16: {"Woodleaf Fire District": 0.065},
        17: {"Scotch-Irish FSD": 0.09},
        18: {"Salisbury Downtown Fire": 0.176},
        19: {"Rowan Iredell Fire": 0.0648},
        20: {"Richfield Misenheimer Fire District": 0.07},
        21: {"South Rowan Fire District": 0.09},
        22: {"East Rowan Fire District": 0.07},
        23: {"East Landis Fire District": 0.0425},
        24: {"West Rowan Fire District": 0.09},
    }

    special_stuff = [None, county_fire_services]

    rowan = general_classes.County(
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

    return rowan


def city_of_salisbury():
    """
    City Class
    """
    # INFORMATION
    city_name = "City of Salisbury"
    city_rate = 0.7196
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


def town_of_spencer():
    """
    City Class
    """
    # INFORMATION
    city_name = "Town of Spencer"
    city_rate = 0.655
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


def town_of_east_spencer():
    """
    City Class
    """
    # INFORMATION
    city_name = "Town of East Spencer"
    city_rate = 0.66
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


def town_of_cleveland():
    """
    City Class
    """
    # INFORMATION
    city_name = "Town of Cleveland"
    city_rate = 0.28
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


def town_of_china_grove():
    """
    City Class
    """
    # INFORMATION
    city_name = "Town of China Grove"
    city_rate = 0.54
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


def town_of_landis():
    """
    City Class
    """
    # INFORMATION
    city_name = "Town of Landis"
    city_rate = 0.53
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


def town_of_faith():
    """
    City Class
    """
    # INFORMATION
    city_name = "Town of Faith"
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


def town_of_rockwell():
    """
    City Class
    """
    # INFORMATION
    city_name = "Town of Rockwell"
    city_rate = 0.46
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


def town_of_granite_quarry():
    """
    City Class
    """
    # INFORMATION
    city_name = "Town of Granite Quarry"
    city_rate = 0.4175
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


def city_of_kannapolis():
    """
    City Class
    """
    # INFORMATION
    city_name = "City of Kannapolis"
    city_rate = 0.63
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
