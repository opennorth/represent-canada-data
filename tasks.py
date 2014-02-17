# coding: utf8

import csv, codecs, cStringIO
from collections import defaultdict, OrderedDict
from datetime import datetime
from ftplib import FTP
from getpass import getpass
from glob import glob
import os
import os.path
import re
import stat
import sys
from StringIO import StringIO
from urlparse import urlparse
from zipfile import ZipFile, BadZipfile

import boundaries
from django.template.defaultfilters import slugify
import gdata.spreadsheet.service
from git import Repo
from invoke import run, task
import lxml.html
import requests
from rfc6266 import parse_headers

from constants import (
  open_data_licenses,
  some_rights_reserved_licenses,
  all_rights_reserved_licenses,
  all_rights_reserved_terms_re,
  terms,
  terms_re,
  valid_keys,
  valid_metadata_keys,
  authorities,
  municipal_subdivisions,
  request_headers,
  receipt_headers,
  headers,
)

# Returns the directory in which a shapefile exists.
def dirname(path):
  # GitPython can't handle paths starting with "./".
  if path.startswith('./'):
    path = path[2:]
  if os.path.isdir(path):
    return path
  else:
    return os.path.dirname(path)


# Reads `definition.py` files.
def registry(base='.'):
  boundaries.autodiscover(base)
  return boundaries.registry


# Reads a remote CSV file.
def csv_reader(url):
  return csv.reader(StringIO(requests.get(url).content))


sgc_code_to_ocdid_memo = {}
# Maps Standard Geographical Classification codes to OCD identifiers.
def sgc_code_to_ocdid():
  if not sgc_code_to_ocdid_memo:
    sgc_code_to_ocdid_memo['01'] = 'ocd-division/country:ca'
    for row in csv_reader('https://raw.github.com/opencivicdata/ocd-division-ids/master/mappings/country-ca-sgc/ca_provinces_and_territories.csv'):
      sgc_code_to_ocdid_memo[row[1]] = row[0]
    filenames = [
      'ca_census_divisions',
      'ca_census_subdivisions',
    ]
    for filename in filenames:
      for row in csv_reader('https://raw.github.com/opencivicdata/ocd-division-ids/master/identifiers/country-ca/%s.csv' % filename):
        sgc_code_to_ocdid_memo[row[0].split(':')[-1]] = row[0]
  return sgc_code_to_ocdid_memo


ocdid_to_name_memo = {}
# Maps OCD identifiers to names.
def ocdid_to_name():
  if not ocdid_to_name_memo:
    filenames = [
      'ca_manual',
      'ca_provinces_and_territories',
      'ca_census_divisions',
      'ca_census_subdivisions',
      'census_subdivision-montreal-arrondissements',
    ]
    for filename in filenames:
      for row in csv_reader('https://raw.github.com/opencivicdata/ocd-division-ids/master/identifiers/country-ca/%s.csv' % filename):
        ocdid_to_name_memo[row[0].decode('utf8')] = row[1].decode('utf8')
  return ocdid_to_name_memo


ocdid_to_type_memo = {}
# Maps OCD identifiers to types.
def ocdid_to_type():
  if not ocdid_to_type_memo:
    filenames = [
      'ca_census_divisions',
      'ca_census_subdivisions',
    ]
    for filename in filenames:
      for row in csv_reader('https://raw.github.com/opencivicdata/ocd-division-ids/master/mappings/country-ca-types/%s.csv' % filename):
        ocdid_to_type_memo[row[0].decode('utf8')] = row[1].decode('utf8')
  return ocdid_to_type_memo


corporations_memo = {}
def corporations():
  if not corporations_memo:
    for row in csv_reader('https://raw.github.com/opencivicdata/ocd-division-ids/master/mappings/country-ca-corporations/ca_municipal_subdivisions.csv'):
      corporations_memo[row[0]] = row[1].decode('utf8')
  return corporations_memo


