#coding: utf8

from datetime import datetime
import os.path
import re
from urlparse import urlparse
from zipfile import ZipFile, BadZipfile

import boundaries
from git import *
import requests

# @see Command#handle in boundaries/management/commands/loadshapefiles.py
boundaries.autodiscover('.')
all_sources = boundaries.registry

no_update = [
  # Need to run additional commands.
  'http://opendata.peelregion.ca/media/2549/wardboundary20102014_shp_04.2012.zip',
  # Needs to be split into one shapefile per municipality.
  'http://depot.ville.montreal.qc.ca/elections-2009-districts/multi-poly/data.zip',
]

# Update shapefiles.
repo = Repo('.')
index = repo.index
for slug, config in all_sources.items():
  if config.get('data_url'):
    url = config['data_url']

    if url not in no_update:
      result = urlparse(url)

      if result.scheme == 'ftp':
        # @todo
        print "FTP %s\n" % url
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
          last_updated = datetime.strptime(last_modified, '%a, %d %b %Y %H:%M:%S GMT').date()
        else:
          last_updated = None

        if not last_updated or config['last_updated'] < last_updated:
          extension = os.path.splitext(url)[1]

          if extension == '.zip':
            # GitPython can't handle paths starting with "./".
            if config['file'].startswith('./'):
              directory = config['file'][2:]
            else:
              directory = config['file']

            # Remove old files.
            for basename in os.listdir(config['file']):
              if basename not in ('.DS_Store', 'definition.py', 'LICENSE.txt'):
                os.unlink(os.path.join(config['file'], basename))
                index.remove([os.path.join(directory, basename)])

            # Download new file.
            arguments['stream'] = True
            response = requests.get(url, **arguments)
            zip_file_path = os.path.join(config['file'], 'data.zip')
            with open(zip_file_path, 'wb') as f:
              for chunk in response.iter_content():
                f.write(chunk)

            try:
              # Unzip new file.
              zip_file = ZipFile(zip_file_path)
              for name in zip_file.namelist():
                # Flatten the zip file hierarchy.
                basename = os.path.basename(name)
                with open(os.path.join(config['file'], basename), 'wb') as f:
                  f.write(zip_file.read(name))
                index.add([os.path.join(directory, basename)])

              # Update last updated timestamp.
              definition_path = os.path.join(config['file'], 'definition.py')
              with open(definition_path) as f:
                definition = f.read()
              with open(definition_path, 'w') as f:
                f.write(re.sub('(?<=last_updated=date\()[\d, ]+', last_updated.strftime('%Y, %-m, %-d'), definition))

              # Print notes.
              if config.get('notes'):
                print "%s\n%s\n" % (slug, config['notes'])
            except BadZipfile:
              print "Bad zip file %s\n" % url

            # Clean up.
            os.unlink(zip_file_path)
          elif extension == '.kml':
            # @todo
            print "KML %s\n" % url
          else:
            print "Unrecognized extension %s\n" % url
