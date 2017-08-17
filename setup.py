# coding: utf-8

from __future__ import absolute_import

from os import path
from setuptools import setup, find_packages
from codecs import open as fopen
fread = lambda name, encoding="utf-8": fopen(name, "r", encoding).read()

top_dir = path.dirname(path.abspath(__file__))

with open(path.join(top_dir, "annotate", "__about__.py")) as f:
    class about: exec(f.read(), None)

setup(
    name             = about.__title__,
    version          = about.__version__,
    description      = about.__summary__,
    url              = about.__uri__,
    download_url     = about.__uri__,

    author           = about.__author__,
    author_email     = about.__email__,
    maintainer       = about.__author__,
    maintainer_email = about.__email__,
    license          = about.__license__,
    long_description = (fread(path.join(top_dir, "README.rst")) + "\n" +
                        fread(path.join(top_dir, "CHANGES.rst"))),

    platforms        = ["any"],
    packages         = ["annotate"],
    scripts          = [],
    provides         = ["annotate"],
    entry_points     = {},
    requires         = [],
    include_package_data = True,
    zip_safe         = True,
    test_suite       = "tests",

    python_requires  = ">=2.6.0",
    setup_requires   = ["setuptools>=24.2.1"],
    install_requires = ["setuptools>=24.2.1"],

    keywords    = ["annotate", "decorator"],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: zlib/libpng License",
        "Operating System :: OS Independent",
        "Natural Language :: Polish",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: Implementation :: Stackless",
        "Programming Language :: Python :: Implementation :: IronPython",
        "Programming Language :: Python :: Implementation :: Jython",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)

# eof