def get_division_id(config):
  division_id = config['metadata'].get('division_id')
  geographic_code = config['metadata'].get('geographic_code')

  # Determine division_id if not set.
  if division_id:
    if geographic_code:
      raise Exception('%s: Set division_id or geographic_code' % slug)
  else:
    if geographic_code:
      length = len(geographic_code)
      if length == 2:
        division_id = sgc_code_to_ocdid()[geographic_code]
      elif length == 4:
        division_id = 'ocd-division/country:ca/cd:%s' % geographic_code
      elif length == 7:
        division_id = 'ocd-division/country:ca/csd:%s' % geographic_code
      else:
        raise Exception('%s: Unrecognized geographic code %s' % (slug, geographic_code))

  return division_id

def get_definition(division_id):
  sections = division_id.split('/')
  ocd_type, ocd_type_id = sections[-1].split(':')

  config = {
    'encoding': 'iso-8859-1',
  }

  # Determine slug, domain and authority.
  name = ocdid_to_name()[division_id]
  if ocd_type == 'country':
    slug = 'Federal electoral districts'
    config['domain'] = name
    config['authority'] = ['Her Majesty the Queen in Right of Canada']

  elif ocd_type in ('province', 'territory'):
    slug = '%s electoral districts' % name
    config['domain'] = name
    config['authority'] = ['Her Majesty the Queen in Right of %s' % name]

  elif ocd_type in ('cd', 'csd'):
    province_or_territory_sgc_code = ocd_type_id[:2]
    province_or_territory_abbreviation = sgc_code_to_ocdid()[province_or_territory_sgc_code].split(':')[-1].upper()

    boroughs = [
      'ocd-division/country:ca/csd:2425213',  # Lévis
      'ocd-division/country:ca/csd:2458227',  # Longueuil
      'ocd-division/country:ca/csd:2466023',  # Montréal
      'ocd-division/country:ca/csd:2423027',  # Québec
      'ocd-division/country:ca/csd:2494068',  # Saguenay
      'ocd-division/country:ca/csd:2443027',  # Sherbrooke
    ]

    if province_or_territory_sgc_code == '24' and division_id in boroughs:
      slug = '%s boroughs' % name
    elif province_or_territory_sgc_code == '12' and ocdid_to_type()[division_id] == 'RGM':
      slug = '%s districts' % name
    elif province_or_territory_sgc_code == '48' and ocdid_to_type()[division_id] == 'MD':
      slug = '%s divisions' % name
    elif province_or_territory_sgc_code == '24':
      slug = '%s districts' % name
    else:
      slug = '%s wards' % name
    config['domain'] = '%s, %s' % (name, province_or_territory_abbreviation)
    if ocd_type == 'csd':
      config['authority'] = authorities + [corporations()[division_id]]
    else:
      config['authority'] = ['']  # We have no expectation for the authority of a Census division

  elif ocd_type == 'arrondissement':
    census_subdivision_ocdid = '/'.join(sections[:-1])
    census_subdivision_name = ocdid_to_name()[census_subdivision_ocdid]

    province_or_territory_sgc_code = census_subdivision_ocdid.split(':')[-1][:2]
    province_or_territory_abbreviation = sgc_code_to_ocdid()[province_or_territory_sgc_code].split(':')[-1].upper()

    slug = '%s districts' % name
    config['domain'] = '%s, %s, %s' % (name, census_subdivision_name, province_or_territory_abbreviation)
    config['authority'] = [corporations()[census_subdivision_ocdid]]

  else:
    raise Exception('%s: Unrecognized OCD type %s' % (division_id, ocd_type))

  return (slug, config)


def assert_match(slug, field, actual, expected):
  if isinstance(expected, re._pattern_type):
    if not expected.search(actual):
      print '%-50s Expected %s to match %s not %s' % (slug, field, expected.pattern, actual)
  elif isinstance(expected, list):
    if actual not in expected:
      print '%-50s Expected %s to be %s not %s' % (slug, field, expected[-1], actual)
  elif actual != expected:
    print '%-50s Expected %s to be %s not %s' % (slug, field, expected, actual)


class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)


