from logging import basicConfig, INFO, getLogger
from pathlib import Path

import click

from dircast.files import find_files

@click.command()
@click.argument(
    "directory",
)
def main(directory):
    basicConfig(level=INFO)
    getLogger(__name__).info("started")
    for file in find_files(Path(directory)):
        pass
