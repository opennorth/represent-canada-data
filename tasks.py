#coding: utf8

import csv
from ftplib import FTP
import os
import os.path
import re
import stat
from urlparse import urlparse

from invoke import run, task
import requests

open_data_licenses = [
  'http://data.gc.ca/eng/open-government-licence-canada',
  'http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
  'http://donnees.ville.quebec.qc.ca/licence.aspx',
  'http://opendata.peelregion.ca/terms-of-use.aspx',
  'http://ottawa.ca/en/mobile-apps-and-open-data/open-data-terms-use',
  'http://www.citywindsor.ca/opendata/Documents/OpenDataTermsofUse.pdf',
  'http://www.countygp.ab.ca/EN/main/community/maps-gis/open-data/open-data-licence.html',
  'http://www.edmonton.ca/city_government/initiatives_innovation/open-data-terms-of-use.aspx',
  'http://www.electionspei.ca/apilicense',
  'http://www.hamilton.ca/NR/rdonlyres/C58984A4-FE11-40B9-A231-8572EB922AAA/0/OpenDataTermsAndConditions_Final.htm',
  'http://www.fredericton.ca/en/citygovernment/TermsOfUse.asp',
  'http://www.london.ca/d.aspx?s=/Open_Data/Open_Data_Terms_Use.htm',
  'http://www.milton.ca/en/resourcesGeneral/Open_Data/Milton_Open_Data_Terms_V1.pdf',
  'http://www.regina.ca/residents/open-government/data/terms/',
  'http://www.regionofwaterloo.ca/en/regionalGovernment/OpenDataLicence.asp',
  'http://www.strathcona.ca/local-government/strathcona-county-elections/election-2013-open-data/#licence',
  'http://www1.toronto.ca/wps/portal/contentonly?vgnextoid=4a37e03bb8d1e310VgnVCM10000071d60f89RCRD&vgnextfmt=default',
  'http://www5.mississauga.ca/research_catalogue/CityofMississauga_TermsofUse.pdf',
  'https://cityonline.calgary.ca/Pages/PdcTermsOfUse.aspx',
]

some_rights_reserved_licenses = [
  'http://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php',  # per CIPPIC
  'https://mli2.gov.mb.ca/app/register/app/index.php',  # no commercial redistribution
  'https://www.geosask.ca/Portal/jsp/terms_popup.jsp',  # per CIPPIC
]

all_rights_reserved_licenses = [
  'http://opendata-saskatoon.cloudapp.net/TermsOfUse/TermsOfUse',  # open data license pending
  'http://www.altalis.com/agreement.html',  # per CIPPIC
  'http://www.elections.on.ca/en-CA/Tools/ElectoralDistricts/LimitedUseDataProductLicenceAgreement.htm',  # per CIPPIC
]


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
  import boundaries
  boundaries.autodiscover(base)
  return boundaries.registry

# Reads a remote CSV file.
def csv_reader(url):
  from StringIO import StringIO
  return csv.reader(StringIO(requests.get(url).content))

# Maps Standard Geographical Classification codes to the OCD identifiers of provinces and territories.
ocd_codes_memo = {}
def ocd_codes():
  if not ocd_codes_memo:
    ocd_codes_memo['01'] = 'ocd-division/country:ca'
    reader = csv_reader('https://raw.github.com/opencivicdata/ocd-division-ids/master/mappings/country-ca-sgc/ca_provinces_and_territories.csv')
    for row in reader:
      ocd_codes_memo[row[1]] = row[0]
  return ocd_codes_memo

