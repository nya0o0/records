#!/usr/bin/env python

"""
Call `pip install -e .` to install package locally for testing.
"""

from setuptools import setup

# build command
setup(
    name="records",
    version="0.0.1",
    author="Selina Chen",
    author_email="yc4635@columbia.edu",
    description="A package for getting data from GBIF API",
    classifiers=["Programming Language :: Python :: 3"],
)