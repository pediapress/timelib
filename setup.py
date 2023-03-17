#! /usr/bin/env python

from distutils import sysconfig

from Cython.Build import cythonize
from setuptools import setup, Extension

if sysconfig.get_config_var("LIBM") == "-lm":
    libraries = ["m"]
else:
    libraries = []

extensions = [
    Extension(
        "timelib",
        sources=[
            "ext-date-lib/astro.c",
            "ext-date-lib/dow.c",
            "ext-date-lib/parse_date.c",
            "ext-date-lib/parse_tz.c",
            "ext-date-lib/timelib.c",
            "ext-date-lib/tm2unixtime.c",
            "ext-date-lib/unixtime2tm.c",
            "timelib.pyx",
        ],
        libraries=libraries,
        include_dirs=[".", "ext-date-lib"],
        define_macros=[("HAVE_STRING_H", 1)],
    )
]

setup(
    name="timelib",
    version="0.3.0",
    description="parse english textual date descriptions",
    author="Ralf Schmitt",
    author_email="ralf@systemexit.de",
    url="https://github.com/pediapress/timelib/",
    ext_modules=cythonize(extensions, gdb_debug=True, compiler_directives=dict(language_level=3)),
    include_dirs=[".", "ext-date-lib"],
    long_description=open("README.rst").read(),
    license="zlib/php",
)
