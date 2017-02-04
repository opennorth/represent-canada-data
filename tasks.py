# coding: utf-8
from __future__ import unicode_literals

import csv
import os
import os.path
import re
import socket
import stat
import sys
from collections import defaultdict, OrderedDict
from datetime import datetime
from ftplib import FTP
from glob import glob
from zipfile import ZipFile, BadZipfile

import boundaries
import requests
from django.template.defaultfilters import slugify
from django.utils.six.moves.urllib.parse import urlparse
from six import StringIO
from invoke import run, task
from rfc6266 import parse_headers

from constants import (
    some_rights_reserved_licenses,
    all_rights_reserved_licenses,
    all_rights_reserved_terms_re,
    terms,
    terms_re,
    valid_keys,
    valid_extra_keys,
    authorities,
    municipal_subdivisions,
    request_headers,
    receipt_headers,
    headers,
)


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


def csv_reader(url, encoding='utf-8'):
    """
    Reads a remote CSV file.
    """
    response = requests.get(url)
    response.encoding = encoding
    return csv.reader(StringIO(response.text))


sgc_code_to_ocdid_memo = {}


def sgc_code_to_ocdid():
    """
    Maps Standard Geographical Classification codes to OCD identifiers.
    """

    if not sgc_code_to_ocdid_memo:
        sgc_code_to_ocdid_memo['01'] = 'ocd-division/country:ca'
        reader = csv_reader('https://raw.githubusercontent.com/opencivicdata/ocd-division-ids/master/identifiers/country-ca/ca_provinces_and_territories.csv')
        next(reader)
        for row in reader:
            sgc_code_to_ocdid_memo[row[4]] = row[0]
        filenames = [
            'ca_census_divisions',
            'ca_census_subdivisions',
        ]
        for filename in filenames:
            reader = csv_reader('https://raw.githubusercontent.com/opencivicdata/ocd-division-ids/master/identifiers/country-ca/%s.csv' % filename)
            next(reader)
            for row in reader:
                sgc_code_to_ocdid_memo[row[0].split(':')[-1]] = row[0]
    return sgc_code_to_ocdid_memo


ocdid_to_name_memo = {}


def ocdid_to_name():
    """
    Maps OCD identifiers to names.
    """

    if not ocdid_to_name_memo:
        reader = csv_reader('https://raw.githubusercontent.com/opencivicdata/ocd-division-ids/master/identifiers/country-ca.csv')
        next(reader)
        for row in reader:
            ocdid_to_name_memo[row[0]] = row[1]
    return ocdid_to_name_memo


ocdid_to_type_memo = {}


def ocdid_to_type():
    """
    Maps OCD identifiers to types.
    """

    if not ocdid_to_type_memo:
        filenames = [
            'ca_census_divisions',
            'ca_census_subdivisions',
        ]
        for filename in filenames:
            reader = csv_reader('https://raw.githubusercontent.com/opencivicdata/ocd-division-ids/master/identifiers/country-ca/%s.csv' % filename)
            next(reader)
            for row in reader:
                ocdid_to_type_memo[row[0]] = row[3]
    return ocdid_to_type_memo


corporations_memo = {}


def corporations():
    if not corporations_memo:
        reader = csv_reader('https://raw.githubusercontent.com/opencivicdata/ocd-division-ids/master/identifiers/country-ca/ca_census_subdivisions.csv')
        next(reader)
        for row in reader:
            corporations_memo[row[0]] = row[4]
    return corporations_memo


