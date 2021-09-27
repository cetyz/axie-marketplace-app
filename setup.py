# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 00:49:11 2021

@author: Charles
"""

from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)