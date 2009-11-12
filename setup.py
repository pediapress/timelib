#! /usr/bin/env python
import os

try:
    from setuptools import setup, Extension    
    extra = dict(zip_safe=False)
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension
    extra = dict()
    
def read_long_description():
    fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.txt")
    return open(fn).read()
    
sources = "astro.c dow.c parse_date.c parse_tz.c timelib.c tm2unixtime.c unixtime2tm.c".split()
sources = ["ext-date-lib/"+x for x in sources]
sources.append("timelib.c")

setup(name='timelib',
      version='0.2.1',
      description="parse english textual date descriptions",
      author='Ralf Schmitt',
      author_email='schmir@gmail.com',
      url="http://github.com/schmir/timelib/tree/master",
      ext_modules=[Extension("timelib", sources=sources)],
      include_dirs=[".",  "ext-date-lib"],
      long_description=read_long_description(),
      license="zlib/php",
      **extra
     )
