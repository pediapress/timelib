#! /usr/bin/env py.test

import timelib
import py

def test_bad_date():
    py.test.raises(ValueError, timelib.strtotime,  "2007-09-27PM EDT")
