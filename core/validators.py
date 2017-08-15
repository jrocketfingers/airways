"""Set of utility functions used for validation."""
from datetime import date
from dateutil.relativedelta import relativedelta


def over_18(value: date):
    """Returns whether a date was at least 18 years ago.

    :param value: To-be-validated date.
    :returns bool: Wheter or not the date was 18 years ago.
    """
    delta = relativedelta(date.today(), value)
    age = delta.years

    return age >= 18
