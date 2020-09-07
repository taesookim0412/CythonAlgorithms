from setuptools import setup
from Cython.Build import cythonize
setup(
    name='add int',
    ext_modules=cythonize("add_int.pyx"),
    zip_safe=False,
)
