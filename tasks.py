#coding: utf8

from ftplib import FTP
import os
import os.path
import re
from urlparse import urlparse

from invoke import run, task
import requests

# @see Command#handle in boundaries/management/commands/loadshapefiles.py
def registry(base='.'):
  import boundaries

  boundaries.autodiscover(base)
  return boundaries.registry

# Reads the spreadsheet for tracking progress on data collection.
def csv():
  import csv
  from StringIO import StringIO

  url = 'https://docs.google.com/spreadsheet/pub?key=0AtzgYYy0ZABtdGpJdVBrbWtUaEV0THNUd2JIZ1JqM2c&single=true&gid=18&output=csv'
  reader = csv.reader(StringIO(requests.get(url).content))
  reader.next()
  return dict((row[0], row[1:]) for row in reader)

# Check that all `definition.py` files are valid.
@task
def definitions(base='.'):
  valid_keys = set([
    # Added by boundaries.register.
    'file',
    # Used by represent-boundaries.
    'singular',
    'domain',
    'last_updated',
    'slug_func',
    'name_func',
    'id_func',
    'is_valid_func',
    'authority',
    'source_url',
    'licence_url',
    'data_url',
    'notes',
    'encoding',
    # Used by this script.
    'geographic_code',
    'ogr2ogr',
  ])

  valid_domains = [
    u'Canada',
    # Provinces and territories
    u'Alberta',
    u'British Columbia',
    u'Manitoba',
    u'New Brunswick',
    u'Newfoundland and Labrador',
    u'Northwest Territories',
    u'Nova Scotia',
    u'Nunavut',
    u'Ontario',
    u'Prince Edward Island',
    u'Québec',
    u'Saskatchewan',
    u'Yukon',
  ]

  valid_domains_re = re.compile(', (AB|BC|MB|NB|NL|NS|NT|NU|ON|PE|QC|SK|YT)$')

  for slug, config in registry(base).items():
    invalid_keys = set(config.keys()) - valid_keys
    if invalid_keys:
      print "%s Unrecognized key: %s" % (config['file'], ', '.join(invalid_keys))
    values = config.values()
    if len(values) > len(set(values)):
      print "%s Non-unique values" % config['file']
    for key, value in config.items():
      if not value:
        print "%s Empty value for %s" % (config['file'], key)
    if config.get('domain'):
      if config['domain'] not in valid_domains and not valid_domains_re.search(config['domain']):
        print "%s Unrecognized domain: %s" % (config['file'], config['domain'])
    if config.get('encoding'):
      if config['encoding'] not in ('iso-8859-1'):
        print "%s Unrecognied encoding: %s" % (config['file'], config['encoding'])

# Check that all data directories contain a `LICENSE.txt`.
@task
def licenses(base='.'):
  for (dirpath, dirnames, filenames) in os.walk(base, followlinks=True):
    if '.git' in dirnames:
      dirnames.remove('.git')
    if '.DS_Store' in filenames:
      filenames.remove('.DS_Store')
    if filenames and 'LICENSE.txt' not in filenames:
      print '%s No LICENSE.txt' % dirpath

# Check that the source, data and licence URLs work.
@task
def urls(base='.'):
  for slug, config in registry(base).items():
    for key in ('source_url', 'licence_url', 'data_url'):
      if config.get(key):
        url = config[key]
        result = urlparse(url)
        if result.scheme == 'ftp':
          ftp = FTP(result.hostname)
          ftp.login(result.username, result.password)
          ftp.cwd(os.path.dirname(result.path))
          if os.path.basename(result.path) not in ftp.nlst():
            print '404 %s' % url
          ftp.quit()
        else:
          try:
            arguments = {'allow_redirects': True}
            if result.username:
              url = '%s://%s%s' % (result.scheme, result.hostname, result.path)
              arguments['auth'] = (result.username, result.password)
            response = requests.head(url, **arguments)
            status_code = response.status_code
            if status_code != 200:
              print '%d %s' % (status_code, url)
          except requests.exceptions.ConnectionError:
            print '404 %s' % url

