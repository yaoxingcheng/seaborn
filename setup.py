#! /usr/bin/env python
#
# Copyright (C) 2012-2019 Michael Waskom

DESCRIPTION = "seaborn: statistical data visualization"
LONG_DESCRIPTION = """\
Seaborn is a library for making statistical graphics in Python. It is built on top of `matplotlib <https://matplotlib.org/>`_ and closely integrated with `pandas <https://pandas.pydata.org/>`_ data structures.

Here is some of the functionality that seaborn offers:

- A dataset-oriented API for examining relationships between multiple variables
- Specialized support for using categorical variables to show observations or aggregate statistics
- Options for visualizing univariate or bivariate distributions and for comparing them between subsets of data
- Automatic estimation and plotting of linear regression models for different kinds dependent variables
- Convenient views onto the overall structure of complex datasets
- High-level abstractions for structuring multi-plot grids that let you easily build complex visualizations
- Concise control over matplotlib figure styling with several built-in themes
- Tools for choosing color palettes that faithfully reveal patterns in your data

Seaborn aims to make visualization a central part of exploring and understanding data. Its dataset-oriented plotting functions operate on dataframes and arrays containing whole datasets and internally perform the necessary semantic mapping and statistical aggregation to produce informative plots.
"""

DISTNAME = 'seaborn'
MAINTAINER = 'Michael Waskom'
MAINTAINER_EMAIL = 'mwaskom@nyu.edu'
URL = 'https://seaborn.pydata.org'
LICENSE = 'BSD (3-clause)'
DOWNLOAD_URL = 'https://github.com/mwaskom/seaborn/'
VERSION = '0.9.1.dev'

INSTALL_REQUIRES = [
    'numpy>=1.9.3',
    'scipy>=0.14.0',
    'pandas>=0.15.2',
    'matplotlib==3.0.1',
]

PACKAGES = [
    'seaborn',
    'seaborn.colors',
    'seaborn.external',
    'seaborn.tests',
]

CLASSIFIERS = [
    'Intended Audience :: Science/Research',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'License :: OSI Approved :: BSD License',
    'Topic :: Scientific/Engineering :: Visualization',
    'Topic :: Multimedia :: Graphics',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Operating System :: MacOS'
]

try:
    from setuptools import setup
    _has_setuptools = True
except ImportError:
    from distutils.core import setup

if __name__ == "__main__":

    setup(
        name=DISTNAME,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        license=LICENSE,
        url=URL,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        install_requires=INSTALL_REQUIRES,
        packages=PACKAGES,
        classifiers=CLASSIFIERS
    )
