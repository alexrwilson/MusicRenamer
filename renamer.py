#!/usr/bin/python

import fnmatch
import os
import argparse
import re
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

parser = argparse.ArgumentParser(description='Renames MP3 files to prepend trach numbers.')
parser.add_argument("dir", help="directory to search for music files")

args = parser.parse_args()

track_number_pattern = re.compile('\d+')

def add_track_number(full_filename, filename):
	audio_file = MP3(full_filename, ID3=EasyID3)
	raw_track_number_string = audio_file["tracknumber"][0]


	match = track_number_pattern.match(raw_track_number_string)
	if match:
		track_number = match.group()
		current_track_number_pattern = re.compile('0*' + track_number) # Needs some work
		filename_match = current_track_number_pattern.match(filename)
		if not filename_match:
			processed_filename = track_number.zfill(3) + " - " + filename
			processed_full_filename = full_filename.replace(filename, processed_filename)
			os.rename(full_filename, processed_full_filename)
	else:
		print"WARN: No track number found for ", full_filename

if __name__ == '__main__':
	for root, subFolders, files in os.walk(args.dir):
		for file in files:
			if fnmatch.fnmatch(file, '*mp3'):
				#print root
				add_track_number(os.path.join(root, file), file)





