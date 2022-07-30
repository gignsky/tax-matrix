from ..utilities import InputHelper
from ..utilities import LogicalWork
from ..utilities import classes
from ..utilities import Printer

from .mecklenburg import main as mecklenburg


def load_all_counties(which_run):
    if which_run == "inital":
        pass
    elif which_run == "reload":
        classes.Counties.reset_counties()

    classes.Counties.add_county(mecklenburg())
    # classes.Counties.add_county("""COUNTY_FUNCTION""")
    # classes.Counties.add_county("""COUNTY_FUNCTION""")
    # classes.Counties.add_county("""COUNTY_FUNCTION""")
    # classes.Counties.add_county("""COUNTY_FUNCTION""")
    # classes.Counties.add_county("""COUNTY_FUNCTION""")
    # classes.Counties.add_county("""COUNTY_FUNCTION""")
