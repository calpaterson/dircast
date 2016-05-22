from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "requirements.txt"), "r") as f:
    install_requires = f.read().splitlines()

setup(
    name="dircast",
    version="0.0",
    maintainer="Cal Paterson",
    packages=find_packages(),
    include_package_data=True,
    scripts=[
    ],
    install_requires=install_requires,
    entry_points={
        "console_scripts": "dircast = dircast.cli:main"
    }
)
