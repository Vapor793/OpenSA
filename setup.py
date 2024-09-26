from setuptools import setup, find_packages

setup(
    name = "OpenSA",
    version = "0.1",
    install_requires=[
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