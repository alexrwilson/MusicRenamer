#!/usr/bin/python

import fnmatch
import os
import argparse

parser = argparse.ArgumentParser(description='Renames MP3 files to prepend trach numbers.')
parser.add_argument("dir", help="directory to search for music files")

args = parser.parse_args()


def add_track_number(filename):
	print "Adding Track number to ", filename


rootdir = '/'
for root, subFolders, files in os.walk(args.dir):
	for file in files:
		if fnmatch.fnmatch(file, '*py'):
			add_track_number(os.path.join(root, file))