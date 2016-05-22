from pathlib import Path
from os import path

from dircast.files import load_channel_file, find_files, FileMetadata

HERE = Path(path.abspath(path.dirname(__file__)))

def test_find_channel_file():
    expected = {
        "title": "All About Everything",
        "description": "A show about everything",
        "url": "http://www.example.com/podcasts/everything/index.html",
        }
    assert expected == load_channel_file(Path(HERE) / "test_data" / "0")

def test_find_mp3_files():
    files = find_files(Path(HERE) / "test_data" / "0")
    expected = FileMetadata(
        id="7a37534b4994869e96552561449b2f5b9ddd985e",
        title="Some silence",
        link="1-some-silence.mp3",
        author_name="Unknown author",
        author_email="unknown@example.com"
    )
    assert files[0] == expected
