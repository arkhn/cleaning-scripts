import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


requirements = read("requirements.txt").split()

setup(
    name="cleaning-scripts",
    version="0.2.5",
    author="Arkhn",
    author_email="contact@arkhn.org",
    description="Python scripts used in the FHIR integration pipeline "
    "to clean input data for different external sources.",
    url="https://github.com/arkhn/cleaning-scripts",
    license="Apache License 2.0",
    packages=find_packages(exclude=["api*", "test*"]),
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    install_requires=requirements,
)
