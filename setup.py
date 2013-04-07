#!/bin/env python
# -*- coding: utf8 -*-

from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

version = "0.1.0"

setup(
    name="predestinate",
    version=version,
    description="Python wrapper around xautomation because Python is disco super-fly",
    classifiers=[
        "Programming Language :: Python :: 3.3",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: Unix",
    ],
    keywords="xautomation wrapper X",
    author="David Gay",
    author_email="oddshocks@riseup.net",
    url="https://github.com/oddshocks/predestinate",
    license="GPLv3+",
    packages=find_packages(
    ),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "",
    ],
    #TODO: Deal with entry_points
    #entry_points="""
    #[console_scripts]
    #pythong = pythong.util:parse_args
    #"""
)