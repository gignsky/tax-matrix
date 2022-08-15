"""
    gaston co rates document
"""

from . import cls
from . import InputHelper
from . import InputTesters
from . import Printer
from . import classes


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
    special_stuff = True
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

    gaston = Gaston(
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
        county_fire_services,
    )

    return gaston


def belmont():
    # INFORMATION
    city_name = "Belmont"
    city_rate = 0.00515
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    city = classes.City(
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
    # INFORMATION
    city_name = "Bessemer"
    city_rate = 0.0045
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    city = classes.City(
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
    # INFORMATION
    city_name = "Cherryville"
    city_rate = 0.0052
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    city = classes.City(
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
    # INFORMATION
    city_name = "Cramerton"
    city_rate = 0.00475
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    city = classes.City(
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
    # INFORMATION
    city_name = "Dallas"
    city_rate = 0.004
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    city = classes.City(
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
    # INFORMATION
    city_name = "Gastonia"
    city_rate = 0.0052
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    city = classes.City(
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
    # INFORMATION
    city_name = "High Shoals"
    city_rate = 0.0038
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = 0.00104
    fire_rate_title = f"{city_name} Fire"

    city = classes.City(
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
    # INFORMATION
    city_name = "Kings Mtn"
    city_rate = 0.0043
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    city = classes.City(
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
    # INFORMATION
    city_name = "Lowell"
    city_rate = 0.0043
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = 0.00068
    fire_rate_title = f"{city_name} FD"

    city = classes.City(
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
    # INFORMATION
    city_name = "McAdenville"
    city_rate = 0.0033
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    city = classes.City(
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
    # INFORMATION
    city_name = "Mt. Holly"
    city_rate = 0.00485
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    city = classes.City(
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
    # INFORMATION
    city_name = "Ranlo"
    city_rate = 0.004
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = 0.00088
    fire_rate_title = f"{city_name} Fire"

    city = classes.City(
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
    # INFORMATION
    city_name = "Spencer Mtn"
    city_rate = 0
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = 0.00093
    fire_rate_title = f"{city_name} Fire"

    city = classes.City(
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
    # INFORMATION
    city_name = "Stanley"
    city_rate = 0.0054
    city_rate_title = city_name
    police_rate = None
    police_rate_title = f"{city_name} Police"
    fire_rate = None
    fire_rate_title = f"{city_name} Fire"

    city = classes.City(
        city_name,
        city_rate,
        city_rate_title,
        police_rate,
        police_rate_title,
        fire_rate,
        fire_rate_title,
    )

    return city


class Gaston(classes.County):
    """
    Gaston county specific class

    Args:
        classes (class): generic county class
    """
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
        self.special_fire_department_default_str=None

    def select_special_options(self):
        """
        select_special_options options for all county fire departments to be added
        """

        input_loop = True

        while input_loop:

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
            input_loop = False

    def select_fire_department(self, include):
        """
        which_modify helps to determine if one should modify the values available options on the County services

        SPECIFIC TO GASTON COUNTY
        """

        mod_loop = True

        while mod_loop:
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

                    mod_loop = False

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

        self.generate_special_current_default_strs()

        # print gaston co specific info
        Printer.print_yellow(self.special_fire_department_default_str)

    def generate_special_current_default_strs(self):
        """
        generate_SPECIAL_current_default_strs
        """
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
