from setuptools import setup
from Cython.Build import cythonize
from distutils.extension import Extension
import numpy

extensions = [
    Extension('cec2013', ['cec2013.pyx', 'cec13_test_func.cpp'],
              include_dirs=[numpy.get_include()],
              extra_compile_args=['-std=c++17'],
              language='c++'
              ),
]

setup(
    ext_modules=cythonize(extensions),
    extra_compile_args=['-w', '-O3', '-march=native'],
)