# @todo Guess name_func and id_func based on the shapefile.
@task
def define(division_id):
  ocdid_to_sgc_code_map = {v:k for k,v in sgc_code_to_ocdid().items()}

  slug, config = get_definition(division_id)
  if isinstance(slug, re._pattern_type):
    slug = re.sub('\\\[AZ]', '', slug.pattern)

  config['slug'] = slug
  config['last_updated'] = datetime.now().strftime('%Y, %-m, %-d')
  config['authority'] = config['authority'][-1]

  ocd_type, ocd_type_id = division_id.split('/')[-1].split(':')
  if ocd_type == 'country' and ocd_type_id == 'ca':
    config['geographic_code'] = '01'
  elif ocd_type in ('province', 'territory', 'cd', 'csd'):
    config['geographic_code'] = ocdid_to_sgc_code_map[division_id]
  else:
    raise Exception('%s: Unrecognized OCD type %s' % (division_id, ocd_type))

  print """from datetime import date

import boundaries

boundaries.register(u'%(slug)s',
    domain=u'%(domain)s',
    last_updated=date(%(last_updated)s),
    name_func=boundaries.attr(''),
    id_func=boundaries.attr(''),
    authority=u'%(authority)s',
    encoding='iso-8859-1',
    metadata={'geographic_code': '%(geographic_code)s'},
)""" % config


# Check that all data directories contain a `LICENSE.txt`.
@task
def licenses(base='.'):
  for (dirpath, dirnames, filenames) in os.walk(base, followlinks=True):
    if '.git' in dirnames:
      dirnames.remove('.git')
    if 'geojson' in dirnames:
      dirnames.remove('geojson')
    if '.DS_Store' in filenames:
      filenames.remove('.DS_Store')
    if filenames and 'LICENSE.txt' not in filenames:
      print '%s No LICENSE.txt' % dirpath


# Fix file permissions.
@task
def permissions(base='.'):
  for (dirpath, dirnames, filenames) in os.walk(base, followlinks=True):
    if '.git' in dirnames:
      dirnames.remove('.git')
    for filename in filenames:
      path = os.path.join(dirpath, filename)
      if os.stat(path).st_mode != 33188:  # 100644 octal
        os.chmod(path, stat.S_IWUSR | stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)


# @see http://ben.balter.com/2013/06/26/how-to-convert-shapefiles-to-geojson-for-use-on-github/
@task
def geojson(base='.', geo_json_base='./geojson'):
  sgc_code_to_ocdid_map = sgc_code_to_ocdid()
  ocdid_to_name_map = ocdid_to_name()
  readme = defaultdict(lambda: defaultdict(list))

  for slug, config in registry(base).items():
    if 'fed/cd' not in config['file'] and 'fed/csd' not in config['file']:  # files are too large for GitHub
      directory = dirname(config['file'])
      shp_file_path = glob(os.path.join(directory, '*.shp'))[0]
      geo_json_path = os.path.join(geo_json_base, re.sub('/', '_', re.sub('^/|/$', '', re.sub('^' + re.escape(base), '', directory))) + '.geojson')
      if not os.path.exists(geo_json_path):
        run('ogr2ogr -f "GeoJSON" -t_srs EPSG:4326 "%s" "%s"' % (geo_json_path, shp_file_path), echo=True)
      # I have not been able to install topojson (hangs during install), but it may reduce file sizes.
      # run('topojson -o %s %s', (geo_json_path, geo_json_path), echo=True)

      division_id = get_division_id(config)
      if os.stat(geo_json_path).st_size > 10485760:  # 10MB
        suffix = ' (too large to preview)'
      else:
        suffix = ''

      item = (slug, '* [%s](https://github.com/opennorth/represent-canada-data/blob/master/geojson/%s#files): [API](http://represent.opennorth.ca/boundaries/%s/?limit=0)%s\n' %
        (slug.encode('utf-8'), os.path.basename(geo_json_path), slugify(slug).encode('utf-8'), suffix))

      match = re.search('\Aocd-division/country:ca/csd:(\d+)', division_id)
      if match:
        readme[ocdid_to_name_map[sgc_code_to_ocdid_map[match.group(1)[:2]]]]['lower'].append(item)
      else:
        readme[ocdid_to_name_map[division_id]]['upper'].append(item)

  with open(os.path.join(geo_json_base, 'README.md'), 'w') as f:
    f.write('# Represent API: GeoJSON\n\n## Canada\n\n')
    items = readme.pop('Canada', None)
    if items:
      for part in ('upper', 'lower'):
        for slug, markdown in sorted(items[part]):
          f.write(markdown)
    for name, items in sorted(readme.items()):
      f.write('\n## %s\n\n' % name.encode('utf-8'))
      for part in ('upper', 'lower'):
        for slug, markdown in sorted(items[part]):
          f.write(markdown)


