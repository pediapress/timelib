#! /usr/bin/env py.test

import pytest
import timelib
from datetime import datetime


def test_bad_date():
    pytest.raises(ValueError, timelib.strtotime, "2007-09-27PM EDT")


def test_epoch():
    d = timelib.strtotime("1970-01-01")
    assert d == 0, "epoch should be 0"


def test_epoch_plus_one():
    d = timelib.strtodatetime("1970-01-01 00:00:01")
    assert d == datetime(1970, 1, 1, 0, 0, 1), "DateTime should be 1970-01-01 00:00:01"
