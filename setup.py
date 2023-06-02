# -*- coding: utf-8 -*-

import os

from setuptools import find_packages
from setuptools import setup

base_dir = os.path.dirname(__file__)

setup(
    name='DemoApp',
    version='0.1.0',
    description='Simple Python CLI App',
    author='Markus Schneider',
    author_email='markus.schneider73@gmail.com',
    setup_requires='setuptools',
    license='Copyright 2023 Markus Schneider',
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
   entry_points={
        'console_scripts': [
            'demoapp = src.main:main',
        ]
    },
    packages=find_packages(),
    package_data={"template": ["*.j2"]},
    install_requires=[
        'pytest==7.3.1',
        'jinja2==3.1.2',
    ]
)
