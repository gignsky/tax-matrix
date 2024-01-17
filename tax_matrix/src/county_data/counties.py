import os
import yaml

def get_counties():
    """
    Retrieve a dictionary of counties and their corresponding data from YAML files in the current directory.

    Returns:
        dict: A dictionary where the keys are county names and the values are the data associated with each county.
    """
    county_files_dir = os.path.dirname(__file__)
    counties = {}

    for filename in os.listdir(county_files_dir):
        if filename.endswith(".yml"):
            filepath = os.path.join(county_files_dir, filename)
            with open(filepath, "r") as file:
                data = yaml.safe_load(file)
                county_name = data.get("county_name")
                if county_name:
                    counties[county_name] = data

    counties=simplify_county_data(counties)

    return counties

def simplify_county_data(counties):
    """
    Simplify the county data by removing titles and rates when the rate is null.

    Args:
        counties (dict): A dictionary where the keys are county names and the values are the data associated with each county.

    Returns:
        dict: A simplified dictionary where the keys are county names and the values are the simplified data associated with each county.
    """
    simplified_counties = {}

    for county_name, county_data in counties.items():
        simplified_county_data=null_parser(county_data)

        simplified_counties[county_name] = simplified_county_data

    return simplified_counties

def null_parser(dictionary):
    """
    Recursively parses a dictionary and removes any key-value pairs where the value is None.
    If a key contains the word 'rate' and its value is None, the entire dictionary is returned as None.

    Args:
        dictionary (dict): The dictionary to be parsed.

    Returns:
        dict or None: The parsed dictionary with None values removed, or None if a 'rate' key has a value of None.
    """
    simplified_data = {}
    keys_to_delete = []

    for key, value in dictionary.items():
        if isinstance(value, dict):
            value = null_parser(value)
        if "rate" in key and value is None:
            return None
        simplified_data[key] = value

    for key in simplified_data.keys():
        if simplified_data[key] is None:
            keys_to_delete.append(key)

    for key in keys_to_delete:
        del simplified_data[key]

    return simplified_data