# Check that the spreadsheet is up-to-date.
@task
def spreadsheet(base='.'):
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
    u"Ontario electoral districts",
    u"Prince Edward Island electoral districts",
    u"Québec electoral districts",
    u"Saskatchewan electoral districts",

    # Federal
    u"Census divisions",
    u"Census subdivisions",
    u"Federal electoral districts",
  ]

  rows = csv()

  for slug, config in registry(base).items():
    geographic_code = config.get('geographic_code')
    if geographic_code:
      row = rows.get(config['geographic_code'])
      if row:
        if row[3] != 'Y':
          print '%s (%s) Change "Shapefile?" from "%s" to "Y"' % (slug, geographic_code, row[3])
      else:
        print "%s (%s) Not in spreadsheet" % (slug, geographic_code)
    elif slug not in no_geographic_code:
      print "%s No geographic code" % slug

# Review any notes about the boundaries.
@task
def notes(base='.'):
  rows = csv()

  for slug, config in registry(base).items():
    notes = []
    if config.get('notes'):
      notes.append('Notes: %s' % config['notes'])
    geographic_code = config.get('geographic_code')
    if geographic_code:
      row = rows.get(config['geographic_code'])
      if row:
        if row[8]:
          raise Exception('%s has request notes' % slug)
        if row[9]:
          notes.append('Revision: %s' % row[9])
    if notes:
      print slug
      if config.get('source_url'):
        print 'Source: %s' % config['source_url']
      for note in notes:
        print note
      print

