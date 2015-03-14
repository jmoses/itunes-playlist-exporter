#!/usr/bin/env python

import sys, os, os.path, re, shutil

playlist = sys.argv[1]
target_root = sys.argv[2]

rows = 0
with open(playlist) as play:
    contents = play.read()
    for entry in re.sub('\x00', '', contents).split("\r"):
        if rows == 0:
            rows = 1
            continue
        
        if not entry:
            continue

        fields = entry.split("\t")

        location = os.path.join('/Volumes', re.sub(':', '/', fields[26].strip()))

        if os.path.exists(location):
            print "Found %s" % location

            rest, filename = os.path.split(location)
            album = fields[3]
            artist = fields[1]

            print "%s - %s - %s" % (artist, album, os.path.basename(location))

            alb_root = os.path.join(target_root, artist, album)
            if not os.path.exists(alb_root):
                os.makedirs(alb_root)

            if not os.path.exists(os.path.join(alb_root, filename)):
                shutil.copy(location, os.path.join(alb_root, filename))
        
