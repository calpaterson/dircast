from logging import basicConfig, INFO, ERROR, getLogger
from pathlib import Path
from sys import stderr, stdout, exit

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
    if not channel_dict["base_url"].endswith("/"):
        getLogger(__name__).error("base_url should end with a /")
        exit(1)
    feed = generate_feed(
        channel_dict,
        output_file,
        find_files(channel_dict["base_url"], Path(directory)))
    with open(output_file, "wb") as output_f:
        output_f.write(feed)
