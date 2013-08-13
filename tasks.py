#coding: utf8

from ftplib import FTP
import os.path
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

# Makes sure the spreadsheet doesn't undercount.
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
        if row[5] != 'Y':
          print "Change 'Shapefile?' for %s (%s) from '%s' to 'Y'" % (slug, geographic_code, row[5])
      else:
        print "%s (%s) isn't in the spreadsheet" % (slug, geographic_code)
    elif slug not in no_geographic_code:
      print "%s doesn't have a geographic code" % slug

# Makes sure URLs in definition files exist.
@task
def urls(base='.'):
  for slug, config in registry(base).items():
    # Check URLs.
    for key in ('source_url', 'licence_url', 'data_url'):
      if config.get(key):
        url = config[key]
        result = urlparse(url)
        if result.scheme == 'ftp':
          ftp = FTP(result.hostname)
          ftp.login(result.username, result.password)
          ftp.cwd(os.path.dirname(result.path))
          if os.path.basename(result.path) not in ftp.nlst():
            print "404 %s" % url
          ftp.quit()
        else:
          try:
            arguments = {'allow_redirects': True}
            if result.username:
              url = "%s://%s%s" % (result.scheme, result.hostname, result.path)
              arguments['auth'] = (result.username, result.password)
            response = requests.head(url, **arguments)
            status_code = response.status_code
            if status_code != 200:
              print "%d %s" % (status_code, url)
          except requests.exceptions.ConnectionError:
            print "404 %s" % url

# Prints notes about the boundaries.
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

# Updates shapefiles.
@task
def shapefiles(base='.'):
  def process(slug, config, url, data_file_path):
    from glob import glob
    import os
    import re
    from zipfile import ZipFile, BadZipfile

    from git import Repo

    repo = Repo('.')
    index = repo.index
    extension = os.path.splitext(data_file_path)[1]

    if extension in ('.kml', '.kmz', '.zip'):
      # GitPython can't handle paths starting with "./".
      if config['file'].startswith('./'):
        directory = config['file'][2:]
      else:
        directory = config['file']

      # Remove old files.
      for basename in os.listdir(config['file']):
        if basename not in ('.DS_Store', 'definition.py', 'LICENSE.txt', 'data.kml', 'data.zip'):
          os.unlink(os.path.join(config['file'], basename))
          index.remove([os.path.join(directory, basename)])

      error_thrown = False
      if extension == '.zip':
        try:
          # Unzip new file.
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
            if basename != 'data.kml':
              index.add([os.path.join(directory, basename)])
        except BadZipfile:
          error_thrown = True
          print 'Bad zip file %s\n' % url
        finally:
          os.unlink(data_file_path)

      kmz_file_path = os.path.join(config['file'], 'data.kmz')
      if not error_thrown and os.path.exists(kmz_file_path):
        try:
          # Unzip any KMZ.
          zip_file = ZipFile(kmz_file_path)
          for name in zip_file.namelist():
            if name == 'doc.kml':
              with open(os.path.join(config['file'], 'data.kml'), 'wb') as f:
                f.write(zip_file.read(name))
            else:
              raise Exception('Unrecognized KMZ content %s' % name)
        except BadZipfile:
          error_thrown = True
          print 'Bad KMZ file %s\n' % url
        finally:
          os.unlink(kmz_file_path)

      if not error_thrown:
        # Convert any KML to shapefile.
        kml_file_path = os.path.join(config['file'], 'data.kml')
        if os.path.exists(kml_file_path):
          if not os.system('ogr2ogr -f "ESRI Shapefile" %s %s -nlt POLYGON Boundaries' % (config['file'], kml_file_path)):
            for name in glob(os.path.join(directory, '*.[dps][bhr][fjpx]')):
              index.add([name])
          os.unlink(kml_file_path)

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
        if config.get('additional_commands'):
          notes.append(config['additional_commands'])
        if notes:
          print '%s\n%s\n' % (slug, '\n'.join(notes))
    else:
      print "Unrecognized extension %s\n" % url

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
            url = "%s://%s%s" % (result.scheme, result.hostname, result.path)
            arguments['auth'] = (result.username, result.password)
          response = requests.head(url, **arguments)
          last_modified = response.headers.get('last-modified')

          # Parse the timestamp as a date.
          if last_modified:
            last_updated = datetime.strptime(last_modified, '%a, %d %b %Y %H:%M:%S GMT')
          else:
            last_updated = datetime.now()
          last_updated = last_updated.date()

          if config['last_updated'] < last_updated:
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
