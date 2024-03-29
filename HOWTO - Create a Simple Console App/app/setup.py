# -*- coding: utf-8 -*-

import os

from setuptools import find_packages
from setuptools import setup

base_dir = os.path.dirname(__file__)

setup(
    name='ConsoleApp',
    version='0.1.0',
    description='Simple Python Console App',
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
            'app = app.__main__:main',
        ]
    },
    packages=find_packages(include=['app', 'app.*']),
    install_requires=[
        'pytest==7.3.1',
        'jinja2==3.1.2',
    ]
)
