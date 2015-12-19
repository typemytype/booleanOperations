from __future__ import print_function
import sys
import os

try:
    import pkg_resources
except ImportError:
    print("Setuptools is required.\n"
          "Get it from: https://pypi.python.org/pypi/setuptools")
    exit(1)


def is_installed(requirement):
    try:
        pkg_resources.require(requirement)
    except pkg_resources.ResolutionError:
        return False
    else:
        return True

# this is the latest version available from PyPI as of 18 December 2015
cython_req = 'cython >= 0.23.4'

# Resolving Cython dependency via 'setup_requires' requires setuptools >= 18.0:
# https://bitbucket.org/pypa/setuptools/commits/424966904023#chg-CHANGES.txt
setuptools_req = "setuptools >= 18.0"

requirements = []
# If the Cython-generated files are absent, and the required Cython isn't
# installed, add Cython to 'setup_requires'.
if not os.path.exists("cppWrapper/pyClipper.cpp"):
    if not is_installed(cython_req):
        if not is_installed(setuptools_req):
            import textwrap
            print(textwrap.dedent("""
                Cython >= 0.23.4 is required, and the dependency cannot be
                automatically resolved with the version of setuptools that is
                currently installed (%s).
                
                You can install/upgrade Cython using pip:
                $ pip install -U cython

                Alternatively, you can upgrade setuptools:
                $ pip install -U setuptools
                """ % pkg_resources.get_distribution("setuptools").version),
                file=sys.stderr)
            exit(1)
        requirements.append(cython_req)

from setuptools import setup, Extension

if is_installed(cython_req) or cython_req in requirements:
    print('Development mode: Compiling Cython modules from .pyx sources.')
    sources = ["cppWrapper/pyClipper.pyx"]

    from setuptools.command.sdist import sdist as _sdist

    class sdist(_sdist):
        """ Run 'cythonize' on *.pyx sources to ensure the .cpp files included
        in the source distribution are up-to-date.
        """
        def run(self):
            from Cython.Build import cythonize
            cythonize(sources, language='c++')
            _sdist.run(self)

    cmdclass = {'sdist': sdist}
    if is_installed(cython_req):
        from Cython.Distutils import build_ext
        cmdclass['build_ext'] = build_ext

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
