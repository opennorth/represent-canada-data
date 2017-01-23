# coding: utf-8
from __future__ import unicode_literals

from datetime import date

import boundaries

sets = {
    1301006: ['Saint John', 'Saint John'],
    1302004: ['Campobello Island', 'Campobello'],
    1303012: ['Oromocto', 'Oromocto'],
    1306020: ['Riverview', 'Riverview'],
    1307005: ['Beaubassin East', 'Beaubassin East\Beaubassin-Est'],
    1307013: ['Memramcook', 'Memramcook'],
    1307022: ['Moncton', 'Moncton'],
    1307045: ['Dieppe', 'Dieppe'],
    1309027: ['Upper Miramichi', 'Upper Miramichi'],
    # Fredericton has ward names in its data catalog.
    # 1310032: ['Fredericton', 'Fredericton'],
    1311027: ['Florenceville-Bristol', 'Florenceville-Bristol'],
    1313002: ['Saint-André', 'Saint-André'],
    1313027: ['Edmundston', 'Edmunston'],
    1314019: ['Kedgwick', 'Kedgwick'],
    1314025: ['Belledune', 'Belledune'],
    1315027: ['Bas-Caraquet', 'Bas-Caraquet'],
    1315028: ['Caraquet', 'Caraquet'],
}

for geographic_code, (name, machine_name) in sets.items():
    boundaries.register('%s wards' % name,
        file='%s.shp' % name,
        domain='%s, NB' % name,
        last_updated=date(2014, 3, 24),
        name_func=lambda f: 'Ward %s' % f.get('WARD_ID'),
        id_func=boundaries.attr('WARD_ID'),
        authority='Her Majesty the Queen in Right of New Brunswick',
        source_url='http://geonb.snb.ca/ArcGIS/rest/services/GeoNB_ENB_MunicipalWards/MapServer/0',
        licence_url='http://geonb.snb.ca/downloads/documents/geonb_license_e.pdf',
        encoding='iso-8859-1',
        extra={'division_id': 'ocd-division/country:ca/csd:%d' % geographic_code},
        ogr2ogr='''-where "MUN_NAME='%s'"''' % machine_name,
        base_file='OGRGeoJSON.shp',
    )

boundaries.register('Beresford wards',
    file='Beresford.shp',
    domain='Beresford, NB',
    last_updated=date(2014, 3, 24),
    name_func=lambda f: 'Ward B' if f.get('OBJECTID') == 52 else 'Ward A',
    authority='Her Majesty the Queen in Right of New Brunswick',
    source_url='http://geonb.snb.ca/ArcGIS/rest/services/GeoNB_ENB_MunicipalWards/MapServer/0',
    licence_url='http://geonb.snb.ca/downloads/documents/geonb_license_e.pdf',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:1315015'},
    ogr2ogr='''-where "MUN_NAME='Beresford'"''',
    base_file='OGRGeoJSON.shp',
)

boundaries.register('Grand Falls wards',
    file='Grand Falls.shp',
    domain='Grand Falls, NB',
    last_updated=date(2014, 3, 24),
    name_func=lambda f: 'South Ward' if f.get('OBJECTID') == 35 else 'North Ward',
    authority='Her Majesty the Queen in Right of New Brunswick',
    source_url='http://geonb.snb.ca/ArcGIS/rest/services/GeoNB_ENB_MunicipalWards/MapServer/0',
    licence_url='http://geonb.snb.ca/downloads/documents/geonb_license_e.pdf',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:1312019'},
    ogr2ogr='''-where "MUN_NAME='Grand Falls\Grand-Sault'"''',
    base_file='OGRGeoJSON.shp',
)
