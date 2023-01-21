from setuptools import setup
from Cython.Build import cythonize
from Cython.Distutils import Extension
import os.path

setup(
    name='main',
    ext_modules=cythonize(Extension("main", ["main.py"])),
    zip_safe=False,
)