# Check that all `definition.py` files are valid.
@task
def definitions(base='.'):
  division_ids = set()
  for slug, config in registry(base).items():
    directory = dirname(config['file'])

    # Validate LICENSE.txt.
    license_path = os.path.join(directory, 'LICENSE.txt')
    if os.path.exists(license_path):
      with open(license_path) as f:
        license_text = f.read().rstrip('\n')
      if config.get('licence_url'):
        licence_url = config['licence_url']
        if licence_url in open_data_licenses or licence_url in some_rights_reserved_licenses:
          if not terms.get(licence_url) and not terms_re.get(licence_url):
            print '%-50s No LICENSE.txt template for License URL %s' % (slug, licence_url)
          elif terms.get(licence_url) and license_text != terms[licence_url] or terms_re.get(licence_url) and not terms_re[licence_url].search(license_text):
            print '%-50s Expected LICENSE.txt to match license-specific template' % slug
        elif licence_url in all_rights_reserved_licenses:
          if not all_rights_reserved_terms_re.search(license_text):
            print '%-50s Expected LICENSE.txt to match "all rights reserved" template' % slug
        else:
          print '%-50s Unrecognized License URL %s' % (slug, licence_url)
      elif not all_rights_reserved_terms_re.search(license_text):
        print '%-50s Expected LICENSE.txt to match "all rights reserved" template' % slug

    # Check for invalid keys, non-unique or empty values.
    invalid_keys = set(config.keys()) - valid_keys
    if invalid_keys:
      print '%-50s Unrecognized key: %s' % (slug, ', '.join(invalid_keys))
    values = [value for key, value in config.items() if key != 'metadata']
    if len(values) > len(set(values)):
      print '%-50s Non-unique values' % slug
    for key, value in config.items():
      if not value:
        print '%-50s Empty value for %s' % (slug, key)

    # Check for missing required keys.
    for key in ('domain', 'last_updated', 'name_func', 'authority', 'encoding'):
      if not config.get(key):
        print '%-50s Missing %s' % (slug, key)
    if not config.get('source_url') and (config.get('licence_url') or config.get('data_url')):
      print '%-50s Missing source_url' % slug
    if config.get('source_url') and not config.get('licence_url') and not config.get('data_url'):
      print '%-50s Missing licence_url or data_url' % slug

    # Validate fields.
    for key in ('name', 'singular'):
      if config.get(key):
        print '%-50s Expected %s to be missing' % (slug, key)
    if config.get('encoding') and config['encoding'] != 'iso-8859-1':
      print '%-50s Expected encoding to be iso-8859-1 not %s' % (slug, config['encoding'])

    if slug not in ('Census divisions', 'Census subdivisions'):
      # Check for invalid keys or empty values.
      invalid_keys = set(config['metadata'].keys()) - valid_metadata_keys
      if invalid_keys:
        print '%-50s Unrecognized key: %s' % (slug, ', '.join(invalid_keys))
      for key, value in config['metadata'].items():
        if not value:
          print '%-50s Empty value for %s' % (slug, key)

      division_id = get_division_id(config)

      # Ensure division_id is unique.
      if division_id in division_ids:
        print '%-50s Duplicate division_id %s' % (slug, division_id)
      else:
        ocd_divisions.add(division_id)

      expected_slug, expected_config = get_definition(division_id)

      # Check for unexpected values.
      assert_match(slug, 'slug', slug, expected_slug)
      for key, value in expected_config.items():
        assert_match(slug, key, config[key], value)


# Check that the source, data and license URLs work.
@task
def urls(base='.'):
  headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)'}

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
            arguments = {}
            if result.username:
              url = '%s://%s%s' % (result.scheme, result.hostname, result.path)
              arguments['auth'] = (result.username, result.password)
            response = requests.head(url, headers=headers, **arguments)
            if response.status_code == 405:  # if HEAD requests are not allowed
              response = requests.get(url, headers=headers, **arguments)
            if response.status_code != 200:
              print '%d %s' % (response.status_code, url)
          except requests.exceptions.ConnectionError:
            print '404 %s' % url


