#! /usr/bin/env python

import os

try:
    from setuptools import setup, Extension
    extra = dict(zip_safe=False)
except ImportError:
    from distutils.core import setup
    from distutils.extension import Extension
    extra = dict()

from distutils import sysconfig
if sysconfig.get_config_var("LIBM") == "-lm":
    libraries = ["m"]
else:
    libraries = []


def read_long_description():
    fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.rst")
    return open(fn).read()

sources = "astro.c dow.c parse_date.c parse_tz.c timelib.c tm2unixtime.c unixtime2tm.c".split()
sources = ["ext-date-lib/" + x for x in sources]
sources.append("timelib.c")

if not os.path.exists("timelib.c"):
    os.system("cython timelib.pyx")

setup(name='timelib',
      version='0.2.3',
      description="parse english textual date descriptions",
      author='Ralf Schmitt',
      author_email='ralf@systemexit.de',
      url="https://github.com/pediapress/timelib/",
      ext_modules=[Extension("timelib", sources=sources,
                             libraries=libraries,
                             define_macros=[('HAVE_STRING_H', 1)])],
      include_dirs=[".",  "ext-date-lib"],
      long_description=read_long_description(),
      license="zlib/php",
      **extra)
