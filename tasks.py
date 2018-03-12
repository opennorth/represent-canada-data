# coding: utf-8
import csv
import os
import os.path
import re
import socket
import stat
import sys
from collections import OrderedDict
from datetime import date, datetime, timedelta
from ftplib import FTP
from glob import glob
from io import StringIO
from urllib.parse import urlparse
from zipfile import ZipFile, BadZipfile

import boundaries
import requests
from invoke import run, task
from opencivicdata.divisions import Division
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from rfc6266 import parse_headers

from constants import (
    more_licenses_with_templates,
    all_rights_reserved_licenses,
    all_rights_reserved_terms_re,
    terms,
    terms_re,
    valid_keys,
    authorities,
    quartiers,
    municipal_subdivisions,
    default_expectation,
)

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

province_or_territory_abbreviation_memo = {}
divisions_with_boroughs_memo = set()
ocd_division_csv = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'country-ca.csv')


def dirname(path):
    """
    Returns the directory in which a shapefile exists.
    """
    # GitPython can't handle paths starting with "./".
    if path.startswith('./'):
        path = path[2:]
    if os.path.isdir(path):
        return path
    else:
        return os.path.dirname(path)


def registry(base='.'):
    """
    Reads definition.py files.
    """
    boundaries.autodiscover(base)
    return boundaries.registry


def csv_dict_reader(url, encoding='utf-8'):
    """
    Reads a remote CSV file.
    """
    response = requests.get(url)
    response.encoding = encoding
    return csv.DictReader(StringIO(response.text))


def province_or_territory_abbreviation(code):
    if not province_or_territory_abbreviation_memo:
        for division in Division.all('ca', from_csv=ocd_division_csv):
            if division._type in ('province', 'territory'):
                province_or_territory_abbreviation_memo[division.attrs['sgc']] = type_id(division.id).upper()
    return province_or_territory_abbreviation_memo[type_id(code)[:2]]


def divisions_with_boroughs():
    """
    Returns the OCD identifiers for divisions with boroughs.
    """
    if not divisions_with_boroughs_memo:
        for division in Division.all('ca', from_csv=ocd_division_csv):
            if division._type == 'borough':
                divisions_with_boroughs_memo.add(division.parent.id)
    return divisions_with_boroughs_memo


def type_id(id):
    """
    Returns an OCD identifier's type ID.
    """
    return id.rsplit(':', 1)[1]


def get_definition(division_id, path=None):
    """
    Returns the expected contents of a definition file.
    """
    config = {}

    division = Division.get(division_id, from_csv=ocd_division_csv)

    # Determine slug, domain and authority.
    name = division.name
    if not name:
        print('%-60s unknown name: check slug and domain manually' % division.id)

    if division._type == 'country':
        slug = 'Federal electoral districts'
        config['domain'] = name
        config['authority'] = ['Her Majesty the Queen in Right of Canada']

    elif division._type in ('province', 'territory'):
        slug = '%s electoral districts' % name
        config['domain'] = name
        config['authority'] = ['Her Majesty the Queen in Right of %s' % name]

    elif division._type in ('cd', 'csd'):
        province_or_territory_sgc_code = type_id(division.id)[:2]

        if province_or_territory_sgc_code == '24' and division.id in divisions_with_boroughs():
            slug = re.compile('\A%s (boroughs|districts)\Z' % name)
        elif province_or_territory_sgc_code == '12' and division.attrs['classification'] != 'T':
            slug = '%s districts' % name
        elif province_or_territory_sgc_code == '47' and division.attrs['classification'] != 'CY':
            slug = '%s divisions' % name
        elif province_or_territory_sgc_code == '48' and division.attrs['classification'] == 'MD':
            slug = '%s divisions' % name
        elif province_or_territory_sgc_code == '24':
            if division.id in quartiers:
                slug = '%s quartiers' % name
            else:
                slug = '%s districts' % name
        else:
            slug = '%s wards' % name

        config['domain'] = '%s, %s' % (name, province_or_territory_abbreviation(division.id))

        if province_or_territory_sgc_code == '12' and 'boundaries/ca_ns_districts/' in path:
            config['authority'] = ['Her Majesty the Queen in Right of Nova Scotia']
        elif province_or_territory_sgc_code == '13' and 'boundaries/ca_nb_wards/' in path:
            config['authority'] = ['Her Majesty the Queen in Right of New Brunswick']
        elif province_or_territory_sgc_code == '24' and 'boundaries/ca_qc_' in path:
            config['authority'] = ['Directeur général des élections du Québec']
        elif province_or_territory_sgc_code == '47' and division.attrs['classification'] != 'CY':
            config['authority'] = ['MuniSoft']
        elif division._type == 'csd':
            config['authority'] = authorities + [division.attrs['organization_name']]
        else:
            config['authority'] = ['']  # We have no expectation for the authority of a Census division

    elif division._type == 'borough':
        province_or_territory_sgc_code = type_id(division.parent.id)[:2]

        if name:
            slug = '%s districts' % name
            config['domain'] = '%s, %s, %s' % (name, division.parent.name, province_or_territory_abbreviation(division.parent.id))
        else:
            slug = None
            config['domain'] = None

        if province_or_territory_sgc_code == '24':
            config['authority'] = ['Directeur général des élections du Québec']
        else:
            config['authority'] = [division.parent.attrs['organization_name']]

    else:
        raise Exception('%s: Unrecognized OCD type %s' % (division.id, division._type))

    return (slug, config)