# Update any out-of-date shapefiles.
@task
def shapefiles(base='.'):
  headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)'}

  def process(slug, config, url, data_file_path):
    # We can only process KML, KMZ and ZIP files.
    extension = os.path.splitext(data_file_path)[1]
    if extension in ('.kml', '.kmz', '.zip'):
      repo_path = os.path.dirname(data_file_path)
      while not os.path.exists(os.path.join(repo_path, '.git')) and not repo_path == '/':
        repo_path = os.path.join(repo_path, '..')
      repo_path = os.path.realpath(repo_path)

      repo = Repo(repo_path)
      index = repo.index
      directory = dirname(config['file'])

      # Remove old files.
      for basename in os.listdir(directory):
        if basename not in ('.DS_Store', 'definition.py', 'LICENSE.txt', 'data.kml', 'data.kmz', 'data.zip'):
          os.unlink(os.path.join(directory, basename))
          index.remove([os.path.relpath(os.path.join(directory, basename), repo_path)])

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
              basename = 'data%s' % extension  # assumes one KML or KMZ file per archive
            else:
              basename = os.path.basename(name)  # assumes no collisions across hierarchy
            with open(os.path.join(directory, basename), 'wb') as f:
              f.write(zip_file.read(name))
            if extension not in ('.kml', '.kmz'):
              files_to_add.append(os.path.join(directory, basename))
        except BadZipfile:
          error_thrown = True
          print 'Bad ZIP file %s\n' % url
        finally:
          os.unlink(data_file_path)

      # Unzip any KMZ file.
      kmz_file_path = os.path.join(directory, 'data.kmz')
      if not error_thrown and os.path.exists(kmz_file_path):
        try:
          zip_file = ZipFile(kmz_file_path)
          for name in zip_file.namelist():
            # A KMZ file contains a single KML file and other supporting files.
            # @see https://developers.google.com/kml/documentation/kmzarchives
            if os.path.splitext(name)[1] == '.kml':
              with open(os.path.join(directory, 'data.kml'), 'wb') as f:
                f.write(zip_file.read(name))
        except BadZipfile:
          error_thrown = True
          print 'Bad KMZ file %s\n' % url
        finally:
          os.unlink(kmz_file_path)

      if not error_thrown:
        # Convert any KML to shapefile.
        kml_file_path = os.path.join(directory, 'data.kml')
        if os.path.exists(kml_file_path):
          result = run('ogrinfo -q %s | grep -v "3D Point"' % kml_file_path, hide='out').stdout
          if result.count('\n') > 1:
            print 'Too many layers %s' % url
          else:
            layer = re.search('\A\d+: (\S+)', result).group(1)
            run('ogr2ogr -f "ESRI Shapefile" %s %s -nlt POLYGON %s' % (directory, kml_file_path, layer), echo=True)
            for name in glob(os.path.join(directory, '*.[dps][bhr][fjpx]')):
              files_to_add.append(name)
            os.unlink(kml_file_path)

        # Merge multiple shapefiles into one.
        names = glob(os.path.join(directory, '*.shp'))
        if len(names) > 1:
          for name in names:
            run('ogr2ogr -f "ESRI Shapefile" %s %s -update -append -nln Boundaries' % (directory, name), echo=True)
            basename = os.path.splitext(os.path.basename(name))[0]
            for name in glob(os.path.join(directory, '%s.[dps][bhr][fjnpx]' % basename)):
              files_to_add.remove(name)
              os.unlink(name)

        shp_file_path = glob(os.path.join(directory, '*.shp'))
        if shp_file_path:
          shp_file_path = shp_file_path[0]
        if shp_file_path and os.path.exists(shp_file_path):
          # Convert any 3D shapefile into 2D.
          result = run('ogrinfo -q %s' % shp_file_path, hide='out').stdout
          if result.count('\n') > 1:
            print 'Too many layers %s' % url
          elif re.search('3D Polygon', result):
            run('ogr2ogr -f "ESRI Shapefile" %s %s -nlt POLYGON -overwrite' % (directory, shp_file_path), echo=True)
            for name in list(files_to_add):
              if not os.path.exists(name):
                files_to_add.remove(name)

          # Replace "Double_Stereographic" with "Oblique_Stereographic".
          prj_file_path = os.path.splitext(shp_file_path)[0] + '.prj'
          if prj_file_path and os.path.exists(prj_file_path):
            with open(prj_file_path) as f:
              prj = f.read()
            if 'Double_Stereographic' in prj:
              with open(prj_file_path, 'w') as f:
                f.write(prj.replace('Double_Stereographic', 'Oblique_Stereographic'))
          elif config.get('prj'):
            with open(prj_file_path, 'w') as f:
              f.write(requests.get(config['prj']).content)
            files_to_add.append(prj_file_path)
          else:
            print 'No PRJ file %s' % url

          # Run any additional commands on the shapefile.
          if config.get('ogr2ogr'):
            run('ogr2ogr -f "ESRI Shapefile" -overwrite %s %s %s' % (directory, shp_file_path, config['ogr2ogr']), echo=True)
            for name in list(files_to_add):
              if not os.path.exists(name):
                files_to_add.remove(name)

        # Add files to git.
        index.add([os.path.relpath(name, repo_path) for name in files_to_add])

        # Update last updated timestamp.
        definition_path = os.path.join(directory, 'definition.py')
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

  # Retrieve shapefiles.
  for slug, config in registry(base).items():
    if config.get('data_url'):
      url = config['data_url']
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
          data_file_path = os.path.join(dirname(config['file']), 'data%s' % extension)

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
        response = requests.head(url, headers=headers, **arguments)
        if response.status_code == 405:  # if HEAD requests are not allowed
          response = requests.get(url, headers=headers, **arguments)
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
          extension = os.path.splitext(filename)[1].lower()

          # Set the new file's name.
          data_file_path = os.path.join(dirname(config['file']), 'data%s' % extension)

          # Download new file.
          arguments['stream'] = True
          response = requests.get(url, headers=headers, **arguments)
          with open(data_file_path, 'wb') as f:
            for chunk in response.iter_content():
              f.write(chunk)

          process(slug, config, url, data_file_path)


