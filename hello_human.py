from setuptools import setup
from Cython.Build import cythonize
setup(
    name='Hello human app',
    ext_modules=cythonize("hello_human.pyx"),
    zip_safe=False,
)
