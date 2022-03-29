from os import path
from pathlib import Path

from lxml import etree

from dircast.files import load_channel_file, find_files
from dircast.feed import generate_feed

HERE = Path(path.abspath(path.dirname(__file__)))


def test_feed_with_no_files():
    channel_dict = load_channel_file(Path(HERE) / "test_data" / "0")
    feed = generate_feed(channel_dict, [])
    tree = etree.fromstring(feed)
    channel = tree.findall("channel")[0]
    assert channel.findall("title")[0].text == channel_dict["title"]
    assert channel.findall("description")[0].text == channel_dict["description"]
    assert channel.findall("link")[0].text == channel_dict["url"]


def test_feed_with_some_files():
    channel_dict = load_channel_file(Path(HERE) / "test_data" / "0")
    files = find_files("http://example.com", Path(HERE) / "test_data" / "0")
    feed = generate_feed(channel_dict, files)
    tree = etree.fromstring(feed)
    items = tree.findall("channel")[0].findall("item")
    expected_titles = ["Some silence", "More silence", "Even more silence"]
    assert expected_titles == [i.findall("title")[0].text for i in items]
