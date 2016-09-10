from setuptools import setup
import re

version = ''
with open('Lib/booleanOperations/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)
if not version:
    raise RuntimeError('Cannot find version information')

setup(
    name="booleanOperations",
    version=version,
    description="Boolean operations on paths.",
    author="Frederik Berlaen",
    author_email="frederik@typemytype.com",
    url="https://github.com/typemytype/booleanOperations",
    license="MIT",
    packages=["booleanOperations"],
    package_dir={"": "Lib"},
    install_requires="pyclipper >= 1.0.1",
)
