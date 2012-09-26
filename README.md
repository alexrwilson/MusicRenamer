MusicRenamer
============

Renames music to have a leading track number for dumb USB MP3 players that don't read ID tags properly.

Currently only looks at MP3 files, since this is the only format I have found players for that experience this problem.

Uses [Mutagen](http://code.google.com/p/mutagen/) 1.20 for tag retrieval.


#Usage

To run, you need Python 2 (developed against 2.7.3 on Linux), and the Mutagen audio metadata library.

The easiest way to set up dependencies is using [pip](http://www.pip-installer.org)

```console
pip install mutagen
```

Alternatively, you can get a release from the (Mutagen site)[http://code.google.com/p/mutagen/downloads/list] for manual installation.

Once installed, running renamer.py through a python interpreter with the path to the root directory as an argument should cause all MP3 files to be renamed with a leading track title.

