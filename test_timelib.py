#! /usr/bin/env py.test

import py, timelib


def test_bad_date():
    py.test.raises(ValueError, timelib.strtotime, "2007-09-27PM EDT")


def test_epoch():
    d = timelib.strtotime("1970-01-01")
    assert d == 0, "epoch should be 0"