# Generate the spreadsheet for tracking progress on data collection.
@task
def spreadsheet(base='.', private_base='../represent-canada-private-data'):
  sgc_code_to_ocdid_map = sgc_code_to_ocdid()
  ocdid_to_sgc_code_map = {v:k for k,v in sgc_code_to_ocdid_map.items()}
  records = OrderedDict()

  for row in csv_reader('https://raw.github.com/opencivicdata/ocd-division-ids/master/mappings/country-ca-subdivisions/ca_municipal_subdivisions.csv'):
    municipal_subdivisions[row[0].split(':')[-1]] = row[1]

  urls = {}
  for row in csv_reader('https://raw.github.com/opencivicdata/ocd-division-ids/master/mappings/country-ca-urls/ca_census_subdivisions.csv'):
    urls[row[0].split(':')[-1]] = row[1]

  abbreviations = {}
  for row in csv_reader('https://raw.github.com/opencivicdata/ocd-division-ids/master/mappings/country-ca-abbr/ca_provinces_and_territories.csv'):
    abbreviations[row[1]] = row[0].split(':')[-1].upper()

  # Get scraper URLs.
  scraper_urls = {}
  for representative_set in requests.get('http://represent.opennorth.ca/representative-sets/?limit=0').json()['objects']:
    boundary_set_url = representative_set['related']['boundary_set_url']
    if boundary_set_url:
      if boundary_set_url != '/boundary-sets/census-subdivisions/':
        boundary_set = requests.get('http://represent.opennorth.ca%s' % boundary_set_url).json()
        if boundary_set.get('extra') and boundary_set['extra'].get('geographic_code'):
          scraper_urls[boundary_set['extra']['geographic_code']] = representative_set['data_about_url'] or representative_set['data_url']
        else:
          sys.stderr.write('%-60s No extra\n' % boundary_set_url)
    else:
      sys.stderr.write('%-60s No boundary_set_url\n' % representative_set['url'])

  # Create records for provinces and territories.
  for row in csv_reader('https://raw.github.com/opencivicdata/ocd-division-ids/master/identifiers/country-ca/ca_provinces_and_territories.csv'):
    records[ocdid_to_sgc_code_map[row[0]]] = {
      'OCD': row[0],
      'Geographic code': ocdid_to_sgc_code_map[row[0]],
      'Geographic name': row[1],
      'Province or territory': row[0].split(':')[-1].upper(),
      'Population': '',
      'URL': '',
      'Scraper?': scraper_urls.get(ocdid_to_sgc_code_map[row[0]], ''),
      'Shapefile?': '',
      'Contact': '',
      'Highrise URL': '',
      'Request notes': '',
      'Received via': '',
      'Last boundary': '',
      'Next boundary': '',
      'Permission to distribute': '',
      'Type of license': '',
      'License URL': '',
      'Denial notes': '',
    }

  # Create records for census subdivisions.
  reader = csv_reader('http://www12.statcan.gc.ca/census-recensement/2011/dp-pd/hlt-fst/pd-pl/FullFile.cfm?T=301&LANG=Eng&OFT=CSV&OFN=98-310-XWE2011002-301.CSV')
  reader.next()  # title
  reader.next()  # headers
  for row in reader:
    if row:
      result = re.search('\A(.+) \((.+)\)\Z', row[1].decode('iso-8859-1'))
      if result:
        name = result.group(1)
        province_or_territory = abbreviations[result.group(2)]
      elif row[1] == 'Canada':
        name = 'Canada'
        province_or_territory = ''
      else:
        raise Exception('Unrecognized name "%s"' % row[1])

      record = {
        'OCD': sgc_code_to_ocdid_map[row[0]],
        'Geographic code': row[0],
        'Geographic name': name,
        'Province or territory': province_or_territory,
        'Population': row[4],
        'URL': urls.get(row[0], ''),
        'Scraper?': scraper_urls.get(row[0], ''),
        'Contact': '',
        'Highrise URL': '',
        'Request notes': '',
        'Received via': '',
        'Last boundary': '',
        'Next boundary': '',
        'Permission to distribute': '',
        'Type of license': '',
        'License URL': '',
        'Denial notes': '',
      }

      if municipal_subdivisions.get(row[0]):
        if municipal_subdivisions[row[0]] == 'N':
          for header in ['Shapefile?'] + request_headers + receipt_headers:
            record[header] = 'N/A'
        elif municipal_subdivisions[row[0]] == 'Y':
          record['Shapefile?'] = 'Request'
        elif municipal_subdivisions[row[0]] == '?':
          record['Shapefile?'] = ''
      else:
        record['Shapefile?'] = ''

      records[row[0]] = record
    else:
      break

  # Merge information from received data.
  for directory, permission_to_distribute in [(base, 'Y'), (private_base, 'N')]:
    boundaries.registry = {}
    for slug, config in registry(directory).items():
      if config.get('metadata'):
        geographic_code = config['metadata'].get('geographic_code')
        if geographic_code:
          license_path = os.path.join(dirname(config['file']), 'LICENSE.txt')
          license_text = ''
          if os.path.exists(license_path):
            with open(license_path) as f:
              license_text = f.read().rstrip('\n').decode('utf-8')

          record = records[geographic_code]
          record['Shapefile?'] = 'Y'
          record['Permission to distribute'] = permission_to_distribute
          record['License URL'] = config.get('licence_url', '')

          if config.get('last_updated'):
            record['Last boundary'] = config['last_updated'].strftime('%-m/%-d/%Y')

          if config.get('source_url'):
            record['Contact'] = 'N/A'
            record['Received via'] = 'online'
          else:
            match = all_rights_reserved_terms_re.search(license_text)
            if match:
              record['Contact'] = match.group(1)
            record['Received via'] = 'email'

          if config.get('licence_url'):
            licence_url = config['licence_url']
            if licence_url in open_data_licenses:
              record['Type of license'] = 'Open'
            elif licence_url in some_rights_reserved_licenses:
              record['Type of license'] = 'Most rights reserved'
            elif licence_url in all_rights_reserved_licenses:
              record['Type of license'] = 'All rights reserved'
            else:
              raise Exception(licence_url)
          elif all_rights_reserved_terms_re.search(license_text):
            record['Type of license'] = 'All rights reserved'
          else:
            record['Type of license'] = 'Custom'
        else:
          sys.stderr.write('%-60s No geographic_code\n' % slug)

  reader = csv.DictReader(StringIO(requests.get('https://docs.google.com/spreadsheet/pub?key=0AtzgYYy0ZABtdGpJdVBrbWtUaEV0THNUd2JIZ1JqM2c&single=true&gid=25&output=csv').content))
  for row in reader:
    geographic_code = row['Geographic code']
    record = records[geographic_code]

    for key in row:
      a = record[key]
      b = row[key].decode('utf-8')

      if a != b:
        # Columns that are always tracked manually.
        # Scrapers for municipalities without wards are tracked manually.
        # In-progress requests are tracked manually.
        # Contacts for in-progress requests and private data are tracked manually.
        # We may have a contact to confirm the nonexistence of municipal subdivisions.
        # MFIPPA requests are tracked manually.
        # Additional details about license agreements and written consent are tracked manually.
        # We may have information for a bad shapefile from an in-progress request.
        if b and (
           (key in ('Highrise URL', 'Request notes', 'Next boundary', 'Denial notes')) or
           (key == 'Scraper?'         and not a         and record['Shapefile?'] == 'N/A') or
           (key == 'Shapefile?'       and not a         and b in ('Request', 'Requested')) or
           (key == 'Shapefile?'       and a == 'Request'and b == 'Requested') or
           (key == 'Contact'          and not a         and (row['Shapefile?'] == 'Requested' or record['Permission to distribute'] == 'N')) or
           (key == 'Contact'          and a == 'N/A'    and record['Shapefile?'] == 'N/A') or
           (key == 'Received via'     and a == 'email'  and b == 'MFIPPA') or
           (key == 'Type of license'  and '(' in b) or
           (key in ('Received via', 'Type of license', 'Permission to distribute') and not a and row['Shapefile?'] == 'Requested')):
          record[key] = b
        elif key != 'Population':  # separators
          sys.stderr.write('%-25s %s: expected "%s" got "%s"\n' % (key, geographic_code, a, b))

  writer = UnicodeWriter(sys.stdout)
  writer.writerow(headers)
  for _, record in records.items():
    writer.writerow([record[header] for header in headers])


