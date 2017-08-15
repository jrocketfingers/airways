from datetime import date

import pytest
from django.test import TestCase
from dateutil.relativedelta import relativedelta

from core.validators import over_18


class TestOver18Validator():
    """Groups test cases for the over_18 validator.
    """
    @pytest.mark.parametrize('years', [18, 19, 2000])
    def test_over_18(self, years):
        # GIVEN a date that was over 18 years ago
        date_obj = date.today() - relativedelta(years=years)

        # WHEN the validator is called
        result = over_18(date_obj)

        # THEN it should confirm the date was 18 years ago
        assert result == True

    @pytest.mark.parametrize('years', [17, 1, 0, -1])
    def test_under_18(self, years):
        # GIVEN a date that was under 18 years ago
        date_obj = date.today() - relativedelta(years=years)

        # WHEN the validator is called
        result = over_18(date_obj)

        # THEN it should confirm the date was 18 years ago
        assert result == False
