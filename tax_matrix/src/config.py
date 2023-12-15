"""
General CONFIGURATION information
"""


def current_version():
    var = "2.1.4-alpha"
    return var


def date_revised():
    var = "12.15.2023"
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
