import os
from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    long_description = readme.read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="PathCORE",
    version="1.0.0",
    packages=["pathcore"],
    include_package_data=True,
    license="LICENSE",
    description="Python 3 implementation of PathCORE analysis methods",
    long_description=long_description,
    url="https://github.com/greenelab/PathCORE",
    author="Greene Lab",
    author_email="team@greenelab.com",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    install_requires=["crosstalk-correction", "numpy", "pandas",
                      "scipy", "statsmodels"],
)
