from pathlib import Path
from os import path

import pytest

from dircast.files import load_channel_file

HERE = Path(path.abspath(path.dirname(__file__)))

def test_find_channel_file():
    expected = {
        "title": "All About Everything",
        "description": "A show about everything",
        "url": "http://www.example.com/podcasts/everything/index.html",
        }
    assert expected == load_channel_file(Path(HERE) / "test_data" / "0")

@pytest.mark.xfail(reason="test not implemented")
def test_find_files_with_mp3():
    assert False
