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

    return counties
