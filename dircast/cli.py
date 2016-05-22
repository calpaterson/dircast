from logging import basicConfig, INFO, ERROR, getLogger
from pathlib import Path
from sys import stderr

import click

from dircast.files import load_channel_file, find_files

@click.command()
@click.argument(
    "directory",
)
@click.option("--debug", is_flag=True, default=False, type=bool)
def main(directory, debug):
    basicConfig(level=INFO if debug else ERROR, steam=stderr)
    getLogger(__name__).info("started")
    load_channel_file(Path(directory))
    for file in find_files(Path(directory)):
        pass
