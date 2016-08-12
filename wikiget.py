#!/usr/bin/python
#
# No rights reserved.
# Author: Aashray Arora <aashrayarora@gmail.com>
#
# Wikiget - get wiki entry summary on a particular entry.
# Version 1.0.0

import sys
import urllib2
import re

WIKI_BASE = "https://en.wikipedia.org/wiki/"

def main(search):
  search = search.replace(" ", "_")
  req = urllib2.Request(WIKI_BASE + search)
  try:
    resp = urllib2.urlopen(req)
    respData = resp.read()
    summary = re.findall(r'<p>(.*?)</p>',str(respData))
    print re.sub('<[^<]+?>', '', summary[0])
  except urllib2.HTTPError, error:
    if error.code == 404:
      print "Sorry, no such entry"
    else:
      print "Unknown error. Possible bug!"

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print "Usage: wikiget <name/place/thing>"
    sys.exit(0)
  main(str(sys.argv[1]))
