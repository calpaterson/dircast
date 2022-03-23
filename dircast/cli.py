from logging import basicConfig, INFO, ERROR, getLogger
from pathlib import Path
from sys import stderr, stdout

import click

from dircast.files import load_channel_file, find_files
from dircast.feed import generate_feed

@click.command()
@click.argument(
    "directory",
    type=click.Path(exists=True, file_okay=False, writable=True),
)
@click.option("--debug", is_flag=True, default=False, type=click.BOOL)
@click.argument("output_file", default="index.rss", type=click.Path(dir_okay=False, writable=True))
def main(directory, debug, output_file):
    basicConfig(level=INFO if debug else ERROR, stream=stderr)
    getLogger(__name__).info("started")
    channel_dict = load_channel_file(Path(directory))
    stdout.buffer.write(
        generate_feed(
            channel_dict,
            output_file,
            find_files(channel_dict["url"], Path(directory)))
    )
