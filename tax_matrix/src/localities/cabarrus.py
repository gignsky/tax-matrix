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
    county_wide_rate = 0.0074
    county_wide_police_title = f"{county_name} Police"
    county_wide_police_rate = None
    county_wide_fire_title = f"{county_name} Fire"
    county_wide_fire_rate = None
    county_wide_ems_title = f"{county_name} EMS"
    county_wide_ems_rate = None
    cities = {
        1: town_of_harrisburg(),
        2: city_of_concord(),
        3: concord_downtown(),
        4: town_of_mt_pleasant(),
        5: city_of_kannapolis(),
        6: city_of_locust(),
        7: town_of_midland(),
    }

    county_fire_services = {
        1: {"Kannapolis Rural Fire": 0.001},
        2: {"Jackson Park Fire": 0.0014},
        3: {"Cold Water Fire": 0.0008},
        4: {"Allen Fire": 0.00075},
        5: {"Midland Fire": 0.001},
        6: {"Harrisburg Rural Fire": 0.0015},
        7: {"Rimer Fire": 0.00088},
        8: {"Mt. Mitchel Fire": 0.000826},
        9: {"Odell": 0.00068},
        10: {"Georgeville Fire": 0.00092},
        11: {"Flowes Store Fire": 0.0007},
        12: {"Northeast Fire": 0.00127},
        13: {"Mt. Pleasant Fire": 0.00118},
        14: {"Gold Hill Fire": 0.0008},
        15: {"Richfield Fire": 0.0007},
        16: {"Concord Rural Fire": 0.0014},
    }

    special_stuff = [None,county_fire_services]

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
    )

    return cabarrus


def town_of_harrisburg():
    """
        City Class
    """
    # INFORMATION
    city_name = "Town of Harrisburg"
    city_rate = 0.00355
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
    city_rate = 0.0048
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
    city_rate = 0.0023
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
    city_rate = 0.00505
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = 0.00118
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
    city_rate = 0.0063
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
    city_rate = 0.0036
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
    city_rate = 0.0022
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = 0.00104
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
