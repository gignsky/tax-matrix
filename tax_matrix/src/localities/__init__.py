"""
    localities general rates
"""

from .. import cls
from .. import general_classes
from .. import special_classes
from .. import county_classes

from ..utilities import InputHelper
from ..utilities import InputTesters
from ..utilities import LogicalWork
from ..utilities import Printer

from . import north_carolina

from . import south_carolina

# from .lancaster import main as lancaster
# from .york import main as york


def load_all_counties(which_run):
    """
    load_all_counties Initalizes all counties or reinitalizeses based on argument

    Args:
        which_run (str): inital or reload based on desired effect
    """

    if which_run == "inital":
        pass
    elif which_run == "reload":
        general_classes.Counties.reset_counties()

    general_classes.Counties.add_county(north_carolina.mecklenburg())
    general_classes.Counties.add_county(north_carolina.union())
    general_classes.Counties.add_county(north_carolina.stanly())
    general_classes.Counties.add_county(north_carolina.cabarrus())
    general_classes.Counties.add_county(north_carolina.iredell())
    general_classes.Counties.add_county(north_carolina.rowan())
    general_classes.Counties.add_county(north_carolina.gaston())
    general_classes.Counties.add_county(south_carolina.lancaster())
    # general_classes.Counties.add_county(south_carolina.york())
