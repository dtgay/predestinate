#!/bin/env python
# -*- coding: utf8 -*-

from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

version = "0.1.2"

setup(
    name="predestinate",
    version=version,
    description="Script mouse and keyboard actions via xautomation in GNU/Linux",
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: Unix",
    ],
    keywords="xautomation wrapper X mouse keyboard scripting",
    author="David Gay",
    author_email="oddshocks@riseup.net",
    url="https://github.com/oddshocks/predestinate",
    license="GPLv3+",
    packages=find_packages(
    ),
    scripts=[
            "distribute_setup.py",
            ],
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