def get_definition(division_id):
    sections = division_id.split('/')
    ocd_type, ocd_type_id = sections[-1].split(':')

    config = {}

    # Determine slug, domain and authority.
    name = ocdid_to_name().get(division_id)
    if not name:
        print('%-60s unknown name: check slug and domain manually' % division_id)

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

        quartiers = [
            'ocd-division/country:ca/csd:2446080',  # Cowansville
            'ocd-division/country:ca/csd:2467025',  # Delson
            'ocd-division/country:ca/csd:2493005',  # Desbiens
            'ocd-division/country:ca/csd:2403005',  # Gaspé
            'ocd-division/country:ca/csd:2402015',  # Grande-Rivière
            'ocd-division/country:ca/csd:2469055',  # Huntingdon
            'ocd-division/country:ca/csd:2487090',  # La Sarre
            'ocd-division/country:ca/csd:2434120',  # Lac-Sergent
            'ocd-division/country:ca/csd:2483065',  # Maniwaki
            'ocd-division/country:ca/csd:2413095',  # Pohngamook
            'ocd-division/country:ca/csd:2453050',  # Saint-Joseph-de-Sorel
            'ocd-division/country:ca/csd:2489040',  # Senne-Terre
            'ocd-division/country:ca/csd:2411040',  # Trois-Pistoles
        ]

        if province_or_territory_sgc_code == '24' and division_id in boroughs:
            slug = re.compile('\A%s (boroughs|districts)\Z' % name)
        elif province_or_territory_sgc_code == '12' and ocdid_to_type()[division_id] != 'T':
            slug = '%s districts' % name
        elif province_or_territory_sgc_code == '47' and ocdid_to_type()[division_id] != 'CY':
            slug = '%s divisions' % name
        elif province_or_territory_sgc_code == '48' and ocdid_to_type()[division_id] == 'MD':
            slug = '%s divisions' % name
        elif province_or_territory_sgc_code == '24':
            if division_id in quartiers:
                slug = '%s quartiers' % name
            else:
                slug = '%s districts' % name
        else:
            slug = '%s wards' % name

        config['domain'] = '%s, %s' % (name, province_or_territory_abbreviation)

        if province_or_territory_sgc_code == '12':
            config['authority'] = ['Her Majesty the Queen in Right of Nova Scotia']
        elif province_or_territory_sgc_code == '13':
            config['authority'] = ['Her Majesty the Queen in Right of New Brunswick']
        elif province_or_territory_sgc_code == '24':
            config['authority'] = ['Directeur général des élections du Québec']
        elif province_or_territory_sgc_code == '47' and ocdid_to_type()[division_id] != 'CY':
            config['authority'] = ['MuniSoft']
        elif ocd_type == 'csd':
            config['authority'] = authorities + [corporations()[division_id]]
        else:
            config['authority'] = ['']  # We have no expectation for the authority of a Census division

    elif ocd_type == 'borough':
        census_subdivision_ocdid = '/'.join(sections[:-1])
        census_subdivision_name = ocdid_to_name()[census_subdivision_ocdid]

        province_or_territory_sgc_code = census_subdivision_ocdid.split(':')[-1][:2]
        province_or_territory_abbreviation = sgc_code_to_ocdid()[province_or_territory_sgc_code].split(':')[-1].upper()

        if name:
            slug = '%s districts' % name
            config['domain'] = '%s, %s, %s' % (name, census_subdivision_name, province_or_territory_abbreviation)
        else:
            slug = None
            config['domain'] = None

        if province_or_territory_sgc_code == '24':
            config['authority'] = ['Directeur général des élections du Québec']
        else:
            config['authority'] = [corporations()[census_subdivision_ocdid]]

    else:
        raise Exception('%s: Unrecognized OCD type %s' % (division_id, ocd_type))

    return (slug, config)


def assert_match(slug, field, actual, expected):
    if isinstance(expected, re._pattern_type):
        if not expected.search(actual):
            print('%-60s Expected %s to match %s not %s' % (slug, field, expected.pattern, actual))
    elif isinstance(expected, list):
        if actual not in expected:
            print('%-60s Expected %s to be %s not %s' % (slug, field, expected[-1], actual))
    elif actual != expected and expected is not None:
        print('%-60s Expected %s to be %s not %s' % (slug, field, expected, actual))


