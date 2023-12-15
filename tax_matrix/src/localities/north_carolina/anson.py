"""
    anson co rates document
"""


from . import general_classes


def main():
    """
    main contents of anson county

    Returns:
        obj: county object
    """
    # INFORMATION:
    county_name = "Anson Co., NC"
    county_wide_rate_title = "Anson County Unincorporated Tax Rate"
    county_wide_rate = 0.777
    county_wide_police_title = f"{county_name} Police"
    county_wide_police_rate = None
    county_wide_fire_title = f"{county_name} Fire"
    county_wide_fire_rate = None
    county_wide_ems_title = f"{county_name} EMS"
    county_wide_ems_rate = None
    tax_rates_year = 2019
    cities = {
        1: ansonville(),
        2: lilesvile(),
        3: mcfarlan(),
        4: morven(),
        5: peachland(),
        6: polkton(),
        7: wadesboro(),
    }

    county_fire_services = {
        1: {"Ansonville Fire District": 0.096},
        2: {"Burnsville Fire District": 0.096},
        3: {"Gulledge Fire District": 0.096},
        4: {"Lanesboro Fire District": 0.096},
        5: {"Lilesville Fire District": 0.096},
        6: {"Morven Fire District": 0.096},
        7: {"Wadesboro Fire District": 0.096},
    }

    special_stuff = [None, county_fire_services]

    anson = general_classes.County(
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

    return anson


def ansonville():
    """
    City Class
    """
    # INFORMATION
    city_name = "Ansonville"
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


def lilesvile():
    """
    City Class
    """
    # INFORMATION
    city_name = "Lilesvile"
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


def mcfarlan():
    """
    City Class
    """
    # INFORMATION
    city_name = "McFarlan"
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


def morven():
    """
    City Class
    """
    # INFORMATION
    city_name = "Morven"
    city_rate = 0.47
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


def peachland():
    """
    City Class
    """
    # INFORMATION
    city_name = "Peachland City"
    city_rate = 0.3
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


def polkton():
    """
    City Class
    """
    # INFORMATION
    city_name = "Polkton"
    city_rate = 0.27
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


def wadesboro():
    """
    City Class
    """
    # INFORMATION
    city_name = "Wadesboro"
    city_rate = 0.556
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
