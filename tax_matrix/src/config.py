"""
General CONFIGURATION information
"""


def current_version():
    var = "2.1.0"
    return var


def date_revised():
    var = "10.28.2022"
    return var


def description():
    var = f"Revised as of: {date_revised()} | Statement Generator for CLT-Surrounding Tax Districts"
    return var


def long_description():
    var = f"Revised as of: {date_revised()} | A tax matrix calculator for form-filling purposes that will generate a statement estimating taxes for a property based on it's specified tax rates"
    return var


def dependencies():
    var = [
        "art",
        "colorama",
        "debugpy",
    ]
    return var