# @todo Guess name_func and id_func based on the shapefile.
@task
def define(division_id):
    slug, config = get_definition(division_id)
    if isinstance(slug, re._pattern_type):
        slug = re.sub('\\\[AZ]', '', slug.pattern)

    config['slug'] = slug
    config['last_updated'] = datetime.now().strftime('%Y, %-m, %-d')
    config['authority'] = config['authority'][-1]
    config['division_id'] = division_id

    print("""from __future__ import unicode_literals

from datetime import date

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
        for dirname in ('.git', '__pycache__', 'geojson', 'topojson', 'ca_qc_wip'):
            if dirname in dirnames:
                dirnames.remove(dirname)
        if '.DS_Store' in filenames:
            filenames.remove('.DS_Store')
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


# @see http://ben.balter.com/2013/06/26/how-to-convert-shapefiles-to-geojson-for-use-on-github/
@task
def topojson(base='.', output_base='./topojson'):
    sgc_code_to_ocdid_map = sgc_code_to_ocdid()
    ocdid_to_name_map = ocdid_to_name()
    readme = defaultdict(lambda: defaultdict(list))
    if 'private' in base:
        repository = 'represent-canada-private-data'
    else:
        repository = 'represent-canada-data'

    for slug, config in registry(base).items():
        if 'fed/cd' not in config['file'] and 'fed/csd' not in config['file']:  # files are too large for GitHub
            shp_file_path = config['file']
            directory = dirname(config['file'])
            name = directory + '_' + slugify(slug)
            basename = os.path.join(output_base, re.sub('[_/-]+', '_', re.sub('^/|/$', '', re.sub('^' + re.escape(base), '', name))))
            topo_json_path = basename + '.topojson'
            if not os.path.exists(topo_json_path):
                geo_json_path = basename + '.geojson'
                if not os.path.exists(geo_json_path):
                    run('ogr2ogr -f "GeoJSON" -t_srs EPSG:4326 "%s" "%s"' % (geo_json_path, shp_file_path), echo=True)
                run('topojson -o %s %s' % (topo_json_path, geo_json_path), echo=True)

            division_id = config['extra']['division_id']
            if os.stat(topo_json_path).st_size > 10485760:  # 10MB
                suffix = ' (too large to preview)'
            else:
                suffix = ''

            item = (
                slug,
                '* [%s](https://github.com/opennorth/%s/blob/master/topojson/%s#files): [API](https://represent.opennorth.ca/boundaries/%s/?limit=0)%s\n' % (
                    slug,
                    repository,
                    os.path.basename(topo_json_path),
                    slugify(slug),
                    suffix
                )
            )

            match = re.search('\Aocd-division/country:ca/csd:(\d+)', division_id)
            if match:
                readme[ocdid_to_name_map[sgc_code_to_ocdid_map[match.group(1)[:2]]]]['lower'].append(item)
            else:
                readme[ocdid_to_name_map[division_id]]['upper'].append(item)

    with open(os.path.join(output_base, 'README.md'), 'w') as f:
        f.write('# Represent API: TopoJSON\n')
        items = readme.pop('Canada', None)
        if items:
            f.write('\n## Canada\n\n')
            for part in ('upper', 'lower'):
                for slug, markdown in sorted(items[part]):
                    f.write(markdown)
        for name, items in sorted(readme.items()):
            f.write('\n## %s\n\n' % name)
            for part in ('upper', 'lower'):
                for slug, markdown in sorted(items[part]):
                    f.write(markdown)


@task
def definitions(base='.'):
    """
    Check that all definition.py files are valid.
    """
    def warn(message, slug):
        if message not in seen:
            print('%-60s %s' % (slug, message))
            seen.add(message)

    duplicate_division_ids = (
        # Multiple years.
        'ocd-division/country:ca',
        'ocd-division/country:ca/province:sk',
        # Districts and boroughs.
        'ocd-division/country:ca/csd:2458227',  # Longueuil
        'ocd-division/country:ca/csd:2466023',  # Montréal
        'ocd-division/country:ca/csd:2423027',  # Québec
        'ocd-division/country:ca/csd:2494068',  # Saguenay
        'ocd-division/country:ca/csd:2443027',  # Sherbrooke
    )

    response = requests.get('https://docs.google.com/spreadsheets/d/1AmLQD2KwSpz3B4eStLUPmUQJmOOjRLI3ZUZSD5xUTWM/pub?gid=0&single=true&output=csv')
    response.encoding = 'utf-8'
    reader = csv.DictReader(StringIO(response.text))
    open_data_licenses = set(filter(None, (row['License URL'] for row in reader)))
    open_data_licenses.add('http://www.electionspei.ca/apilicense')

    seen = set()
    division_ids = set()
    for slug, config in registry(base).items():
        directory = dirname(config['file'])

        # Validate LICENSE.txt.
        license_path = os.path.join(directory, 'LICENSE.txt')
        if os.path.exists(license_path):
            with open(license_path) as f:
                license_text = f.read().rstrip('\n')
            if 'licence_url' in config:
                licence_url = config['licence_url']
                if licence_url in open_data_licenses or licence_url in some_rights_reserved_licenses:
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
            print('%-60s Expected name to be missing' % (slug, key))
        if 'singular' in config and not slug.endswith(')'):
            print('%-60s Expected singular to be missing' % (slug, key))

        if slug not in ('Census divisions', 'Census subdivisions'):
            # Check for invalid keys or empty values.
            invalid_keys = set(config['extra'].keys()) - valid_extra_keys
            if invalid_keys:
                print('%-60s Unrecognized key: %s' % (slug, ', '.join(invalid_keys)))
            for key, value in config['extra'].items():
                if not value:
                    print('%-60s Empty value for %s' % (slug, key))

            division_id = config['extra']['division_id']

            # Ensure division_id is unique.
            if division_id in division_ids and division_id not in duplicate_division_ids:
                print('%-60s Duplicate division_id %s' % (slug, division_id))
            else:
                division_ids.add(division_id)

            expected_slug, expected_config = get_definition(division_id)

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
                            response = requests.head(url, headers=headers, **arguments)
                            if response.status_code == 405:  # if HEAD requests are not allowed
                                response = requests.get(url, headers=headers, **arguments)
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
                # Convert any KML to shapefile.
                kml_file_path = os.path.join(directory, 'data.kml')
                if os.path.exists(kml_file_path):
                    result = run('ogrinfo -q %s | grep -v "3D Point"' % kml_file_path, hide='out').stdout
                    if result.count('\n') > 1:
                        print('Too many layers %s' % url)
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
                    print('%s\n%s\n' % (slug, config['notes']))
        else:
            print('Unrecognized extension %s\n' % url)

    # Retrieve shapefiles.
    processed = set()
    for slug, config in registry(base).items():
        if slug not in processed and 'data_url' in config:
            processed.add(slug)
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
                    print('%s are more recent than the source (%s > %s)\n' % (slug, config['last_updated'], last_updated))
                elif config['last_updated'] < last_updated:
                    # Determine the file extension.
                    if 'content-disposition' in response.headers:
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
    records = OrderedDict()

    reader = csv_reader('https://raw.githubusercontent.com/opencivicdata/ocd-division-ids/master/identifiers/country-ca/ca_municipal_subdivisions-has_children.csv')
    next(reader)
    for row in reader:
        municipal_subdivisions[row[0].split(':')[-1]] = row[1]

    urls = {}
    reader = csv_reader('https://raw.githubusercontent.com/opencivicdata/ocd-division-ids/master/identifiers/country-ca/ca_census_subdivisions-url.csv')
    next(reader)
    for row in reader:
        urls[row[0].split(':')[-1]] = row[1]

    abbreviations = {}
    reader = csv_reader('https://raw.githubusercontent.com/opencivicdata/ocd-division-ids/master/identifiers/country-ca/ca_provinces_and_territories.csv')
    next(reader)
    for row in reader:
        abbreviations[row[2]] = row[0].split(':')[-1].upper()

    # Create records for provinces and territories.
    reader = csv_reader('https://raw.githubusercontent.com/opencivicdata/ocd-division-ids/master/identifiers/country-ca/ca_provinces_and_territories.csv')
    next(reader)
    for row in reader:
        records[row[0]] = {
            'OCD': row[0],
            'Geographic name': row[1],
            'Geographic type': '',
            'Province or territory': row[0].split(':')[-1].upper(),
            'Population': '',
            'URL': '',
            'Shapefile?': '',
            'Contact': '',
            'Request notes': '',
            'Received via': '',
            'Last boundary': '',
            'Next boundary': '',
            'Permission to distribute': '',
            'Highrise URL': '',
            'Response notes': '',
        }

    # Create records for census subdivisions.
    reader = csv_reader('http://www12.statcan.gc.ca/census-recensement/2011/dp-pd/hlt-fst/pd-pl/FullFile.cfm?T=301&LANG=Eng&OFT=CSV&OFN=98-310-XWE2011002-301.CSV', 'ISO-8859-1')
    next(reader)  # title
    next(reader)  # headers
    for row in reader:
        if row:
            result = re.search('\A(.+) \((.+)\)\Z', row[1])
            if result:
                name = result.group(1)
                province_or_territory = abbreviations[result.group(2)]
            elif row[1] == 'Canada':
                name = 'Canada'
                province_or_territory = ''
            else:
                raise Exception('Unrecognized name "%s"' % row[1])

            division_id = sgc_code_to_ocdid_map[row[0]]

            record = {
                'OCD': division_id,
                'Geographic name': name,
                'Province or territory': province_or_territory,
                'Geographic type': row[2],
                'Population': row[4],
                'URL': urls.get(row[0], ''),
                'Contact': '',
                'Request notes': '',
                'Received via': '',
                'Last boundary': '',
                'Next boundary': '',
                'Permission to distribute': '',
                'Highrise URL': '',
                'Response notes': '',
            }

            if row[0] in municipal_subdivisions:
                if municipal_subdivisions[row[0]] == 'N':
                    for header in ['Shapefile?'] + request_headers + receipt_headers:
                        record[header] = 'N/A'
                elif municipal_subdivisions[row[0]] == 'Y':
                    record['Shapefile?'] = 'Request'
                elif municipal_subdivisions[row[0]] == '?':
                    record['Shapefile?'] = ''
            else:
                record['Shapefile?'] = ''

            records[division_id] = record
        else:
            break

    # Merge information from received data.
    for directory, permission_to_distribute in [(base, 'Y'), (private_base, 'N')]:
        boundaries.registry = {}
        for slug, config in registry(directory).items():
            if 'extra' in config:
                division_id = config['extra']['division_id']
                if division_id in records:
                    license_path = os.path.join(dirname(config['file']), 'LICENSE.txt')
                    license_text = ''
                    if os.path.exists(license_path):
                        with open(license_path) as f:
                            license_text = f.read().rstrip('\n')

                    record = records[division_id]
                    record['Shapefile?'] = 'Y'
                    record['Permission to distribute'] = permission_to_distribute

                    if 'last_updated' in config:
                        record['Last boundary'] = config['last_updated'].strftime('%-m/%-d/%Y')

                    if 'source_url' in config:
                        record['Contact'] = 'N/A'
                        record['Received via'] = 'online'
                    else:
                        match = all_rights_reserved_terms_re.search(license_text)
                        if match:
                            record['Contact'] = match.group(1)
                        record['Received via'] = 'email'
                # The spreadsheet doesn't track borough boundaries.
                elif '/borough:' not in division_id:
                    sys.stderr.write('%-25s no record\n' % division_id)
            else:
                sys.stderr.write('%-25s no extra\n' % slug)

    response = requests.get('https://docs.google.com/spreadsheets/d/1ihCIDc9EtvxF7kzPg3Yk6e928DN7JzaycH92IBYr0QU/pub?gid=25&single=true&output=csv')
    response.encoding = 'utf-8'
    reader = csv.DictReader(StringIO(response.text))
    for row in reader:
        record = records[row['OCD']]

        for key in row:
            a = record[key]
            b = row[key]

            if a != b:
                if b and (
                    # Columns that are always tracked manually.
                   (key in ('Highrise URL', 'Request notes', 'Next boundary', 'Response notes')) or
                   # Scrapers for municipalities without wards are tracked manually.
                   (key == 'Shapefile?'       and not a         and b in ('Request', 'Requested')) or
                   # In-progress requests are tracked manually.
                   (key == 'Shapefile?'       and a == 'Request'and b == 'Requested') or
                   # Contacts for in-progress requests and private data are tracked manually.
                   (key == 'Contact'          and not a         and (row['Shapefile?'] == 'Requested' or record['Permission to distribute'] == 'N')) or
                   # We may have a contact to confirm the nonexistence of municipal subdivisions.
                   (key == 'Contact'          and a == 'N/A'    and record['Shapefile?'] == 'N/A') or
                   # MFIPPA requests are tracked manually.
                   (key == 'Received via'     and a == 'email'  and b == 'MFIPPA') or
                   # We may have information for a bad shapefile from an in-progress request.
                   (key in ('Received via', 'Permission to distribute') and not a and row['Shapefile?'] == 'Requested')):
                    record[key] = b
                # The spreadsheet can add contacts and URLs.
                elif key != 'Population' and (key not in ('Contact', 'URL') or a):  # separators
                    sys.stderr.write('%-25s %s: expected "%s" got "%s"\n' % (key, row['OCD'], a, b))

    writer = csv.writer(sys.stdout)
    writer.writerow(headers)
    for _, record in records.items():
        writer.writerow([record[header] for header in headers])
