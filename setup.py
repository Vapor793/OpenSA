import OpenSA
from setuptools import setup, find_packages

DISTNAME = 'OpenSA'
DESCRIPTION = 'OpenSA'
VERSION = OpenSA.__version__

setup(
    name = DISTNAME,
    version = VERSION,
    packages = find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'pandas',
        'scikit-learn',
        'deap',
        ],
    author = "SYF",
    author_email = "",
    description = DESCRIPTION,
)