@task
def define(division_id):
    """
    Print the contents of a definition file.
    """
    slug, config = get_definition(division_id)
    if isinstance(slug, re._pattern_type):
        slug = re.sub('\\\[AZ]', '', slug.pattern)

    config['slug'] = slug
    config['last_updated'] = datetime.now().strftime('%Y, %-m, %-d')
    config['authority'] = config['authority'][-1]
    config['division_id'] = division_id

    print("""from datetime import date

import boundaries

boundaries.register('%(slug)s',
        domain='%(domain)s',
        last_updated=date(%(last_updated)s),
        name_func=boundaries.attr(''),
        id_func=boundaries.attr(''),
        authority='%(authority)s',
        encoding='iso-8859-1',
        extra={'division_id': '%(division_id)s'},
)""" % config)


@task
def licenses(base='.'):
    """
    Check that all data directories contain a LICENSE.txt.
    """
    for (dirpath, dirnames, filenames) in os.walk(base, followlinks=True):
        for dirname in ('.git', '__pycache__'):
            if dirname in dirnames:
                dirnames.remove(dirname)
        for filename in ('.DS_Store', 'empty.csv'):
            if filename in filenames:
                filenames.remove(filename)
        if filenames and 'LICENSE.txt' not in filenames:
            print('%s No LICENSE.txt' % dirpath)


@task
def permissions(base='.'):
    """
    Fix file permissions.
    """
    for (dirpath, dirnames, filenames) in os.walk(base, followlinks=True):
        if '.git' in dirnames:
            dirnames.remove('.git')
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            if filename not in 'update.sh' and os.stat(path).st_mode != 33188:  # 100644 octal
                os.chmod(path, stat.S_IWUSR | stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)


