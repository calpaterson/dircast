from feedgen.feed import FeedGenerator

def generate_feed(channel_dict, mutagen_files):
    fg = FeedGenerator()
    fg.load_extension("podcast")
    fg.link(href=channel_dict["url"], rel="self")
    fg.title(channel_dict["title"])
    fg.description(channel_dict["description"])

    return fg.rss_str(pretty=True)
