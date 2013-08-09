#coding: utf8

import csv
from StringIO import StringIO

import boundaries
import requests

# @see Command#handle in boundaries/management/commands/loadshapefiles.py
boundaries.autodiscover('.')
all_sources = boundaries.registry

no_geographic_code = [
  # Montreal boroughs
  u"Ahuntsic-Cartierville districts",
  u"Anjou districts",
  u"Côte-des-Neiges—Notre-Dame-de-Grâce districts",
  u"L'Île-Bizard—Sainte-Geneviève districts",
  u"Lachine districts",
  u"LaSalle districts",
  u"Le Plateau-Mont-Royal districts",
  u"Le Sud-Ouest districts",
  u"Mercier—Hochelaga-Maisonneuve districts",
  u"Montréal-Nord districts",
  u"Outremont districts",
  u"Pierrefonds-Roxboro districts",
  u"Rivière-des-Prairies—Pointe-aux-Trembles districts",
  u"Rosemont—La Petite-Patrie districts",
  u"Saint-Laurent districts",
  u"Saint-Léonard districts",
  u"Verdun districts",
  u"Ville-Marie districts",
  u"Villeray—Saint-Michel—Parc-Extension districts",
  # Provinces
  u"Alberta electoral districts",
  u"British Columbia electoral districts",
  u"Manitoba electoral districts",
  u"New Brunswick electoral districts",
  u"Newfoundland and Labrador electoral districts",
  u"Nova Scotia electoral districts",
  u"Prince Edward Island electoral districts",
  u"Québec electoral districts",
  u"Saskatchewan electoral districts",
  # Federal
  u"Census divisions",
  u"Census subdivisions",
  u"Federal electoral districts",
]

# Read the spreadsheet for tracking progress on data collection.
url = 'https://docs.google.com/spreadsheet/pub?key=0AtzgYYy0ZABtdGpJdVBrbWtUaEV0THNUd2JIZ1JqM2c&single=true&gid=18&output=csv'
reader = csv.reader(StringIO(requests.get(url).content))
reader.next()
subdivisions = {}
for row in reader:
  subdivisions[row[0]] = row[1:]

# Make sure the spreadsheet doesn't undercount.
for slug, config in all_sources.items():
  geographic_code = config.get('geographic_code')
  if geographic_code:
    subdivision = subdivisions.get(config['geographic_code'])
    if subdivision:
      if subdivision[16] != 'Y':
        print "Change 'Shapefile?' for %s (%s) from '%s' to 'Y'" % (slug, geographic_code, subdivision[16])
    else:
      print "%s (%s) isn't in the spreadsheet" % (slug, geographic_code)
  elif slug not in no_geographic_code:
    print "%s doesn't have a geographic code" % slug