# Update any out-of-date shapefiles.
@task
def shapefiles(base='.'):
  def process(slug, config, url, data_file_path):
    from glob import glob
    from zipfile import ZipFile, BadZipfile

    from git import Repo

    # We can only process KML, KMZ and ZIP files.
    extension = os.path.splitext(data_file_path)[1]
    if extension in ('.kml', '.kmz', '.zip'):
      repo = Repo('.')
      index = repo.index

      # GitPython can't handle paths starting with "./".
      if config['file'].startswith('./'):
        directory = config['file'][2:]
      else:
        directory = config['file']

      # Remove old files.
      for basename in os.listdir(config['file']):
        if basename not in ('.DS_Store', 'definition.py', 'LICENSE.txt', 'data.kml', 'data.kmz', 'data.zip'):
          os.unlink(os.path.join(config['file'], basename))
          index.remove([os.path.join(directory, basename)])

      files_to_add = []

      # Unzip any zip file.
      error_thrown = False
      if extension == '.zip':
        try:
          zip_file = ZipFile(data_file_path)
          for name in zip_file.namelist():
            # Flatten the zip file hierarchy.
            extension = os.path.splitext(name)[1]
            if extension in ('.kml', '.kmz'):
              basename = 'data%s' % extension # assumes one KML or KMZ file per archive
            else:
              basename = os.path.basename(name) # assumes no collisions across hierarchy
            with open(os.path.join(config['file'], basename), 'wb') as f:
              f.write(zip_file.read(name))
            if extension not in ('.kml', '.kmz'):
              files_to_add.append(os.path.join(directory, basename))
        except BadZipfile:
          error_thrown = True
          print 'Bad ZIP file %s\n' % url
        finally:
          os.unlink(data_file_path)

      # Unzip any KMZ file.
      kmz_file_path = os.path.join(config['file'], 'data.kmz')
      if not error_thrown and os.path.exists(kmz_file_path):
        try:
          zip_file = ZipFile(kmz_file_path)
          for name in zip_file.namelist():
            # A KMZ file contains a single KML file and other supporting files.
            # @see https://developers.google.com/kml/documentation/kmzarchives
            if os.path.splitext(name)[1] == '.kml':
              with open(os.path.join(config['file'], 'data.kml'), 'wb') as f:
                f.write(zip_file.read(name))
        except BadZipfile:
          error_thrown = True
          print 'Bad KMZ file %s\n' % url
        finally:
          os.unlink(kmz_file_path)

      if not error_thrown:
        # Convert any KML to shapefile.
        kml_file_path = os.path.join(config['file'], 'data.kml')
        if os.path.exists(kml_file_path):
          result = run('ogrinfo -q %s | grep -v "3D Point"' % kml_file_path, hide='out').stdout
          if result.count('\n') > 1:
            print 'Too many layers %s' % url
          else:
            layer = re.search('^\d+: (\S+)', result).group(1)
            run('ogr2ogr -f "ESRI Shapefile" %s %s -nlt POLYGON %s' % (config['file'], kml_file_path, layer), echo=True)
            for name in glob(os.path.join(directory, '*.[dps][bhr][fjpx]')):
              files_to_add.append(name)
            os.unlink(kml_file_path)

        # Merge multiple shapefiles into one.
        names = glob(os.path.join(config['file'], '*.shp'))
        if len(names) > 1:
          for name in names:
            run('ogr2ogr -f "ESRI Shapefile" %s %s -update -append -nln Boundaries' % (config['file'], name), echo=True)
            basename = os.path.splitext(os.path.basename(name))[0]
            for name in glob(os.path.join(directory, '%s.[dps][bhr][fjnpx]' % basename)):
              files_to_add.remove(name)
              os.unlink(name)

        # Convert any 3D shapefile into 2D.
        shp_file_path = os.path.join(config['file'], '*.shp')
        if os.path.exists(shp_file_path):
          result = run('ogrinfo -q %s' % shp_file_path, hide='out').stdout
          if result.count('\n') > 1:
            print 'Too many layers %s' % url
          elif re.search('3D Polygon', result):
            run('ogr2ogr -f "ESRI Shapefile" %s %s -nlt POLYGON -overwrite' % (config['file'], shp_file_path), echo=True)

        # Run any additional commands.
        if config.get('ogr2ogr'):
          run('ogr2ogr -f "ESRI Shapefile" -overwrite %s %s %s' % (config['file'], shp_file_path, config['ogr2ogr']), echo=True)

        # Add files to git.
        index.add(files_to_add)

        # Update last updated timestamp.
        definition_path = os.path.join(config['file'], 'definition.py')
        with open(definition_path) as f:
          definition = f.read()
        with open(definition_path, 'w') as f:
          f.write(re.sub('(?<=last_updated=date\()[\d, ]+', last_updated.strftime('%Y, %-m, %-d'), definition))

        # Print notes.
        notes = []
        if config.get('notes'):
          notes.append(config['notes'])
        if notes:
          print '%s\n%s\n' % (slug, '\n'.join(notes))
    else:
      print 'Unrecognized extension %s\n' % url

  from datetime import datetime

  from rfc6266 import parse_headers

  no_update = [
    # Needs to be split into one shapefile per municipality.
    'http://depot.ville.montreal.qc.ca/elections-2009-districts/multi-poly/data.zip',
  ]

  # Retrieve shapefiles.
  for slug, config in registry(base).items():
    if config.get('data_url'):
      url = config['data_url']

      if url not in no_update:
        result = urlparse(url)

        if result.scheme == 'ftp':
          # Get the last modified timestamp.
          ftp = FTP(result.hostname)
          ftp.login(result.username, result.password)
          last_modified = ftp.sendcmd('MDTM %s' % result.path)

          # Parse the timestamp as a date.
          last_updated = datetime.strptime(last_modified[4:], '%Y%m%d%H%M%S').date()

          if config['last_updated'] < last_updated:
            # Determine the file extension.
            extension = os.path.splitext(url)[1]

            # Set the new file's name.
            data_file_path = os.path.join(config['file'], 'data%s' % extension)

            # Download new file.
            ftp.retrbinary('RETR %s' % result.path, open(data_file_path, 'wb').write)
            ftp.quit()

            process(slug, config, url, data_file_path)
        else:
          # Get the last modified timestamp.
          arguments = {'allow_redirects': True}
          if result.username:
            url = '%s://%s%s' % (result.scheme, result.hostname, result.path)
            arguments['auth'] = (result.username, result.password)
          response = requests.head(url, **arguments)
          last_modified = response.headers.get('last-modified')

          # Parse the timestamp as a date.
          if last_modified:
            last_updated = datetime.strptime(last_modified, '%a, %d %b %Y %H:%M:%S GMT')
          else:
            last_updated = datetime.now()
          last_updated = last_updated.date()

          if config['last_updated'] > last_updated:
            print '%s are more recent than the source\n' % slug
          elif config['last_updated'] < last_updated:
            # Determine the file extension.
            if response.headers.get('content-disposition'):
              filename = parse_headers(response.headers['content-disposition']).filename_unsafe
            else:
              filename = url
            extension = os.path.splitext(filename)[1]

            # Set the new file's name.
            data_file_path = os.path.join(config['file'], 'data%s' % extension)

            # Download new file.
            arguments['stream'] = True
            response = requests.get(url, **arguments)
            with open(data_file_path, 'wb') as f:
              for chunk in response.iter_content():
                f.write(chunk)

            process(slug, config, url, data_file_path)
