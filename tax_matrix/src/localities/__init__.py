from .. import cls
from ..utilities import InputHelper
from ..utilities import InputTesters
from ..utilities import LogicalWork
from ..utilities import classes
from ..utilities import Printer

from .mecklenburg import main as mecklenburg


from .iredell import main as iredell

from .gaston import main as gaston


def load_all_counties(which_run):
    if which_run == "inital":
        pass
    elif which_run == "reload":
        classes.Counties.reset_counties()

    classes.Counties.add_county(mecklenburg())
    # classes.Counties.add_county(union())
    # classes.Counties.add_county(stanly())
    # classes.Counties.add_county(cabarrus())
    classes.Counties.add_county(iredell())
    # classes.Counties.add_county(rowan())
    classes.Counties.add_county(gaston())
    # classes.Counties.add_county(lancaster())
    # classes.Counties.add_county(york())
