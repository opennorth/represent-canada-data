# coding: utf-8
from __future__ import unicode_literals

from datetime import date

import boundaries

# The shapefile contains features with MUN_NAME equal to Cocagne, Hanwell and
# Tracadie, but these are Census places, not Census subdivisions.
sets = {
    1301006: ['Saint John', 'Saint John'],
    1302004: ['Campobello Island', 'Campobello'],
    1303012: ['Oromocto', 'Oromocto'],
    1306020: ['Riverview', 'Riverview'],
    1307005: ['Beaubassin East', 'Beaubassin East\Beaubassin-Est'],
    # Memramcook was present in 2014-03-24, not in 2017-02-04.
    # 1307013: ['Memramcook', 'Memramcook'],
    1307022: ['Moncton', 'Moncton'],
    1307045: ['Dieppe', 'Dieppe'],
    1309027: ['Upper Miramichi', 'Upper Miramichi'],
    # Fredericton has ward names in its data catalog.
    # 1310032: ['Fredericton', 'Fredericton'],
    1311027: ['Florenceville-Bristol', 'Florenceville-Bristol'],
    1313002: ['Saint-André', 'Saint-André'],
    1313027: ['Edmundston', 'Edmunston'],
    1314013: ['Atholville', 'Atholville'],
    1314019: ['Kedgwick', 'Kedgwick'],
    1314025: ['Belledune', 'Belledune'],
    1315027: ['Bas-Caraquet', 'Bas-Caraquet'],
    1315028: ['Caraquet', 'Caraquet'],
}

for geographic_code, (name, machine_name) in sets.items():
    boundaries.register('%s wards' % name,
        domain='%s, NB' % name,
        last_updated=date(2017, 2, 4),
        name_func=lambda f: 'Ward %s' % f.get('WARD_ID'),
        id_func=boundaries.attr('WARD_ID'),
        authority='Her Majesty the Queen in Right of New Brunswick',
        source_url='http://geonb.snb.ca/ArcGIS/rest/services/GeoNB_ENB_MunicipalWards/MapServer/0',
        licence_url='http://geonb.snb.ca/downloads/documents/geonb_license_e.pdf',
        data_url='http://geonb.snb.ca/ArcGIS/rest/services/GeoNB_ENB_MunicipalWards/MapServer/0',
        encoding='iso-8859-1',
        extra={'division_id': 'ocd-division/country:ca/csd:%d' % geographic_code},
        is_valid_func=lambda f, machine_name=machine_name: f.get('MUN_NAME') == machine_name,
        notes='Compare the subdivisions in boundaries/ca_nb_wards/definition.py to:\nogrinfo -al -geom=NO boundaries/ca_nb_wards | grep " MUN_NAME" | sort | uniq | cut -d= -f 2',
    )

# Beresford was present in 2014-03-24, not in 2017-02-06.
# boundaries.register('Beresford wards',
#     domain='Beresford, NB',
#     last_updated=date(2014, 3, 24),
#     name_func=lambda f: 'Ward B' if f.get('OBJECTID') == 52 else 'Ward A',
#     id_func=lambda f: 'B' if f.get('OBJECTID') == 52 else 'A',
#     authority='Her Majesty the Queen in Right of New Brunswick',
#     source_url='http://geonb.snb.ca/ArcGIS/rest/services/GeoNB_ENB_MunicipalWards/MapServer/0',
#     licence_url='http://geonb.snb.ca/downloads/documents/geonb_license_e.pdf',
#     data_url='http://geonb.snb.ca/ArcGIS/rest/services/GeoNB_ENB_MunicipalWards/MapServer/0',
#     encoding='iso-8859-1',
#     extra={'division_id': 'ocd-division/country:ca/csd:1315015'},
#     is_valid_func=lambda f: f.get('MUN_NAME') == 'Beresford',
# )

boundaries.register('Grand Falls wards',
    domain='Grand Falls, NB',
    last_updated=date(2014, 3, 24),
    name_func=lambda f: 'South Ward' if f.get('OBJECTID') == 35 else 'North Ward',
    authority='Her Majesty the Queen in Right of New Brunswick',
    source_url='http://geonb.snb.ca/ArcGIS/rest/services/GeoNB_ENB_MunicipalWards/MapServer/0',
    licence_url='http://geonb.snb.ca/downloads/documents/geonb_license_e.pdf',
    data_url='http://geonb.snb.ca/ArcGIS/rest/services/GeoNB_ENB_MunicipalWards/MapServer/0',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:1312019'},
    is_valid_func=lambda f: f.get('MUN_NAME') == 'Grand Falls\Grand-Sault',
)
