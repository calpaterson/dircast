import math
from logging import getLogger
import hashlib
from datetime import timedelta

import magic
import yaml
import mutagen


AUDIO_MIMETYPES = {"audio/mpeg", "audio/mp4", "video/mp4"}


class FileMetadata(object):
    def __init__(self, id, title, link, mimetype):
        self.id = id
        self.title = title
        self.link = link
        self.mimetype = mimetype
        self.length = 0
        self.duration = None

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)


def guess_mimetype(path):
    magic_mimetype = magic.from_file(str(path), mime=True)
    if magic_mimetype == "audio/x-m4a":
        return "audio/mp4"
    else:
        return magic_mimetype


def load_channel_file(path):
    path = str(path / "channel.yml")
    getLogger(__name__).info("loading %s", path)
    with open(path) as channel_file:
        return {
            key.lstrip(":"): value
            for key, value in yaml.safe_load(channel_file).items()
        }


def get_file_metadata(channel_url, mimetype, path):
    tag_info = mutagen.File(str(path), easy=True)
    try:
        title = tag_info["title"][0]
    except KeyError:
        title = path.name
    md = FileMetadata(
        id=hashlib.sha1(title.encode()).hexdigest(),
        title=title,
        link="".join([
            channel_url,
            str(path.relative_to(path, path.parents[0])),
        ]),
        mimetype=mimetype
    )
    md.length = path.stat().st_size
    md.duration = timedelta(seconds=round(tag_info.info.length))
    return md


def find_files(channel_url, path):
    files = []
    for child in sorted(path.iterdir()):
        getLogger(__name__).info("checking %s", child)
        mimetype = guess_mimetype(child)
        is_audio = mimetype in AUDIO_MIMETYPES
        getLogger(__name__).info(
            "%s is of type %s - %s",
            child,
            mimetype,
            "is audio" if is_audio else "not audio"
        )

        if is_audio:
            files.append(get_file_metadata(channel_url, mimetype, child))
    return files
