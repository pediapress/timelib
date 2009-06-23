
timelib is a short wrapper around php's internal timelib module.
It currently only provides a few functions:

timelib.strtodatetime:

>>> timelib.strtodatetime('today')
datetime.datetime(2009, 6, 23, 0, 0)
>>> timelib.strtodatetime('today')
datetime.datetime(2009, 6, 23, 0, 0)
>>> timelib.strtodatetime('next friday')
datetime.datetime(2009, 6, 26, 0, 0)
>>> timelib.strtodatetime('29 feb 2008 -108 years')
datetime.datetime(1900, 3, 1, 0, 0)

timelib.strtotime:

>>> import time, timelib
>>> time.ctime(timelib.strtotime("now"))
'Tue Jun 23 15:17:32 2009'
>>> time.ctime(timelib.strtotime("4 hours ago"))
'Tue Jun 23 11:17:38 2009'
>>> time.ctime(timelib.strtotime("20080229 -1 year"))
'Thu Mar  1 01:00:00 2007'

