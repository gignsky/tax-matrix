"""
   iredell co rates document
"""

from . import classes


def main():
    # INFORMATION:
    COUNTY_NAME = "Iredell Co., NC"
    COUNTY_WIDE_RATE_TITLE = "Iredell County Unincorporated Tax Rate"
    COUNTY_WIDE_RATE = 0.005375
    COUNTY_WIDE_POLICE_TITLE = f"{COUNTY_NAME} Police"
    COUNTY_WIDE_POLICE_RATE = None
    COUNTY_WIDE_FIRE_TITLE = f"{COUNTY_NAME} Fire"
    COUNTY_WIDE_FIRE_RATE = 0.0009
    COUNTY_WIDE_EMS_TITLE = f"{COUNTY_NAME} EMS"
    COUNTY_WIDE_EMS_RATE = None
    CITIES = {
        1: statesville_city(),
        2: statesville_downtown(),
        3: woods_municipal_ser(),
        4: troutman(),
        5: harmony(),
        6: mooresville_town(),
        7: mooresville_downtown(),
        8: mooresville_school(),
        9: love_valley(),
        10: davidson_town(),
    }
    SPECIAL_STUFF = None

    iredell = classes.County(
        COUNTY_NAME,
        COUNTY_WIDE_RATE_TITLE,
        COUNTY_WIDE_RATE,
        COUNTY_WIDE_POLICE_TITLE,
        COUNTY_WIDE_POLICE_RATE,
        COUNTY_WIDE_FIRE_TITLE,
        COUNTY_WIDE_FIRE_RATE,
        COUNTY_WIDE_EMS_TITLE,
        COUNTY_WIDE_EMS_RATE,
        CITIES,
        SPECIAL_STUFF,
    )

    return iredell


def statesville_city():
    # INFORMATION
    CITY_NAME = "Statesville City"
    CITY_RATE = 0.005478
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = None
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = None
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    city = classes.City(
        CITY_NAME,
        CITY_RATE,
        CITY_RATE_TITLE,
        POLICE_RATE,
        POLICE_RATE_TITLE,
        FIRE_RATE,
        FIRE_RATE_TITLE,
    )

    return city


def statesville_downtown():
    # INFORMATION
    CITY_NAME = "Statesville Downtown"
    CITY_RATE = 0.001
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = None
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = None
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    city = classes.City(
        CITY_NAME,
        CITY_RATE,
        CITY_RATE_TITLE,
        POLICE_RATE,
        POLICE_RATE_TITLE,
        FIRE_RATE,
        FIRE_RATE_TITLE,
    )

    return city


def woods_municipal_ser():
    # INFORMATION
    CITY_NAME = "Woods Municipal Ser."
    CITY_RATE = 0.0021
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = None
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = None
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    city = classes.City(
        CITY_NAME,
        CITY_RATE,
        CITY_RATE_TITLE,
        POLICE_RATE,
        POLICE_RATE_TITLE,
        FIRE_RATE,
        FIRE_RATE_TITLE,
    )

    return city


def troutman():
    # INFORMATION
    CITY_NAME = "Troutman"
    CITY_RATE = 0.0052
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = None
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = None
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    city = classes.City(
        CITY_NAME,
        CITY_RATE,
        CITY_RATE_TITLE,
        POLICE_RATE,
        POLICE_RATE_TITLE,
        FIRE_RATE,
        FIRE_RATE_TITLE,
    )

    return city


def harmony():
    # INFORMATION
    CITY_NAME = "Harmony"
    CITY_RATE = 0.0012
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = None
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = None
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    city = classes.City(
        CITY_NAME,
        CITY_RATE,
        CITY_RATE_TITLE,
        POLICE_RATE,
        POLICE_RATE_TITLE,
        FIRE_RATE,
        FIRE_RATE_TITLE,
    )

    return city


def mooresville_town():
    # INFORMATION
    CITY_NAME = "Mooresville Town"
    CITY_RATE = 0.0058
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = None
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = None
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    city = classes.City(
        CITY_NAME,
        CITY_RATE,
        CITY_RATE_TITLE,
        POLICE_RATE,
        POLICE_RATE_TITLE,
        FIRE_RATE,
        FIRE_RATE_TITLE,
    )

    return city


def mooresville_downtown():
    # INFORMATION
    CITY_NAME = "Mooresville Downtown"
    CITY_RATE = 0.0016
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = None
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = None
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    city = classes.City(
        CITY_NAME,
        CITY_RATE,
        CITY_RATE_TITLE,
        POLICE_RATE,
        POLICE_RATE_TITLE,
        FIRE_RATE,
        FIRE_RATE_TITLE,
    )

    return city


def mooresville_school():
    # INFORMATION
    CITY_NAME = "Mooresville School"
    CITY_RATE = 0.00185
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = None
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = None
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    city = classes.City(
        CITY_NAME,
        CITY_RATE,
        CITY_RATE_TITLE,
        POLICE_RATE,
        POLICE_RATE_TITLE,
        FIRE_RATE,
        FIRE_RATE_TITLE,
    )

    return city


def love_valley():
    # INFORMATION
    CITY_NAME = "Love Valley"
    CITY_RATE = 0.0025
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = None
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = None
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    city = classes.City(
        CITY_NAME,
        CITY_RATE,
        CITY_RATE_TITLE,
        POLICE_RATE,
        POLICE_RATE_TITLE,
        FIRE_RATE,
        FIRE_RATE_TITLE,
    )

    return city


def davidson_town():
    # INFORMATION
    CITY_NAME = "Davidson Town"
    CITY_RATE = 0.0029
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = None
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = None
    FIRE_RATE_TITLE = f"{CITY_NAME} Fire"

    city = classes.City(
        CITY_NAME,
        CITY_RATE,
        CITY_RATE_TITLE,
        POLICE_RATE,
        POLICE_RATE_TITLE,
        FIRE_RATE,
        FIRE_RATE_TITLE,
    )

    return city
