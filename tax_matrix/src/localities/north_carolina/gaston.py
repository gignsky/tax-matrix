"""
    gaston co rates document
"""


from . import general_classes


def main():
    """
    main contents of gaston county

    Returns:
        obj: county object
    """
    # INFORMATION:
    county_name = "Gaston Co., NC"
    county_wide_rate_title = "Gaston County Unincorporated Tax Rate"
    county_wide_rate = 0.61
    county_wide_police_title = f"{county_name} Police"
    county_wide_police_rate = None
    county_wide_fire_title = f"{county_name} Fire"
    county_wide_fire_rate = None
    county_wide_ems_title = f"{county_name} EMS"
    county_wide_ems_rate = None
    tax_rates_year = 2023
    cities = {
        1: belmont(),
        2: bessemer(),
        3: cherryville(),
        4: cramerton(),
        5: dallas(),
        6: gastonia(),
        7: york_chest_historic_city(),
        8: gastonia_downtown(),
        8: high_shls(),
        9: kings_mtn(),
        10: lowell(),
        11: mcadenville(),
        12: mt_holly(),
        13: ranlo(),
        14: spencer_mtn(),
        15: stanly(),
    }
    county_fire_services = {
        1: {"AG Center Fire": 0.085},
        2: {"Alexis Fire Department": 0.085},
        3: {"Chapel Grove Fire": 0.085},
        4: {"Chestnut Ridge Fire Department": 0.085},
        5: {"Community Fire Department": 0.085},
        6: {"Crouse Fire Department": 0.085},
        7: {"East Gaston Fire Department": 0.085},
        8: {"Hughs Pond Fire Department": 0.085},
        9: {"Long Shoals Fire Department": 0.085},
        10: {"Lowell Fire Department": 0.085},
        11: {"Lucia-RvBend Fire Department": 0.085},
        12: {"New Hope Fire Department": 0.085},
        13: {"Ranlo Fire Department": 0.085},
        14: {"S. Gastonia Fire Department": 0.085},
        15: {"South Point Fire Department": 0.085},
        16: {"Tryonota Fire Department": 0.085},
        17: {"Union Road Fire Department": 0.085},
        18: {"Waco Fire Department": 0.085},
    }

    special_stuff = [None, county_fire_services]

    gaston = general_classes.County(
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

    return gaston


def belmont():
    """
    City Class
    """
    # INFORMATION
    city_name = "Belmont City"
    city_rate = 0.455
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


def bessemer():
    """
    City Class
    """
    # INFORMATION
    city_name = "Bessemer City"
    city_rate = 0.45
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


def cherryville():
    """
    City Class
    """
    # INFORMATION
    city_name = "Cherryville City"
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


def cramerton():
    """
    City Class
    """
    # INFORMATION
    city_name = "Cramerton City"
    city_rate = 0.445
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


def dallas():
    """
    City Class
    """
    # INFORMATION
    city_name = "Town of Dallas"
    city_rate = 0.42
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


def gastonia():
    """
    City Class
    """
    # INFORMATION
    city_name = "Gastonia City"
    city_rate = 0.47
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

def york_chest_historic_city():
    """
    City Class
    """
    # INFORMATION
    city_name = "York-Chest. Hist + City"
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

def gastonia_downtown():
    """
    City Class
    """
    # INFORMATION
    city_name = "Gastonia Downtown Special District"
    city_rate = 0.2
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


def high_shls():
    """
    City Class
    """
    # INFORMATION
    city_name = "High Shoals City"
    city_rate = 0.32
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = 0.085
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


def kings_mtn():
    """
    City Class
    """
    # INFORMATION
    city_name = "Kings Mtn City"
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


def lowell():
    """
    City Class
    """
    # INFORMATION
    city_name = "Lowell City"
    city_rate = 0.49
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = 0.085
    fire_rate_title = f"{city_name} Fire Department"

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


def mcadenville():
    """
    City Class
    """
    # INFORMATION
    city_name = "McAdenville City"
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


def mt_holly():
    """
    City Class
    """
    # INFORMATION
    city_name = "Mount Holly City"
    city_rate = 0.405
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


def ranlo():
    """
    City Class
    """
    # INFORMATION
    city_name = "Ranlo City"
    city_rate = 0.45
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = 0.085
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


def spencer_mtn():
    """
    City Class
    """
    # INFORMATION
    city_name = "Spencer Mtn"
    city_rate = 0
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = 0.085
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


def stanly():
    """
    City Class
    """
    # INFORMATION
    city_name = "Stanley City"
    city_rate = 0.49
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
