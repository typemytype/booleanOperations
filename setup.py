# We require setuptools >= 18.0 so that we can resolve Cython dependency via
# 'setup_requires':
# https://bitbucket.org/pypa/setuptools/commits/424966904023#chg-CHANGES.txt

no_setuptools_msg = ('Setuptools >= 18.0 is required.\n'
                     'Get it from: https://pypi.python.org/pypi/setuptools')
try:
    import pkg_resources
except ImportError:
    print(no_setuptools_msg)
    exit(1)

try:
    pkg_resources.require("setuptools >= 18.0")
except pkg_resources.ResolutionError:
    print(no_setuptools_msg)
    exit(1)

from setuptools import setup, Extension
import os

# this is the latest version available from PyPI as of 18 December 2015
cython = 'cython >= 0.23.4'

# If the Cython-generated files are absent, add Cython to 'setup_requires'
if not os.path.exists("cppWrapper/pyClipper.cpp"):
    requirements = [cython]
    cython_is_required = True
else:
    requirements = []
    cython_is_required = False

# check if the required Cython version is already installed on the system
try:
    pkg_resources.require(cython)
except pkg_resources.ResolutionError:
    cython_is_installed = False
else:
    cython_is_installed = True

if cython_is_installed or cython_is_required:
    print('Development mode: Compiling Cython modules from .pyx sources.')
    sources = ["cppWrapper/pyClipper.pyx"]

    from setuptools.command.sdist import sdist as _sdist

    class sdist(_sdist):
        """ Run 'cythonize' on *.pyx sources to ensure the .cpp files included
        in the source distribution are up-to-date.
        """
        def run(self):
            from Cython.Build import cythonize
            cythonize([s for s in sources if s.endswith('.pyx')],
                      language='c++')
            _sdist.run(self)

    cmdclass = {'sdist': sdist}

else:
    print('Distribution mode: Compiling from Cython-generated .cpp sources.')
    sources = ["cppWrapper/pyClipper.cpp"]
    cmdclass = {}

ext_module = Extension(
    "booleanOperations.pyClipper",
    sources=sources + ["cppWrapper/clipper.cpp"],
    depends=["cppWrapper/clipper.hpp"],
    language='c++',
)

setup(
    name="booleanOperations",
    version="0.2",
    description="Boolean operations on paths.",
    author="Frederik Berlaen",
    author_email="frederik@typemytype.com",
    url="https://github.com/typemytype/booleanOperations",
    license="MIT",
    packages=["booleanOperations"],
    package_dir={"": "Lib"},
    setup_requires=requirements,
    ext_modules=[ext_module],
    cmdclass=cmdclass,
)
