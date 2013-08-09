#coding: utf8

import csv
from datetime import date, timedelta
from StringIO import StringIO

import boundaries
import requests

# @see Command#handle in boundaries/management/commands/loadshapefiles.py
boundaries.autodiscover('.')
all_sources = boundaries.registry

# Read the spreadsheet for tracking progress on data collection.
url = 'https://docs.google.com/spreadsheet/pub?key=0AtzgYYy0ZABtdGpJdVBrbWtUaEV0THNUd2JIZ1JqM2c&single=true&gid=18&output=csv'
reader = csv.reader(StringIO(requests.get(url).content))
reader.next()
subdivisions = {}
for row in reader:
  subdivisions[row[0]] = row[1:]

for slug, config in all_sources.items():
  notes = []
  if config.get('notes'):
    notes.append("Notes: %s" % config['notes'])
  geographic_code = config.get('geographic_code')
  if geographic_code:
    subdivision = subdivisions.get(config['geographic_code'])
    if subdivision:
      if subdivision[19]:
        notes.append("Online notes: %s" % subdivision[19])
      if subdivision[20]:
        notes.append("Revisions: %s" % subdivision[20])
  if notes:
    print slug
    if config.get('source_url'):
      print "Source: %s" % config['source_url']
    for note in notes:
      print note
    print
