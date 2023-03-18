#! /usr/bin/env py.test

import pytest
import timelib
from datetime import datetime, timedelta


def test_bad_date():
    pytest.raises(ValueError, timelib.strtotime, "2007-09-27PM EDT")


def test_epoch():
    d = timelib.strtotime("1970-01-01")
    assert d == 0, "epoch should be 0"


def test_epoch_plus_one():
    d = timelib.strtodatetime("1970-01-01 00:00:01")
    assert d == datetime(1970, 1, 1, 0, 0, 1), "DateTime should be 1970-01-01 00:00:01"


def test_today():
    d = timelib.strtodatetime("today")
    assert d == datetime.utcnow().replace(
        hour=0, minute=0, second=0, microsecond=0
    ), "DateTime should be today"


def test_next_friday():
    d = timelib.strtodatetime("next friday")
    today = datetime.today()
    days_to_friday = (4 - today.weekday()) % 7
    days_to_friday = 7 if days_to_friday == 0 else days_to_friday
    next_friday = today + timedelta(days=days_to_friday)
    next_friday = next_friday.replace(hour=0, minute=0, second=0, microsecond=0)
    assert d == next_friday, "DateTime should be next friday"
