from setuptools import setup, find_packages
import sys

needs_pytest = {'pytest', 'test'}.intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []
needs_wheel = {'bdist_wheel'}.intersection(sys.argv)
wheel = ['wheel'] if needs_wheel else []

with open('README.md', 'r') as f:
    long_description = f.read()

setup_params = dict(
    name="booleanOperations",
    use_scm_version=True,
    description="Boolean operations on paths.",
    long_description=long_description,
    author="Frederik Berlaen",
    author_email="frederik@typemytype.com",
    url="https://github.com/typemytype/booleanOperations",
    license="MIT",
    package_dir={"": "Lib"},
    packages=find_packages("Lib"),
    setup_requires=[
        "setuptools_scm>=1.11.1",
    ] + pytest_runner + wheel,
    tests_require=[
        'pytest>=3.0.2',
    ],
    install_requires=[
        "pyclipper>=1.0.5",
        # TODO(anthrotype): un-comment these once they are on PyPI.
        # In the meantime, pip install -r requirements.txt
        # "fonttools>=3.1",
        # "ufoLib>=1.2",
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Graphics :: Editors :: Vector-Based',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

if __name__ == "__main__":
    setup(**setup_params)