# Maps OCD identifiers and Standard Geographical Classification codes to names.
ocd_names_memo = {}
def ocd_names():
  if not ocd_names_memo:
    urls = [
      'https://raw.github.com/opencivicdata/ocd-division-ids/master/identifiers/country-ca/ca_manual.csv',
      'https://raw.github.com/opencivicdata/ocd-division-ids/master/identifiers/country-ca/ca_provinces_and_territories.csv',
      'https://raw.github.com/opencivicdata/ocd-division-ids/master/identifiers/country-ca/ca_census_divisions.csv',
      'https://raw.github.com/opencivicdata/ocd-division-ids/master/identifiers/country-ca/ca_census_subdivisions.csv',
      'https://raw.github.com/opencivicdata/ocd-division-ids/master/identifiers/country-ca/census_subdivision-montreal-arrondissements.csv',
    ]
    for url in urls:
      for row in csv_reader(url):
        ocd_names_memo[row[0].decode('utf8')] = row[1].decode('utf8')
  return ocd_names_memo

# Returns the Open Civic Data division identifier and Standard Geographical Classification code.
def get_ocd_division(slug, config):
  ocd_division = config['metadata'].get('ocd_division')
  geographic_code = config['metadata'].get('geographic_code')
  if ocd_division:
    if geographic_code:
      raise Exception('%s: Set ocd_division or geographic_code' % slug)
  else:
    if geographic_code:
      length = len(geographic_code)
      if length == 2:
        ocd_division = ocd_codes()[geographic_code]
      elif length == 4:
        ocd_division = 'ocd-division/country:ca/cd:%s' % geographic_code
      elif length == 7:
        ocd_division = 'ocd-division/country:ca/csd:%s' % geographic_code
      else:
        raise Exception('%s: Unrecognized geographic code %s' % (slug, geographic_code))
  return [ocd_division, geographic_code]


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


# Fix file permissions.
@task
def permissions(base='.'):
  for (dirpath, dirnames, filenames) in os.walk(base, followlinks=True):
    if '.git' in dirnames:
      dirnames.remove('.git')
    if '.DS_Store' in filenames:
      filenames.remove('.DS_Store')
    for filename in filenames:
      path = os.path.join(dirpath, filename)
      if os.stat(path).st_mode != 33188: # 100644 octal
        os.chmod(path, stat.S_IWUSR | stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)