# Update the spreadsheet for tracking progress on data collection.
# @see https://code.google.com/p/gdata-python-client/source/browse/samples/oauth/oauth_example.py
# @see https://code.google.com/p/gdata-python-client/source/browse/samples/spreadsheets/spreadsheetExample.py
@task
def update_spreadsheet(filename=''):
  client = gdata.spreadsheet.service.SpreadsheetsService()
  client.SetOAuthInputParameters(gdata.auth.OAuthSignatureMethod.HMAC_SHA1, 'opennorth.ca', consumer_secret=getpass('OAuth consumer secret: '))
  client.SetOAuthToken(client.FetchOAuthRequestToken())
  raw_input('Press a key after authenticating at %s' % client.GenerateOAuthAuthorizationURL())
  client.UpgradeToOAuthAccessToken()

  feed = client.GetListFeed('tjIuPkmkThEtLsTwbHgRj3g', 'oci')
  for entry in feed.entry[1:]:
    client.DeleteRow(entry)

  # Deleting a row at a time is incredibly slow. I didn't get to inserting rows.
  # Just use Google Spreadsheets' import feature.

  client.RevokeOAuthToken()


# Update populations.py in the represent-canada repository.
@task
def populations():
  reader = csv_reader('http://www12.statcan.gc.ca/census-recensement/2011/dp-pd/hlt-fst/pd-pl/FullFile.cfm?T=301&LANG=Eng&OFT=CSV&OFN=98-310-XWE2011002-301.CSV')
  reader.next()  # title
  reader.next()  # headers
  for row in reader:
    if row:
      if row[1] != 'Canada':
        division_id = 'ocd-division/country:ca/csd:%s' % row[0]
        if ocdid_to_type()[division_id] in ('C', 'CV', 'CY', 'MD', 'MU', 'RGM', 'T', 'TP', 'V', 'VL'):
          print '  u"%s": %s,' % (get_definition(division_id)[0], row[4])
    else:
      break
