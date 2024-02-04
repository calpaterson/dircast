from logging import getLogger
import hashlib
from datetime import timedelta, datetime, timezone

import yaml
import mutagen


STANDARDISED_MIMETYPES = {"audio/mpeg", "audio/mp4"}


class FileMetadata(object):
    def __init__(self, id, title, link, mimetype, published):
        self.id = id
        self.title = title
        self.link = link
        self.mimetype = mimetype
        self.length = 0
        self.duration = None
        self.published = published

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self.__eq__(other)


def guess_mimetype(path):
    mutagen_f = mutagen.File(path)
    if mutagen_f is None:
        return None
    mimes = set(mutagen_f.mime)
    getLogger(__name__).debug("mutagen got %s for %s", mimes, path)

    # first match against the standards - mutagen returns multiple mimetypes
    # for mp3 and mp4 and we want to use a specific one for compatibility
    standardised_mimes = mimes.intersection(STANDARDISED_MIMETYPES)
    if len(standardised_mimes) > 0:
        return next(iter(standardised_mimes))

    # otherwise (eg it's some other audio format) return the first 'audio/*' mimetype
    for mime in mimes:
        if mime.startswith("audio/"):
            return mime

    # else it's not audio
    else:
        return None


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
    link = "".join([channel_url, str(path)])
    mtime = path.stat().st_mtime
    md = FileMetadata(
        id=hashlib.sha1(title.encode()).hexdigest(),
        title=title,
        link=link,
        mimetype=mimetype,
        published=datetime.fromtimestamp(mtime, timezone.utc),
    )
    md.length = path.stat().st_size
    md.duration = timedelta(seconds=round(tag_info.info.length))
    return md


def find_files(channel_url, path):
    files = []
    for child in sorted(path.iterdir()):
        getLogger(__name__).info("checking %s", child)
        mimetype = guess_mimetype(child)
        is_audio = mimetype is not None
        getLogger(__name__).info(
            "%s is of type %s - %s",
            child,
            mimetype,
            "is audio" if is_audio else "not audio",
        )

        if is_audio:
            files.append(get_file_metadata(channel_url, mimetype, child))
    return files
