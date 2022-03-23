from urllib.parse import urljoin
from feedgen.feed import FeedGenerator

def format_itunes_duration(td):
    return "{hours:02d}:{minutes:02d}:{seconds:02d}".format(
        hours=td.seconds//3600,
        minutes=(td.seconds//60)%60,
        seconds=int(td.seconds%60)
    )

def add_entry(fg, md):
    fe = fg.add_entry()
    fe.id(md.id)
    fe.title(md.title)
    fe.enclosure(md.link, str(md.length), "audio/mpeg")
    if md.duration is not None:
        fe.podcast.itunes_duration(format_itunes_duration(md.duration))

def generate_feed(channel_dict, output_file, file_metadatas):
    fg = FeedGenerator()
    fg.load_extension("podcast")
    feed_url = urljoin(channel_dict["base_url"], output_file)
    fg.link(href=feed_url, rel="self")
    fg.title(channel_dict["title"])
    fg.description(channel_dict["description"])

    for file_metadata in reversed(file_metadatas):
        add_entry(fg, file_metadata)

    return fg.rss_str(pretty=True)
