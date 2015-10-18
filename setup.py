from distutils.core import setup
from distutils.extension import Extension
import os

# see "A note on setup.py" in README.md for an explanation of the dev file
dev_mode = os.path.exists('dev')

if dev_mode:
    from Cython.Distutils import build_ext
    print('Development mode: Compiling Cython modules from .pyx sources.')
    source_ext = '.pyx'
else:
    from distutils.command.build_ext import build_ext
    print('Distribution mode: Compiling Cython generated .cpp sources.')
    source_ext = '.cpp'

ext_module = Extension(
    "booleanOperations.pyClipper",
    sources=[
        "cppWrapper/pyclipper" + source_ext,
        "cppWrapper/clipper.cpp"
        ],
    depends=[
        "cppWrapper/clipper.hpp",
        ],
    language='c++',
)

setup(
    name="booleanOperations",
    version="0.1",
    description="Boolean operations on paths.",
    author="Frederik Berlaen",
    author_email="frederik@typemytype.com",
    url="https://github.com/typemytype/booleanOperations",
    license="MIT",
    packages=["booleanOperations"],
    package_dir={"": "Lib"},
    ext_modules=[ext_module],
    cmdclass={'build_ext': build_ext},
)