@task
def definitions(base='.'):
    """
    Check that all definition.py files are valid.
    """
    def warn(message, slug):
        if message not in seen:
            print('%-60s %s' % (slug, message))
            seen.add(message)

    def assert_match(slug, field, actual, expected):
        if isinstance(expected, re._pattern_type):
            if not expected.search(actual):
                print('%-60s Expected %s to match %s not %s' % (slug, field, expected.pattern, actual))
        elif isinstance(expected, list):
            if actual not in expected:
                print('%-60s Expected %s to be %s not %s' % (slug, field, expected[-1], actual))
        elif actual != expected and expected is not None:
            print('%-60s Expected %s to be %s not %s' % (slug, field, expected, actual))

    response = requests.get('https://docs.google.com/spreadsheets/d/1AmLQD2KwSpz3B4eStLUPmUQJmOOjRLI3ZUZSD5xUTWM/pub?gid=0&single=true&output=csv')
    response.encoding = 'utf-8'
    reader = csv.DictReader(StringIO(response.text))
    licenses_with_templates = set(filter(None, (row['License URL'] for row in reader)))
    licenses_with_templates.update(more_licenses_with_templates)

    seen = set()
    division_ids = set()
    for slug, config in registry(base).items():
        directory = dirname(config['file'])

        if config.get('extra'):
            division_id = config['extra']['division_id']
            ocd_type = division_id.rsplit('/', 1)[1].split(':')[0]
        else:
            division_id = None
            ocd_type = None

        # Validate LICENSE.txt.
        license_path = os.path.join(directory, 'LICENSE.txt')
        if os.path.exists(license_path):
            with open(license_path) as f:
                license_text = f.read().rstrip('\n')
            if 'licence_url' in config:
                licence_url = config['licence_url']
                if licence_url in licenses_with_templates:
                    if licence_url not in terms and not terms_re.get(licence_url):
                        warn('No LICENSE.txt template for License URL %s' % licence_url, slug)
                    elif licence_url in terms and license_text != terms[licence_url] or terms_re.get(licence_url) and not terms_re[licence_url].search(license_text):
                        print('%-60s Expected LICENSE.txt to match license-specific template' % slug)
                elif licence_url in all_rights_reserved_licenses:
                    if not all_rights_reserved_terms_re.search(license_text):
                        print('%-60s Expected LICENSE.txt to match "all rights reserved" template' % slug)
                else:
                    print('%-60s Unrecognized License URL %s' % (slug, licence_url))
            elif not all_rights_reserved_terms_re.search(license_text):
                print('%-60s Expected LICENSE.txt to match "all rights reserved" template' % slug)

        # Check for invalid keys, non-unique or empty values.
        invalid_keys = set(config.keys()) - valid_keys
        if invalid_keys:
            print('%-60s Unrecognized key: %s' % (slug, ', '.join(invalid_keys)))
        values = [value for key, value in config.items() if key != 'extra']
        if len(values) > len(set(values)):
            print('%-60s Non-unique values' % slug)
        for key, value in config.items():
            if not value:
                print('%-60s Empty value for %s' % (slug, key))

        # Check for missing required keys.
        for key in ('domain', 'last_updated', 'name_func', 'authority', 'encoding'):
            if key not in config:
                print('%-60s Missing %s' % (slug, key))
        if 'source_url' not in config and 'data_url' in config:
            print('%-60s Missing source_url' % slug)
        if 'source_url' in config and 'licence_url' not in config and 'data_url' not in config:
            print('%-60s Missing licence_url or data_url' % slug)

        # Validate fields.
        if 'name' in config:
            print('%-60s Expected name to be missing' % slug)
        if 'singular' in config and not slug.endswith(')') and ocd_type not in ('country', 'province', 'territory'):
            print('%-60s Expected singular to be missing' % slug)

        if slug not in ('Census divisions', 'Census subdivisions'):
            # Check for invalid keys or empty values.
            invalid_keys = set(config['extra'].keys()) - {'division_id'}
            if invalid_keys:
                print('%-60s Unrecognized key: %s' % (slug, ', '.join(invalid_keys)))
            for key, value in config['extra'].items():
                if not value:
                    print('%-60s Empty value for %s' % (slug, key))

            # Ensure division_id is unique.
            if division_id in division_ids and division_id not in divisions_with_boroughs() and ocd_type not in ('country', 'province', 'territory'):
                print('%-60s Duplicate division_id %s' % (slug, division_id))
            else:
                division_ids.add(division_id)

            expected_slug, expected_config = get_definition(division_id, path=config['file'])

            # Check for unexpected values.
            if not slug.endswith(')'):
                assert_match(slug, 'slug', slug, expected_slug)
            for key, value in expected_config.items():
                assert_match(slug, key, config[key], value)


