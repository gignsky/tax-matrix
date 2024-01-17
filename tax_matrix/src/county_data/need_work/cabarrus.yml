"""
    cabarrus co rates document
"""


from . import general_classes


def main():
    """
    main contents of cabarrus county

    Returns:
        obj: county object
    """
    # INFORMATION:
    county_name = "Cabarrus Co., NC"
    county_wide_rate_title = "Cabarrus County Unincorporated Tax Rate"
    county_wide_rate = 0.74
    county_wide_police_title = f"{county_name} Police"
    county_wide_police_rate = None
    county_wide_fire_title = f"{county_name} Fire"
    county_wide_fire_rate = None
    county_wide_ems_title = f"{county_name} EMS"
    county_wide_ems_rate = None
    tax_rates_year = 2023
    cities = {
        1: town_of_harrisburg(),
        2: city_of_concord(),
        3: concord_downtown(),
        4: town_of_mt_pleasant(),
        5: city_of_kannapolis(),
        6: city_of_locust(),
        7: town_of_midland(),
        8: town_of_huntersville(),
    }

    county_fire_services = {
        1: {"Kannapolis Rural Fire District": 0.1},
        2: {"Jackson Park Fire District": 0.14},
        3: {"Cold Water Fire District": 0.08},
        4: {"Allen Fire District": 0.09},
        5: {"Midland Fire District": 0.1},
        6: {"Harrisburg Rural Fire District": 0.15},
        7: {"Rimer Fire District": 0.088},
        8: {"Mt. Mitchel Fire District": 0.0826},
        9: {"Odell Fire District": 0.068},
        10: {"Georgeville Fire District": 0.092},
        11: {"Flowes Store Fire District": 0.1},
        12: {"Northeast Fire District": 0.127},
        13: {"Mt. Pleasant Fire District": 0.118},
        14: {"Gold Hill Fire District": 0.09},
        15: {"Richfield Fire District": 0.07},
        16: {"Concord Rural Fire District": 0.14},
    }

    special_stuff = [None, county_fire_services]

    cabarrus = general_classes.County(
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

    return cabarrus


def town_of_harrisburg():
    """
    City Class
    """
    # INFORMATION
    city_name = "Town of Harrisburg"
    city_rate = 0.435
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


def city_of_concord():
    """
    City Class
    """
    # INFORMATION
    city_name = "City of Concord"
    city_rate = 0.48
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


def concord_downtown():
    """
    City Class
    """
    # INFORMATION
    city_name = "Concord Downtown"
    city_rate = 0.23
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


def town_of_mt_pleasant():
    """
    City Class
    """
    # INFORMATION
    city_name = "Town of Mt. Pleasant"
    city_rate = 0.505
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = 0.118
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
    city_name = "Town of Kannapolis"
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


def city_of_locust():
    """
    City Class
    """
    # INFORMATION
    city_name = "City of Locust"
    city_rate = 0.36
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


def town_of_midland():
    """
    City Class
    """
    # INFORMATION
    city_name = "Town of Midland"
    city_rate = 0.22
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = 0.104
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
