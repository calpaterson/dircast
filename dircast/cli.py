from logging import basicConfig, INFO, ERROR, getLogger
from pathlib import Path
from sys import stderr, stdout

import click

from dircast.files import load_channel_file
from dircast.feed import generate_feed

@click.command()
@click.argument(
    "directory",
)
@click.option("--debug", is_flag=True, default=False, type=bool)
def main(directory, debug):
    basicConfig(level=INFO if debug else ERROR, steam=stderr)
    getLogger(__name__).info("started")
    channel_dict = load_channel_file(Path(directory))
    stdout.buffer.write(generate_feed(channel_dict, []))
