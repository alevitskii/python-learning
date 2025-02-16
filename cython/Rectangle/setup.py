# Build: `python setup.py build_ext --inplace`

from Cython.Build import cythonize
from setuptools import setup

setup(ext_modules=cythonize("rect.pyx"))
