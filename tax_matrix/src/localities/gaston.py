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
    county_wide_rate = 0.83
    county_wide_police_title = f"{county_name} Police"
    county_wide_police_rate = None
    county_wide_fire_title = f"{county_name} Fire"
    county_wide_fire_rate = None
    county_wide_ems_title = f"{county_name} EMS"
    county_wide_ems_rate = None
    cities = {
        1: belmont(),
        2: bessemer(),
        3: cherryville(),
        4: cramerton(),
        5: dallas(),
        6: gastonia(),
        7: high_shls(),
        8: kings_mtn(),
        9: lowell(),
        10: mcadenville(),
        11: mt_holly(),
        12: ranlo(),
        13: spencer_mtn(),
        14: stanly(),
    }
    county_fire_services = {
        1: {"AG Center Fire": 0.092},
        2: {"Alexis VFD": 0.079},
        3: {"Chapel Gr Fire": 0.093},
        4: {"Chestnut Ridge FD": 0.081},
        5: {"Commun. Fire": 0.099},
        6: {"Crouse Fire": 0.069},
        7: {"East Gast. Fire": 0.072},
        8: {"Hughs Pond FD": 0.1050},
        9: {"Long Shoals FD": 0.1040},
        10: {"Lowell FD": 0.068},
        11: {"Lucia Rb Fire": 0.093},
        12: {"New Hp Fire": 0.084},
        13: {"S. Gast. Fire": 0.093},
        14: {"S. Point Fire": 0.036},
        15: {"Tryonota Fire": 0.081},
        16: {"Union Rd Fire": 0.065},
        17: {"Waco Fire": 0.081},
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
    )

    return gaston


def belmont():
    """
    City Class
    """
    # INFORMATION
    city_name = "Belmont"
    city_rate = 0.515
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
    city_name = "Bessemer"
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
    city_name = "Cherryville"
    city_rate = 0.52
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
    city_name = "Cramerton"
    city_rate = 0.475
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
    city_name = "Dallas"
    city_rate = 0.4
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
    city_name = "Gastonia"
    city_rate = 0.52
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
    city_name = "High Shoals"
    city_rate = 0.38
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


def kings_mtn():
    """
    City Class
    """
    # INFORMATION
    city_name = "Kings Mtn"
    city_rate = 0.43
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
    city_name = "Lowell"
    city_rate = 0.43
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = 0.068
    fire_rate_title = f"{city_name} FD"

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
    city_name = "McAdenville"
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


def mt_holly():
    """
    City Class
    """
    # INFORMATION
    city_name = "Mt. Holly"
    city_rate = 0.485
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
    city_name = "Ranlo"
    city_rate = 0.4
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = 0.088
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
    fire_rate = 0.093
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
    city_name = "Stanley"
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
