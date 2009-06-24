#! /usr/bin/env python

try:
    from setuptools import setup, Extension    
    extra = dict(zip_safe=False)
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension
    extra = dict()
    
sources = "astro.c dow.c parse_date.c parse_tz.c timelib.c tm2unixtime.c unixtime2tm.c".split()
sources = ["ext-date-lib/"+x for x in sources]
sources.append("timelib.c")

setup(name='timelib',
      version='0.2',
      description="parse english textual date descriptions",
      author='Ralf Schmitt',
      author_email='schmir@gmail.com',
      url="http://github.com/schmir/timelib/tree/master",
      ext_modules=[Extension("timelib", sources=sources)],
      include_dirs=[".",  "ext-date-lib"],
      **extra
     )
