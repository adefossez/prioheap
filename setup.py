#!/usr/bin/env python3
# Inspired from https://github.com/kennethreitz/setup.py

from pathlib import Path

from setuptools import setup

NAME = 'prioheap'
DESCRIPTION = 'Priority queue with a sane API'
URL = 'https://github.com/adefossez/prioheap'
EMAIL = 'alexandre.defossez@gmail.com'
AUTHOR = 'Alexandre Défossez'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = "0.0.2"

HERE = Path(__file__).parent

REQUIRED = []

try:
    with open(HERE / "README.md", encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    py_modules=['prioheap'],
    install_requires=REQUIRED,
    include_package_data=True,
    license='Unlicense license',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Topic :: Scientific/Engineering'
    ],
)
