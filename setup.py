from setuptools import setup, find_packages

setup(
    name = "OpenSA",
    version = "0.1",
    requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'pandas',
        'scikit-learn'
        ],
    packages = find_packages(),
    author = "SYF",
    author_email = "",
    description = "OpenSA",
)