from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "requirements.txt"), "r") as f:
    install_requires = f.read().splitlines()

classifiers=[
    "Development Status :: 3 - Alpha",
    "Environment :: Console",
    # ? "Intended Audience :: End Users/Desktop",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Programming Language :: Python",#? not sure what lowest working v is
    "Topic :: Multimedia :: Sound/Audio",
    ]

setup(
    name="dircast",
    version="0.0",
    desciption=" Create a podcast RSS feed for a directory of audio files",
    url="https://github.com/calpaterson/dircast",
    maintainer="Cal Paterson",
    license="GPL",
    classifiers=classifiers,
    keywords="podcast rss feed",
    packages=find_packages(),
    include_package_data=True,
    scripts=[
    ],
    install_requires=install_requires,
    entry_points={
        "console_scripts": "dircast = dircast.cli:main"
    }
)
