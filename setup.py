#! /usr/bin/env python

from distutils.core import setup
from distutils.extension import Extension

sources = "astro.c dow.c parse_date.c parse_tz.c timelib.c tm2unixtime.c unixtime2tm.c".split()
sources = ["ext-date-lib/"+x for x in sources]
sources.append("timelib.c")

setup(name='timelib',
      version='0.1',
      description="Parse about any English textual datetime description",
      author='Ralf Schmitt',
      author_email='schmir@gmail.com',
      url="http://github.com/schmir/timelib/tree/master",
      ext_modules=[Extension("timelib", sources=sources)],
      include_dirs=[".",  "ext-date-lib"], 
     )
