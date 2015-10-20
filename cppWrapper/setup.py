from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

# requires cython --> http://cython.org
# python setup.py build_ext --inplace
 
ext = Extension(
	"pyClipper", 
	sources=["pyClipper.pyx", "clipper.cpp"],
	language="c++",  # this causes Cython to create C++ source
	depends=["clipper.hpp"],
)

setup(
	name="pyClipper",
	version="4.8.5",
	description="Python binding for the Clipper library of Angus Johnson",
	url="https://sites.google.com/site/maxelsbackyard/home/pyclipper",
	
	ext_modules=[ext],
	cmdclass = {"build_ext": build_ext}
)