@task
def urls(base='.'):
    """
    Check that the source, data and license URLs work.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)'}

    seen = set()
    for slug, config in registry(base).items():
        for key in ('source_url', 'licence_url', 'data_url'):
            if key in config:
                url = config[key]
                if url not in seen:
                    seen.add(url)

                    result = urlparse(url)
                    if result.scheme == 'ftp':
                        ftp = FTP(result.hostname)
                        ftp.login(result.username, result.password)
                        ftp.cwd(os.path.dirname(result.path))
                        if os.path.basename(result.path) not in ftp.nlst():
                            print('404 %s' % url)
                        ftp.quit()
                    else:
                        try:
                            arguments = {}
                            if result.username:
                                url = '%s://%s%s' % (result.scheme, result.hostname, result.path)
                                arguments['auth'] = (result.username, result.password)
                            try:
                                response = requests.head(url, headers=headers, **arguments)
                            except requests.exceptions.SSLError:
                                response = requests.head(url, verify=False, headers=headers, **arguments)
                            # If HEAD requests are not properly supported.
                            if response.status_code in (204, 403, 405, 500) or (response.status_code == 302 and '404' in response.headers['Location']):
                                response = requests.get(url, stream=True, **arguments)
                            if response.status_code != 200:
                                print('%d %s' % (response.status_code, url))
                        except requests.exceptions.ConnectionError:
                            print('404 %s' % url)
                        except socket.error:
                            errno, errstr = sys.exc_info()[:2]
                            if errno == socket.timeout:
                                print('Timeout %s' % url)
                            else:
                                print('%s %s' % (errstr, url))


@task
def manual(base='.'):
    """
    Print manually updated boundaries that were last updated over a year ago.
    """
    historical_slugs = {
        'Saskatchewan electoral districts (Representation Act, 2002)',
    }

    messages = []

    seen = set()
    for slug, config in registry(base).items():
        last_updated = config['last_updated']
        if 'data_url' not in config and slug not in historical_slugs and last_updated < date.today() - timedelta(days=365):
            directory = dirname(config['file'])
            if directory not in seen:
                message = '%s %-55s %-25s %s' % (last_updated, directory, config['domain'], config.get('source_url', ''))
                notes = config.get('notes')
                if notes:
                    message += '\n%s\n' % notes
                messages.append(message)
                seen.add(directory)

    for message in sorted(messages):
        print(message)


@task
def shapefiles(base='.'):
    """
    Update any out-of-date shapefiles.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)'}

    def process(slug, config, url, data_file_path):
        # We can only process KML, KMZ and ZIP files.
        extension = os.path.splitext(data_file_path)[1]
        if extension in ('.kml', '.kmz', '.zip'):
            repo_path = os.path.dirname(data_file_path)
            while not os.path.exists(os.path.join(repo_path, '.git')) and not repo_path == '/':
                repo_path = os.path.join(repo_path, '..')
            repo_path = os.path.realpath(repo_path)

            directory = dirname(config['file'])

            # Remove old files.
            for basename in os.listdir(directory):
                if basename not in ('.DS_Store', '__pycache__', 'definition.py', 'LICENSE.txt', 'data.kml', 'data.kmz', 'data.zip'):
                    os.unlink(os.path.join(directory, basename))

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
                            with zip_file.open(name, 'r') as fp:
                                if 'skip_crc32' in config:
                                    fp._expected_crc = None
                                f.write(fp.read())
                        if extension not in ('.kml', '.kmz'):
                            files_to_add.append(os.path.join(directory, basename))
                except BadZipfile as e:
                    error_thrown = True
                    print('Bad ZIP file %s %s\n' % (e, url))
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
                    print('Bad KMZ file %s\n' % url)
                finally:
                    os.unlink(kmz_file_path)

            if not error_thrown:
                shp_file_path = glob(os.path.join(directory, '*.shp'))

                # Convert any KML to shapefile.
                if not shp_file_path:
                    kml_file_path = os.path.join(directory, 'data.kml')
                    if os.path.exists(kml_file_path):
                        result = run('ogrinfo -q %s | grep -v "3D Point"' % kml_file_path, hide='out').stdout
                        if result.count('\n') > 1:
                            print('Too many layers %s' % url)
                        else:
                            layer = re.search('\A\d+: (.+?) \(', result).group(1)
                            run('ogr2ogr -f "ESRI Shapefile" %s %s -nlt POLYGON "%s"' % (directory, kml_file_path, layer), echo=True)
                            for name in glob(os.path.join(directory, '*.[dps][bhr][fjpx]')):
                                files_to_add.append(name)
                            os.unlink(kml_file_path)

                # Merge multiple shapefiles into one.
                if len(shp_file_path) > 1:
                    for name in shp_file_path:
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
                        print('Too many layers %s' % url)
                    elif re.search('3D Polygon', result):
                        run('ogr2ogr -f "ESRI Shapefile" -overwrite %s %s -nlt POLYGON' % (directory, shp_file_path), echo=True)
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
                    elif 'prj' in config:
                        with open(prj_file_path, 'w') as f:
                            f.write(requests.get(config['prj']).text)
                        files_to_add.append(prj_file_path)
                    else:
                        print('No PRJ file %s' % url)

                # Update last updated timestamp.
                definition_path = os.path.join(directory, 'definition.py')
                with open(definition_path) as f:
                    definition = f.read()
                with open(definition_path, 'w') as f:
                    f.write(re.sub('(?<=last_updated=date\()[\d, ]+', last_updated.strftime('%Y, %-m, %-d'), definition))

                # Print notes.
                if 'notes' in config:
                    print('%s\n%s\n' % (config['file'], config['notes']))
        else:
            print('Unrecognized extension %s\n' % url)

    # Retrieve shapefiles.
    processed = set()
    for slug, config in registry(base).items():
        if config['file'] not in processed and 'data_url' in config:
            processed.add(config['file'])
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
                arguments = {}
                if result.username:
                    url = '%s://%s%s' % (result.scheme, result.hostname, result.path)
                    arguments['auth'] = (result.username, result.password)
                response = requests.head(url, headers=headers, **arguments)
                # If HEAD requests are not properly supported.
                if response.status_code in (204, 403, 405, 500) or (response.status_code == 302 and '404' in response.headers['Location']):
                    response = requests.get(url, headers=headers, stream=True, **arguments)

                last_modified = response.headers.get('last-modified')

                # Parse the timestamp as a date.
                if last_modified:
                    last_updated = datetime.strptime(last_modified, '%a, %d %b %Y %H:%M:%S GMT')
                else:
                    last_updated = datetime.now()
                last_updated = last_updated.date()

                if config['last_updated'] > last_updated:
                    print('%s are more recent than the source (%s > %s)\n' % (slug, config['last_updated'], last_updated))
                elif config['last_updated'] < last_updated:
                    # Determine the file extension.
                    if 'content-disposition' in response.headers:
                        filename = parse_headers(response.headers['content-disposition']).filename_unsafe
                    else:
                        filename = url

                    extension = os.path.splitext(filename)[1].lower()
                    if not extension:
                        if response.headers['content-type'] == 'application/vnd.google-earth.kml+xml; charset=utf-8':
                            extension = '.kml'

                    # Set the new file's name.
                    data_file_path = os.path.join(dirname(config['file']), 'data%s' % extension)

                    # Download new file.
                    arguments['stream'] = True
                    response = requests.get(url, headers=headers, **arguments)
                    with open(data_file_path, 'wb') as f:
                        for chunk in response.iter_content():
                            f.write(chunk)

                    process(slug, config, url, data_file_path)


