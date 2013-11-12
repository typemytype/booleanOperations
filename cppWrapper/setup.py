from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

# requires cython --> http://cython.org
# python setup.py build_ext --inplace
 
ext =	Extension("pyClipper", 
                sources=["pyClipper.pyx", "clipper.cpp"],
                language="c++",              # this causes Cython to create C++ source
				include_dirs=["include"],
				)

setup(
        ext_modules=[ext],
        cmdclass = {'build_ext': build_ext},
)