from ..utilities import InputHelper
from ..utilities import LogicalWork
from ..utilities import classes
from ..utilities import Printer

from .mecklenburg import main as mecklenburg


def load_all_counties():
    classes.Counties.add_county(mecklenburg())
    # classes.Counties.add_county("""COUNTY_FUNCTION""")
    # classes.Counties.add_county("""COUNTY_FUNCTION""")
    # classes.Counties.add_county("""COUNTY_FUNCTION""")
    # classes.Counties.add_county("""COUNTY_FUNCTION""")
    # classes.Counties.add_county("""COUNTY_FUNCTION""")
    # classes.Counties.add_county("""COUNTY_FUNCTION""")
