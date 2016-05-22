from logging import getLogger

import yaml


def load_channel_file(path):
    path = str(path / "channel.yml")
    getLogger(__name__).info("loading %s", path)
    with open(path) as channel_file:
        return {
            key.lstrip(":"): value
            for key, value in yaml.safe_load(channel_file).items()
        }


def find_files(path):
    for child in path.iterdir():
        getLogger(__name__).info("checking %s", child)
        yield child
