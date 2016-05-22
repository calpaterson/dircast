from feedgen.feed import FeedGenerator

def add_entry(fg, md):
    fe = fg.add_entry()
    fe.id(md.id)
    fe.title(md.title)
    fe.enclosure(md.link, str(md.length), "audio/mpeg")

def generate_feed(channel_dict, file_metadatas):
    fg = FeedGenerator()
    fg.load_extension("podcast")
    fg.link(href=channel_dict["url"], rel="self")
    fg.title(channel_dict["title"])
    fg.description(channel_dict["description"])

    for file_metadata in file_metadatas:
        add_entry(fg, file_metadata)

    return fg.rss_str(pretty=True)
