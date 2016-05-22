Dircast - create a podcast RSS feed for a directory of audio files
------------------------------------------------------------------

Dircast is a tool to create a podcast RSS feed for a directory of audio files.

Dircast is inspired by other projects that do the same thing (especially
[dropcaster](https://github.com/nerab/dropcaster)) but dircast supports file
formats other than mp3.

Usage
=====

First create a `channel.yml` file in the same directory as your audio files:

```
---
title: All About Everything
description: A show about everything
url: http://www.mywebsite.com/everything-podcast/
```

The `url` part should be where you will host your podcast.

Then (in the same directory) use it like this:

```
dircast . > index.rss
```

Dircast will automatically look for audio files and add them to the RSS feed.
It will use any tags present in the audio files to set file metadata.

Supported file formats
======================

- mp3 (*.mp3)
- mp4 (*.aac, *.mp4, *.m4a)

Titles and RSS "unique ids"
===========================

Dircast will look for a title tag to determine the title of your files.  If it
doesn't find one it will use the filename as the title.

Whichever is chosen the title's SHA1 checksum will be the "unique id" of that
podcast entry.  If you change the title tag (or, if you didn't have a title
tag, if you rename the file) the unique id will change and podcast software
might get confused.

Range queries
=============

Make sure that the HTTP server you are serving from supports
[range requests](https://en.wikipedia.org/wiki/Byte_serving) - otherwise most
podcast software will not be able to seek through the audio.  Most proper
webservers like nginx or apache will do this but simple ones (like the one in
the Python standard library) won't.

Licence
=======

Dircast is licensed under GPLv3.  See the file [LICENCE](LICENCE) for details.
