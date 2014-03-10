#!/usr/bin/env python

from setuptools import setup
from glob import glob
from readgood import readgood_version
import sys

__author__ = "Daniel McDonald"
__copyright__ = "Copyright 2014"
__credits__ = ["Daniel McDonald"]
__license__ = "BSD"
__version__ = readgood_version.mmm
__maintainer__ = "Daniel McDonald"
__email__ = "mcdonadt@colorado.edu"

try:
    import bipy
except ImportError:
    raise ImportError("readgood requires bipy!")

# PyPI's list of classifiers can be found here:
# https://pypi.python.org/pypi?%3Aaction=list_classifiers
classes = """
    Development Status :: 4 - Beta
    License :: OSI Approved :: BSD License
    Topic :: Multimedia :: Graphics :: Presentation
    Programming Language :: Python
    Programming Language :: Python :: 2.7
    Programming Language :: Python :: Implementation :: CPython
    Operating System :: OS Independent
    Operating System :: POSIX
    Operating System :: POSIX :: Linux
    Operating System :: MacOS :: MacOS X
"""
classifiers = [s.strip() for s in classes.split('\n') if s]

# Verify Python version
ver = '.'.join(map(str, [sys.version_info.major, sys.version_info.minor]))
if ver not in ['2.7']:
    sys.stderr.write("Only Python >=2.7 and <3.0 is supported.")
    sys.exit(1)

long_description = """A speedreader inspired by Spritz and Optimal Recognition Point"""

setup(name='readgood',
      version=__version__,
      license=__license__,
      description='readgood',
      long_description=long_description,
      author=__maintainer__,
      author_email=__email__,
      maintainer=__maintainer__,
      maintainer_email=__email__,
      url='https://github.com/wasade/readgood',
      packages=['readgood'],
      scripts=glob('scripts/readgood*'),
      install_requires=["pyqi == 0.3.1"], # bipy is not pip installable yet
      classifiers=classifiers
      )