# Check that all `definition.py` files are valid.
@task
def definitions(base='.'):
  import lxml.html

  valid_keys = set([
    # Added by boundaries.register.
    'file',
    # Used by represent-boundaries.
    'name',
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
    'metadata',
    'notes',
    'encoding',
    # Used by this script. Not validated.
    'ogr2ogr',
    'prj',
  ])

  valid_metadata_keys = set([
    'geographic_code',
    'ocd_division',
  ])

  terms = {
    # @see https://www.cippic.ca/sites/default/files/CIPPIC%20-%20How%20to%20Redistribute%20Open%20Data.pdf
    'http://ottawa.ca/en/mobile-apps-and-open-data/open-data-terms-use': 'I. Terms of Use. This work is provided under the terms of “City of Ottawa – Terms of Use” (http://ottawa.ca/en/mobile-apps-and-open-data/open-data-terms-use).  Any use of the work other than as authorized under these terms is strictly prohibited.',
    'http://www.citywindsor.ca/opendata/Documents/OpenDataTermsofUse.pdf': 'I. Terms of Use. This work is provided under the terms of “City of Windsor – Terms of Use” (http://www.citywindsor.ca/opendata/Documents/OpenDataTermsofUse.pdf).  Any use of the work other than as authorized under these terms is strictly prohibited.',
    'http://www.edmonton.ca/city_government/initiatives_innovation/open-data-terms-of-use.aspx': 'I. Terms of Use. This work is provided under the terms of City of Edmonton Open Data Terms of Use (http://www.edmonton.ca/city_government/initiatives_innovation/open-data-terms-of-use.aspx).  Any use of the work other than as authorized under these terms is strictly prohibited.',
    'http://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php': """Attribution: This data is provided by the Directeur général des élections du Québec (http://www.electionsquebec.qc.ca), reproduced according to the terms of the "Conditions d'utilisation de notre site Web" (http://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php). Copyright in the work belongs to the Government of Quebec.""",
    'http://www.london.ca/d.aspx?s=/Open_Data/Open_Data_Terms_Use.htm': 'I. Terms of Use. This work is provided under the terms of “Open Data London – Terms of Use” (http://www.london.ca/d.aspx?s=/Open_Data/Open_Data_Terms_Use.htm).  Any use of the work other than as authorized under these terms is strictly prohibited.',
    'http://www5.mississauga.ca/research_catalogue/CityofMississauga_TermsofUse.pdf': 'I. Terms of Use. This work is provided under the terms of “City of Mississauga – Terms of Use” (http://www.mississauga.ca/file/COM/CityOfMississaugaTermsOfUse.pdf).  Any use of the work other than as authorized under these terms is strictly prohibited.',
    'https://cityonline.calgary.ca/Pages/PdcTermsOfUse.aspx': 'I. Terms of Use. This data is provided by the City of Calgary and is made available under the Open Data Catalogue Terms of Use (https://cityonline.calgary.ca/Pages/PdcTermsOfUse.aspx).',
    # Open Government Licence.
    'http://data.gc.ca/eng/open-government-licence-canada': 
      'I. Terms of Use. Contains information licensed under the Open Government Licence – Canada (http://data.gc.ca/eng/open-government-licence-canada).',
    'http://www.countygp.ab.ca/EN/main/community/maps-gis/open-data/open-data-licence.html': 
      'I. Terms of Use. Contains information licensed under the Open Government Licence – County of Grande Prairie (http://www.countygp.ab.ca/EN/main/community/maps-gis/open-data/open-data-licence.html).',
    'http://www.nanaimo.ca/EN/main/departments/106/DataCatalogue/Licence.html':
      'I. Terms of Use. Contains information licensed under the Open Government Licence - Nanaimo (http://www.nanaimo.ca/EN/main/departments/106/DataCatalogue/Licence.html).',
    'http://www.strathcona.ca/local-government/strathcona-county-elections/election-2013-open-data/#licence':
      'I. Terms of Use. Contains information licensed under the Open Government Licence – Strathcona County (http://www.strathcona.ca/local-government/strathcona-county-elections/election-2013-open-data/#licence).',
    'http://www1.toronto.ca/wps/portal/contentonly?vgnextoid=4a37e03bb8d1e310VgnVCM10000071d60f89RCRD&vgnextfmt=default':
      'I. Terms of Use. Contains information licensed under the Open Government Licence – Toronto (http://www1.toronto.ca/wps/portal/contentonly?vgnextoid=4a37e03bb8d1e310VgnVCM10000071d60f89RCRD&vgnextfmt=default).',
    # Text provided by license.
    'http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/': "I. Termes d'utilisation. Contient des données reproduites, modifiées, traduites ou distribuées « telles quelles » avec la permission de la Ville de Montréal (http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/).",
    'http://donnees.ville.quebec.qc.ca/licence.aspx': "I. Conditions d'utilisation. Contient des données reproduites et distribuées « telles quelles » avec la permission de la Ville de Québec (http://donnees.ville.quebec.qc.ca/licence.aspx).",
    'http://opendata.peelregion.ca/terms-of-use.aspx': "I. Terms of Use. Contains public sector Information made available under The Regional Municipality of Peel's Open Data Licence - Version 1.0 (http://opendata.peelregion.ca/terms-of-use.aspx).",
    'http://www.electionspei.ca/apilicense': 'I. Terms of Use. This information is provided by Elections PEI under the Elections PEI Data License (http://www.electionspei.ca/apilicense).',
    'http://www.hamilton.ca/NR/rdonlyres/C58984A4-FE11-40B9-A231-8572EB922AAA/0/OpenDataTermsAndConditions_Final.htm': "I. Terms of Use. Contains public sector Data made available under the City of Hamilton’s Open Data Licence (http://www.hamilton.ca/NR/rdonlyres/C58984A4-FE11-40B9-A231-8572EB922AAA/0/OpenDataTermsAndConditions_Final.htm).",
    'http://www.milton.ca/en/resourcesGeneral/Open_Data/Milton_Open_Data_Terms_V1.pdf': "I. Terms of Use. Contains public sector Datasets made available under the Town of Milton's Open Data License v.1 (http://www.milton.ca/en/resourcesGeneral/Open_Data/Milton_Open_Data_Terms_V1.pdf).",
    'http://www.regionofwaterloo.ca/en/regionalGovernment/OpenDataLicence.asp': 'I. Terms of Use. Contains information provided by the Regional Municipality of Waterloo under licence (http://www.regionofwaterloo.ca/en/regionalGovernment/OpenDataLicence.asp).',
    # Kent Mewhort email (2012-02-10).
    'https://mli2.gov.mb.ca/app/register/app/index.php': '© 2001 Her Majesty the Queen in Right of Manitoba, as represented by the Minister of Conservation. All rights reserved. Distributed under the terms of the Manitoba Land Initiative Terms and Conditions of Use (https://mli2.gov.mb.ca//app/register/app/index.php).',
  }

  terms_re = {
    # @see https://www.cippic.ca/sites/default/files/CIPPIC%20-%20How%20to%20Redistribute%20Open%20Data.pdf
    'https://www.geosask.ca/Portal/jsp/terms_popup.jsp': re.compile("\AAttribution: (Source|Adapted from): Her Majesty In Right Of Saskatchewan or Information Services Corporation of Saskatchewan, [^.]+\. The incorporation of data sourced from Her Majesty In Right Of Saskatchewan and/or Information Services Corporation of Saskatchewan, within this product shall not be construed as constituting an endorsement by Her Majesty In Right Of Saskatchewan or Information Services Corporation of Saskatchewan of such product\.\Z"),
  }

  all_rights_reserved_terms_re = re.compile('\ADistributed with permission from .+?.  Please direct licensing inquiries and requests to:\n\n')

  authorities = [
    u'Elections Prince Edward Island',
    u'Regional Municipality of Peel',
    u'Regional Municipality of Waterloo',
    u'Ville de Montréal',
  ]

  # Map census type codes to names.
  census_division_type_names = {}
  document = lxml.html.fromstring(requests.get('http://www12.statcan.gc.ca/census-recensement/2011/ref/dict/table-tableau/table-tableau-4-eng.cfm').content)
  for abbr in document.xpath('//table/tbody/tr/th[1]/abbr'):
    census_division_type_names[abbr.text_content()] = re.sub(' /.+\Z', '', abbr.attrib['title'])
  census_subdivision_type_names = {}
  document = lxml.html.fromstring(requests.get('http://www12.statcan.gc.ca/census-recensement/2011/ref/dict/table-tableau/table-tableau-5-eng.cfm').content)
  for abbr in document.xpath('//table/tbody/tr/th[1]/abbr'):
    census_subdivision_type_names[abbr.text_content()] = re.sub(' /.+\Z', '', abbr.attrib['title'])

  # Map OCD identifiers to census subdivision types.
  types = {}
  reader = csv_reader('https://raw.github.com/opencivicdata/ocd-division-ids/master/mappings/country-ca-types/ca_census_divisions.csv')
  for row in reader:
    types[row[0]] = census_division_type_names[row[1].decode('utf8')]
  reader = csv_reader('https://raw.github.com/opencivicdata/ocd-division-ids/master/mappings/country-ca-types/ca_census_subdivisions.csv')
  for row in reader:
    types[row[0]] = census_subdivision_type_names[row[1].decode('utf8')]

  codes = ocd_codes()
  names = ocd_names()
  ocd_divisions = set()

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
            print "%-50s No LICENSE.txt template for License URL %s" % (slug, licence_url)
          elif terms.get(licence_url) and license_text != terms[licence_url] or terms_re.get(licence_url) and not terms_re[licence_url].search(license_text):
            print "%-50s Expected LICENSE.txt to match license-specific template" % slug
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
      print "%-50s Unrecognized key: %s" % (slug, ', '.join(invalid_keys))
    values = [value for key, value in config.items() if key != 'metadata']
    if len(values) > len(set(values)):
      print "%-50s Non-unique values" % slug
    for key, value in config.items():
      if not value:
        print "%-50s Empty value for %s" % (slug, key)

    # Check for missing required keys.
    for key in ('domain', 'last_updated', 'name_func', 'authority', 'encoding'):
      if not config.get(key):
        print "%-50s Missing %s" % (slug, key)
    if not config.get('source_url') and (config.get('licence_url') or config.get('data_url')):
      print "%-50s Missing source_url" % slug
    if config.get('source_url') and not config.get('licence_url') and not config.get('data_url'):
      print "%-50s Missing licence_url or data_url" % slug

    # Validate fields.
    for key in ('name', 'singular'):
      if config.get(key):
        print "%-50s Expected %s to be missing" % (slug, key)
    if config.get('encoding') and config['encoding'] != 'iso-8859-1':
      print "%-50s Expected encoding to be iso-8859-1 not %s" % (slug, config['encoding'])

    if slug not in ('Census divisions', 'Census subdivisions'):
      if config.get('metadata'):
        # Check for invalid keys or empty values.
        invalid_keys = set(config['metadata'].keys()) - valid_metadata_keys
        if invalid_keys:
          print "%-50s Unrecognized key: %s" % (slug, ', '.join(invalid_keys))
        for key, value in config['metadata'].items():
          if not value:
            print "%-50s Empty value for %s" % (slug, key)

        ocd_division, geographic_code = get_ocd_division(slug, config)

        if ocd_division:
          # Ensure ocd_division is unique.
          if ocd_division in ocd_divisions:
            raise Exception('%s: Duplicate ocd_division %s' % (slug, ocd_division))
          else:
            ocd_divisions.add(ocd_division)

          sections = ocd_division.split('/')
          ocd_type, ocd_type_id = sections[-1].split(':')

          # Validate slug, domain and authority.
          name = names[ocd_division]
          if ocd_type == 'country':
            expected = 'Federal electoral districts'
            if slug != expected:
              print "%-50s Expected slug to be %s" % (slug, expected)

            if config['domain'] != name:
              print "%-50s Expected domain to be %s not %s" % (slug, name, config['domain'])

            expected = 'Her Majesty the Queen in Right of Canada'
            if config['authority'] != expected:
              print "%-50s Expected authority to be %s not %s" % (slug, expected, config['authority'])

          elif ocd_type in ('province', 'territory'):
            expected = '%s electoral districts' % name
            if slug != expected:
              print "%-50s Expected slug to be %s" % (slug, expected)

            if config['domain'] != name:
              print "%-50s Expected domain to be %s not %s" % (slug, name, config['domain'])

            expected = 'Her Majesty the Queen in Right of %s' % name
            if config['authority'] != expected:
              print "%-50s Expected authority to be %s not %s" % (slug, expected, config['authority'])

          elif ocd_type in ('cd', 'csd'):
            province_or_territory_code = ocd_type_id[:2]
            province_or_territory_abbreviation = codes[province_or_territory_code].split(':')[-1].upper()

            if province_or_territory_code == '24':
              expected = re.compile('\A%s (boroughs|districts)\Z' % name)
            else:
              expected = re.compile('\A%s (districts|divisions|wards)\Z' % name)
            if not expected.search(slug):
              print "%-50s Expected slug to match %s" % (slug, expected.pattern)

            expected = '%s, %s' % (name, province_or_territory_abbreviation)
            if config['domain'] != expected:
              print "%-50s Expected domain to be %s not %s" % (slug, expected, config['domain'])

            if province_or_territory_code == '24':
              preposition = 'de'
            else:
              preposition = 'of'
            expected = '%s %s %s' % (types[ocd_division], preposition, name)
            if config['authority'] != expected and config['authority'] not in authorities:
              print "%-50s Expected authority to be %s not %s" % (slug, expected, config['authority'])

          elif ocd_type == 'arrondissement':
            census_subdivision_ocd_division = '/'.join(sections[:-1])
            census_subdivision_name = names[census_subdivision_ocd_division]
            province_or_territory_code = census_subdivision_ocd_division.split(':')[-1][:2]
            province_or_territory_abbreviation = codes[province_or_territory_code].split(':')[-1].upper()

            expected = '%s districts' % name
            if slug != expected:
              print "%-50s Expected slug to be %s" % (slug, expected)

            expected = '%s, %s, %s' % (name, census_subdivision_name, province_or_territory_abbreviation)
            if config['domain'] != expected:
              print "%-50s Expected domain to be %s not %s" % (slug, expected, config['domain'])

            if province_or_territory_code == '24':
              preposition = 'de'
            else:
              preposition = 'of'
            expected = '%s %s %s' % (types[census_subdivision_ocd_division], preposition, census_subdivision_name)
            if config['authority'] != expected:
              print "%-50s Expected authority to be %s not %s" % (slug, expected, config['authority'])

          else:
            raise Exception('%s: Unrecognized OCD type %s' % (slug, ocd_type))
      else:
        print "%-50s Missing metadata" % slug


