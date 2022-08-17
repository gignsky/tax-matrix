"""
    ALL ITEMS CLASSES
"""

class Counties:
    """
    countains list of all counties class refernce variables

    ***NOTE: contains only "Class Methods"
    """

    ALL_COUNTIES = []

    @classmethod
    def add_county(cls, county_class):
        """
        add_county add county object to list

        Args:
            county_class (object): county object
        """
        cls.ALL_COUNTIES.append(county_class)

    @classmethod
    def get_all_counties(cls):
        """
        get_all_counties returns all counties in a list

        Returns:
            list: objects for all counties
        """
        return cls.ALL_COUNTIES

    @classmethod
    def reset_counties(cls):
        """
        reset_counties resets counties in selection to an empty list in preperation for a reload of all counties
        """
        cls.ALL_COUNTIES = []


class Cities:
    """
    countains list of all counties class refernce variables
    """

    def __init__(self, county):
        self.all_cities = []
        self.county = county

    def add_city(self, city_class):
        """
        add_city add city to all city list

        Args:
            city_class (list): list of all cities in a county
        """
        self.all_cities.append(city_class)

    def get_all_cities(self):
        """
        get_all_cities returns all cities in county

        Returns:
            list: list of city objects for specific county
        """
        return self.all_cities
