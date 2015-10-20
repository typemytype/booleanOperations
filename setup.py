from distutils.core import setup
from distutils.extension import Extension
from distutils.command.sdist import sdist as _sdist
import os


# see README.md for an explanation of the 'dev' file
dev_mode = os.path.exists('dev')

if dev_mode:
    from Cython.Distutils import build_ext
    from Cython.Build import cythonize

    print('Development mode: Compiling Cython modules from .pyx sources.')

    sources = ["cppWrapper/pyClipper.pyx", "cppWrapper/clipper.cpp"]

    class sdist(_sdist):
        """ Run 'cythonize' on *.pyx sources to ensure the .cpp files included
        in the source distribution are up-to-date.
        """
        def run(self):
            cythonize([s for s in sources if s.endswith('.pyx')], language='c++')
            _sdist.run(self)

    # use custom 'build_ext' and 'sdist' distutils commands
    cmdclass = {'build_ext': build_ext, 'sdist': sdist}

else:
    from distutils.command.build_ext import build_ext

    print('Distribution mode: Compiling from Cython-generated .cpp sources.')

    # use the pre-converted .cpp sources
    sources = ["cppWrapper/pyClipper.cpp", "cppWrapper/clipper.cpp"]
    cmdclass = {}

ext_module = Extension(
    "booleanOperations.pyClipper",
    sources=sources,
    depends=["cppWrapper/clipper.hpp"],
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
    cmdclass=cmdclass,
)