# Check that the source, data and license URLs work.
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
            arguments = {}
            if result.username:
              url = '%s://%s%s' % (result.scheme, result.hostname, result.path)
              arguments['auth'] = (result.username, result.password)
            response = requests.head(url, **arguments)
            status_code = response.status_code
            if status_code != 200:
              print '%d %s' % (status_code, url)
          except requests.exceptions.ConnectionError:
            print '404 %s' % url


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
              basename = 'data%s' % extension # assumes one KML or KMZ file per archive
            else:
              basename = os.path.basename(name) # assumes no collisions across hierarchy
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

  from datetime import datetime

  from rfc6266 import parse_headers

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
        response = requests.head(url, **arguments)
        if response.status_code == 405: # if HEAD requests are not allowed
          response = requests.get(url, **arguments)
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
          response = requests.get(url, **arguments)
          with open(data_file_path, 'wb') as f:
            for chunk in response.iter_content():
              f.write(chunk)

          process(slug, config, url, data_file_path)


# Update the spreadsheet for tracking progress on data collection.
@task
def spreadsheet(base='.', private_data_base='../represent-canada-private-data'):
  import sys

  codes = ocd_codes()
  names = ocd_names()
  rows = {}

  # Boundary sets
  # @todo loop over private_data_base as well (private = 'N')
  private = 'Y'
  for slug, config in registry(base).items():
    if config.get('metadata'):
      ocd_division, geographic_code = get_ocd_division(slug, config)

      if ocd_division:
        sections = ocd_division.split('/')
        ocd_type, ocd_type_id = sections[-1].split(':')

        # Determine province or territory.
        if ocd_type == 'country':
          province_or_territory = None
        elif ocd_type in ('province', 'territory'):
          province_or_territory = ocd_division
        elif ocd_type in ('cd', 'csd'):
          province_or_territory = codes[ocd_type_id[:2]]
        elif ocd_type == 'arrondissement':
          province_or_territory = codes[sections[-2].split(':')[-1][:2]]
        if province_or_territory:
          province_or_territory = province_or_territory.split(':')[-1].upper()

        row = {
          'OCD': ocd_division,
          'Geographic code': geographic_code,
          'Geographic name': names[ocd_division],
          'Province or territory': province_or_territory,
          'Shapefile?': 'Y',

          # Columns used once requested.
          'Contact': None,  # manual
          'Highrise URL': None,  # manual
          'Request notes': '',  # manual if not received

          # Columns used once received.
          'Last boundary': config.get('last_updated'),
          'Next boundary': None,  # manual
          'Permission to distribute': permission,
          'Received via': None,  # manual if MFIPPA
          'License URL': config.get('licence_url'),
          'Denial notes': None,  # manual
        }
        if config.get('data_url'):
          row['Contact'] = 'N/A'
          row['Received via'] = 'online'
        else:
          # @todo reconstruct contact from LICENSE.txt
          row['Received via'] = 'email' # @todo MFIPPA

        directory = dirname(config['file'])
        with open(os.path.join(directory, 'LICENSE.txt')) as f:
          license_text = f.read().rstrip('\n')
        if config.get('licence_url'):
          licence_url = config['licence_url']
          if licence_url in open_data_licenses:
            row['Type of license'] = 'Open'
          elif licence_url in some_rights_reserved_licenses:
            row['Type of license'] = 'Most rights reserved'
          elif licence_url in all_rights_reserved_licenses:
            row['Type of license'] = 'All rights reserved'
        else:
          # @todo License agreements
          row['Type of license'] = 'Unlicensed'

        rows.append(row)
      else:
        print 'No OCD division for %s' % slug

  # Representative sets
  # reader = csv_reader('https://raw.github.com/opencivicdata/ocd-division-ids/master/mappings/country-ca-abbr/ca_provinces_and_territories.csv')
  # abbreviations = [row[1] for row in reader]

  # Map Standard Geographical Classification codes to ScraperWiki URLs.
  # @see https://github.com/opennorth/represent-canada/issues/60
  # scraperwiki_urls = {}
  # for representative_set in requests.get('http://represent.opennorth.ca/representative-sets/?limit=0').json()['objects']:
  #   boundary_set_url = representative_set['related']['boundary_set_url']
  #   if boundary_set_url:
  #     boundary_set = requests.get('http://represent.opennorth.ca%s' % boundary_set_url).json()
  #     if boundary_set.get('metadata') and boundary_set['metadata'].get('geographic_code'):
  #       scraperwiki_urls[boundary_set['metadata']['geographic_code']] = representative_set['scraperwiki_url']
  #     else:
  #       print '%-65s No metadata' % boundary_set_url
  #   else:
  #     print "%-65s No boundary_set_url" % representative_set['url']

  # @todo track if scraped in bulk via Represent API?

  # Map to Pupa modules.
  # @todo check for pupa scrapers

  # geographic_name_re = re.compile('\A(.+) \((.+)\)\Z')
  # reader = csv_reader('http://www12.statcan.gc.ca/census-recensement/2011/dp-pd/hlt-fst/pd-pl/FullFile.cfm?T=301&LANG=Eng&OFT=CSV&OFN=98-310-XWE2011002-301.CSV')
  # writer = csv.writer(sys.stdout)
  # reader.next() # title
  # reader.next() # headers
  # rows = {}
  # for row in reader:
  #   if row:
  #     result = geographic_name_re.search(row[1])
  #     if result:
  #       name = result.group(1)
  #       province_or_territory = result.group(2)
  #       if province_or_territory not in abbreviations:
  #         raise Exception('Unrecognized province or territory "%s" in "%s"' % (province_or_territory, row[1]))
  #     elif row[1] == 'Canada':
  #       name = 'Canada'
  #       province_or_territory = 'Canada'
  #     else:
  #       raise Exception('Unrecognized name "%s"' % row[1])
  #     writer.writerow([
  #       row[0],
  #       name,
  #       province_or_territory,
  #       row[4],
  #       scraperwiki_urls.get(row[0]),
  #     ])
  #   else:
  #     break

  # @todo compare against live spreadsheet, log any conflicts

  # Reads the spreadsheet for tracking progress on data collection.
  # reader = csv_reader('https://docs.google.com/spreadsheet/pub?key=0AtzgYYy0ZABtdGpJdVBrbWtUaEV0THNUd2JIZ1JqM2c&single=true&gid=18&output=csv')
  # reader.next() # headers
  # live = dict((row[0], row[1:]) for row in reader)

  # if no conflicts, update live spreadsheet?
  # https://code.google.com/p/gdata-python-client/
