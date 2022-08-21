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
    county_wide_rate = 0.0083
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
        1: {"AG Center Fire": 0.00092},
        2: {"Alexis VFD": 0.00079},
        3: {"Chapel Gr Fire": 0.00093},
        4: {"Chestnut Ridge FD": 0.00081},
        5: {"Commun. Fire": 0.00099},
        6: {"Crouse Fire": 0.00069},
        7: {"East Gast. Fire": 0.00072},
        8: {"Hughs Pond FD": 0.001050},
        9: {"Long Shoals FD": 0.001040},
        10: {"Lowell FD": 0.00068},
        11: {"Lucia Rb Fire": 0.00093},
        12: {"New Hp Fire": 0.00084},
        13: {"S. Gast. Fire": 0.00093},
        14: {"S. Point Fire": 0.00036},
        15: {"Tryonota Fire": 0.00081},
        16: {"Union Rd Fire": 0.00065},
        17: {"Waco Fire": 0.00081},
    }

    special_stuff = [None,county_fire_services]

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
    city_rate = 0.00515
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
    city_rate = 0.0045
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
    city_rate = 0.0052
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
    city_rate = 0.00475
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
    city_rate = 0.004
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
    city_rate = 0.0052
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
    city_rate = 0.0038
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


def kings_mtn():
    """
        City Class
    """
    # INFORMATION
    city_name = "Kings Mtn"
    city_rate = 0.0043
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
    city_rate = 0.0043
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = 0.00068
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
    city_rate = 0.0033
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
    city_rate = 0.00485
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
    city_rate = 0.004
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = 0.00088
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
    fire_rate = 0.00093
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
    city_rate = 0.0054
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