@task
def spreadsheet(base='.', private_base='../represent-canada-private-data'):
    """
    Validate the spreadsheet for tracking progress on data collection.
    """
    expecteds = OrderedDict()

    # Append to `municipal_subdivisions` from `constants.py`.
    for division in Division.all('ca', from_csv=ocd_division_csv):
        if division.attrs['has_children']:
            municipal_subdivisions[type_id(division.id)] = division.attrs['has_children']

    expecteds['ocd-division/country:ca'] = default_expectation.copy()
    expecteds['ocd-division/country:ca'].update({
        'OCD': 'ocd-division/country:ca',
        'Geographic name': 'Canada',
    })

    # Create expectations for provinces and territories.
    for division in Division.all('ca', from_csv=ocd_division_csv):
        if division._type in ('province', 'territory'):
            expected = default_expectation.copy()
            expected.update({
                'OCD': division.id,
                'Geographic name': division.name,
                'Province or territory': type_id(division.id).upper(),
            })

            expecteds[division.id] = expected

    # Create expectations for census subdivisions.
    reader = csv_dict_reader('http://www12.statcan.gc.ca/census-recensement/2016/dp-pd/hlt-fst/pd-pl/Tables/CompFile.cfm?Lang=Eng&T=301&OFT=FULLCSV', 'ISO-8859-1')
    for row in reader:
        code = row['Geographic code']

        if code == 'Note:':
            break

        division = Division.get('ocd-division/country:ca/csd:%s' % row['Geographic code'], from_csv=ocd_division_csv)

        expected = default_expectation.copy()
        expected.update({
            'OCD': division.id,
            'Geographic name': division.name,
            'Province or territory': province_or_territory_abbreviation(division.id),
            'Geographic type': division.attrs['classification'],
            'Population': row['Population, 2016'],
        })

        if code in municipal_subdivisions:
            if municipal_subdivisions[code] == 'N':
                expected['Shapefile?'] = 'N/A'
                expected['Contact'] = 'N/A'
                expected['Received via'] = 'N/A'
                expected['Last boundary'] = 'N/A'
                expected['Permission to distribute'] = 'N/A'
            elif municipal_subdivisions[code] == 'Y':
                expected['Shapefile?'] = 'Request'

        expecteds[division.id] = expected

    # Merge information from received data.
    for directory, permission_to_distribute in [(base, 'Y'), (private_base, 'N')]:
        boundaries.registry = {}
        for slug, config in registry(directory).items():
            if 'extra' in config:
                division_id = config['extra']['division_id']
                if division_id in expecteds:
                    license_path = os.path.join(dirname(config['file']), 'LICENSE.txt')
                    license_text = ''
                    if os.path.exists(license_path):
                        with open(license_path) as f:
                            license_text = f.read().rstrip('\n')

                    expected = expecteds[division_id]
                    expected['Shapefile?'] = 'Y'
                    expected['Permission to distribute'] = permission_to_distribute

                    if 'data_url' in config:
                        expected['Last boundary'] = 'N/A'
                    elif 'last_updated' in config:
                        expected['Last boundary'] = config['last_updated'].strftime('%-m/%-d/%Y')

                    if 'source_url' in config:
                        expected['Contact'] = 'N/A'
                        expected['Received via'] = 'online'
                    elif expected['Province or territory'] == 'SK' and expected['Geographic type'] == 'RM':
                        expected['Contact'] = 'Mikael Nagel\nMapping Technician\nTel: 1-306-569-2988 x205\nToll free: 1-800-663-6864\nmaps@munisoft.ca'
                        expected['Received via'] = 'purchase'
                    else:
                        match = all_rights_reserved_terms_re.search(license_text)
                        if match:
                            expected['Contact'] = match.group(1)
                        expected['Received via'] = 'email'
                # The spreadsheet doesn't track borough boundaries.
                elif '/borough:' not in division_id:
                    sys.stderr.write('%-25s no record\n' % division_id)
            else:
                sys.stderr.write('%-25s no extra\n' % slug)

    response = requests.get('https://docs.google.com/spreadsheets/d/1ihCIDc9EtvxF7kzPg3Yk6e928DN7JzaycH92IBYr0QU/pub?gid=25&single=true&output=csv')
    response.encoding = 'utf-8'
    reader = csv.DictReader(StringIO(response.text))

    actuals = set()
    for actual in reader:
        expected = expecteds[actual['OCD']]
        actuals.add(actual['OCD'])

        for key in actual.keys() - ('Population', 'URL', 'Request notes', 'Next boundary', 'Response notes'):
            e = expected[key]
            a = actual[key]

            # Note: Some of the following conditions are repetitive for readability.
            if e != a:
                # Change expectations for in-progress requests.
                if expected['Shapefile?'] == 'Request' and actual['Shapefile?'] == 'Requested' and (
                   # Request sent.
                   (key == 'Shapefile?' and e == 'Request' and a == 'Requested') or
                   # Contact found.
                   (key == 'Contact' and not e and a)):
                    continue

                # Some provinces and territories have missing expectations, in which case we defer to the spreadsheet.
                elif actual['Province or territory'] in ('ON', 'MB') and not expected['Shapefile?'] and (
                   # We determined that we needed to request boundaries.
                   (key == 'Shapefile?' and not e and a in ('Request', 'Requested')) or
                   # We determined that we needed to request boundaries, and did so.
                   (actual['Shapefile?'] == 'Requested' and key == 'Contact' and not e and a)):
                    continue

                # Contacts for private data are only stored in the spreadsheet.
                elif ((expected['Permission to distribute'] == 'N' and key == 'Contact' and not e and a) or
                      # MFIPPA receptions are only stored in the spreadsheet.
                      (key == 'Received via' and e == 'email' and a == 'MFIPPA')):
                    continue

                sys.stderr.write('%-25s %s: expected "%s" got "%s"\n' % (key, actual['OCD'], e, a))

    for division_id in expecteds.keys() - actuals:
        record = expecteds[division_id]
        if record['Shapefile?'] != 'N/A':
            sys.stderr.write('%s\t%s\t%s\t%s\t%s\n' % (division_id, record['Geographic name'], record['Province or territory'], record['Geographic type'], record['Population']))

    for division_id in actuals - expecteds.keys():
        sys.stderr.write('Remove %s\n' % division_id)
