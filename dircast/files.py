from logging import getLogger
import mimetypes
import hashlib

import yaml
import mutagen


AUDIO_MIMETYPES = ["audio/mpeg"]


class FileMetadata(object):
    def __init__(self, id, title, link, mimetype):
        self.id = id
        self.title = title
        self.link = link
        self.mimetype = mimetype
        self.length = 0

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)


def load_channel_file(path):
    path = str(path / "channel.yml")
    getLogger(__name__).info("loading %s", path)
    with open(path) as channel_file:
        return {
            key.lstrip(":"): value
            for key, value in yaml.safe_load(channel_file).items()
        }


def get_file_metadata(channel_url, path):
    tag_info = mutagen.File(str(path), easy=True)
    md = FileMetadata(
        id=hashlib.sha1(tag_info["title"][0].encode("utf-8")).hexdigest(),
        title=tag_info["title"][0],
        link="".join([
            channel_url,
            str(path.relative_to(path, path.parents[0])),
        ]),
        mimetype="audio/mpeg"
    )
    md.length = path.stat().st_size
    return md


def find_files(channel_url, path):
    files = []
    for child in sorted(path.iterdir()):
        getLogger(__name__).info("checking %s", child)
        mimetype = mimetypes.guess_type(str(child))[0]
        is_audio = mimetype in AUDIO_MIMETYPES
        getLogger(__name__).info(
            "%s is of type %s - %s",
            child,
            mimetype,
            "is audio" if is_audio else "not audio"
        )

        if is_audio:
            files.append(get_file_metadata(channel_url, child))
    return files
