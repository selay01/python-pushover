#!/usr/bin/env python

from setuptools import setup

setup(
    name="python-pushover",
    version="1.0",
    description="Comprehensive bindings and command line utility for the "
    "Pushover notification service",
    long_description=open("README.rst").read()
    + "\n"
    + open("AUTHORS.rst").read()
    + "\n"
    + open("CHANGES.rst").read(),
    url="https://github.com/Thibauth/python-pushover",
    author="Thibaut Horel",
    author_email="thibaut.horel+pushover@gmail.com",
    py_modules=["pushover", "pushover_cli"],
    entry_points={"console_scripts": ["pushover = pushover_cli:main"]},
    install_requires=["requests>=1.0"],
    use_2to3=True,
    license="GNU GPLv3",
)
