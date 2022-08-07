"""
    gaston co rates document
"""

from . import cls
from . import InputHelper
from . import InputTesters
from . import Printer
from . import classes


def main():
    # INFORMATION:
    COUNTY_NAME = "Gaston Co., NC"
    COUNTY_WIDE_RATE_TITLE = "Gaston County Unincorporated Tax Rate"
    COUNTY_WIDE_RATE = 0.0083
    COUNTY_WIDE_POLICE_TITLE = f"{COUNTY_NAME} Police"
    COUNTY_WIDE_POLICE_RATE = None
    COUNTY_WIDE_FIRE_TITLE = f"{COUNTY_NAME} Fire"
    COUNTY_WIDE_FIRE_RATE = None
    COUNTY_WIDE_EMS_TITLE = f"{COUNTY_NAME} EMS"
    COUNTY_WIDE_EMS_RATE = None
    CITIES = {
        1: belmont(),
        2: Bessemer(),
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
    SPECIAL_STUFF = True
    COUNTY_FIRE_SERVICES = {
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

    gaston = Gaston(
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
        COUNTY_FIRE_SERVICES,
    )

    return gaston


def belmont():
    # INFORMATION
    CITY_NAME = "Belmont"
    CITY_RATE = 0.00515
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


def Bessemer():
    # INFORMATION
    CITY_NAME = "Bessemer"
    CITY_RATE = 0.0045
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


def cherryville():
    # INFORMATION
    CITY_NAME = "Cherryville"
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


def cramerton():
    # INFORMATION
    CITY_NAME = "Cramerton"
    CITY_RATE = 0.00475
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


def dallas():
    # INFORMATION
    CITY_NAME = "Dallas"
    CITY_RATE = 0.004
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


def gastonia():
    # INFORMATION
    CITY_NAME = "Gastonia"
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


def high_shls():
    # INFORMATION
    CITY_NAME = "High Shoals"
    CITY_RATE = 0.0038
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = None
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = 0.00104
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


def kings_mtn():
    # INFORMATION
    CITY_NAME = "Kings Mtn"
    CITY_RATE = 0.0043
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


def lowell():
    # INFORMATION
    CITY_NAME = "Lowell"
    CITY_RATE = 0.0043
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = None
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = 0.00068
    FIRE_RATE_TITLE = f"{CITY_NAME} FD"

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


def mcadenville():
    # INFORMATION
    CITY_NAME = "McAdenville"
    CITY_RATE = 0.0033
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


def mt_holly():
    # INFORMATION
    CITY_NAME = "Mt. Holly"
    CITY_RATE = 0.00485
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


def ranlo():
    # INFORMATION
    CITY_NAME = "Ranlo"
    CITY_RATE = 0.004
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = None
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = 0.00088
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


def spencer_mtn():
    # INFORMATION
    CITY_NAME = "Spencer Mtn"
    CITY_RATE = 0
    CITY_RATE_TITLE = CITY_NAME
    POLICE_RATE = None
    POLICE_RATE_TITLE = f"{CITY_NAME} Police"
    FIRE_RATE = 0.00093
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


def stanly():
    # INFORMATION
    CITY_NAME = "Stanley"
    CITY_RATE = 0.0054
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


class Gaston(classes.County):
    def __init__(
        self,
        county_name,
        county_wide_rate_title,
        county_wide_rate,
        county_wide_police_title,
        county_wide_police_rate,
        county_wide_fire_title,
        county_wide_fire_rate,
        county_wide_ems_title,
        county_wide_ems_rate,
        all_cities,
        special_stuff,
        county_fire_services,
    ):
        super().__init__(
            county_name,
            county_wide_rate_title,
            county_wide_rate,
            county_wide_police_title,
            county_wide_police_rate,
            county_wide_fire_title,
            county_wide_fire_rate,
            county_wide_ems_title,
            county_wide_ems_rate,
            all_cities,
            special_stuff,
        )

        # initalize dict of all county fire rates
        self.county_fire_services = county_fire_services
        self.participating_fire_department_title = None
        self.participating_fire_department_rate = None

    def select_special_options(self):
        """
        select_special_options options for all county fire departments to be added
        """

        INPUT_LOOP = True

        while INPUT_LOOP:

            include = None
            while include is None:
                Printer.print_special_service_dict_with_single_option_and_quit_option(
                    self.county_fire_services, quit_option=False
                )

                include = InputHelper.choice_bool_with_header(
                    "Is the property subject to any of the above specific fire departments that are not attached to cities?"
                )

            cls()

            self.select_fire_department(include)
            Printer.short_liner()
            if self.participating_fire_department_rate is not None:
                Printer.print_green(
                    f"Added '{self.participating_fire_department_title} - {self.participating_fire_department_rate}' to statement"
                )
            else:
                Printer.print_yellow("NO general county Fire Department in statement")
            Printer.short_liner()
            INPUT_LOOP = False

    def select_fire_department(self, include):
        """
        which_modify helps to determine if one should modify the values available options on the County services

        SPECIFIC TO GASTON COUNTY
        """

        MOD_LOOP = True

        while MOD_LOOP:
            if include:
                Printer.print_special_service_dict_with_single_option_and_quit_option(
                    self.county_fire_services, quit_option=True
                )

                option = input(
                    "Please ENTER number associated with Fire Department the property is subject to: "
                )

            else:
                self.participating_fire_department_rate = None
                self.participating_fire_department_title = None
                break

            cls()

            option_int = InputTesters.verify_int(option)

            if option_int is 0:
                break
            else:
                selected_fire_dept_dict = InputTesters.verify_dict_selection(
                    option_int, self.county_fire_services
                )

                if selected_fire_dept_dict is not None:
                    # quit if zero otherwise continue
                    if option_int != 0:
                        title = list(selected_fire_dept_dict.keys())[0]
                        rate = selected_fire_dept_dict[title]

                        if self.participating_fire_department_rate is not None:
                            self.participating_fire_department_rate = None
                            self.participating_fire_department_title = None

                        self.participating_fire_department_rate = rate
                        self.participating_fire_department_title = title

                    MOD_LOOP = False

    def generate_county_statistics(self):
        super().generate_county_statistics()

        if self.participating_fire_department_rate is not None:
            self.county_statistics[
                self.participating_fire_department_title
            ] = self.participating_fire_department_rate
        else:
            pass

        return self.county_statistics

    def print_county_selected_info(self):
        super().print_county_selected_info()

        Printer.print_green(f"{self.get_county_name()} Specific Info")

        self.generate_SPECIAL_current_default_strs()

        # print gaston co specific info
        Printer.print_yellow(self.special_fire_department_default_str)

    def generate_SPECIAL_current_default_strs(self):
        current_fire_department = (
            self.participating_fire_department_rate
            if self.participating_fire_department_rate is not None
            else None
        )

        if current_fire_department is not None:
            current_fire_department = f"{current_fire_department:.6g}"
        else:
            current_fire_department = None

        if current_fire_department is not None:
            self.special_fire_department_default_str = f"Special Fire District for Gaston County: {self.participating_fire_department_title} - Rate: {current_fire_department}"
        else:
            self.special_fire_department_default_str = (
                "No Special Fire District Selected."
            )

    def get_special_options_title(self):
        return "Special Fire Departments"
