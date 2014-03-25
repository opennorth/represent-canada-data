# coding: utf-8
from datetime import date

import boundaries

sets = {
    '1301006': [u'Saint John', u'Saint John'],
    '1302004': [u'Campobello Island', u'Campobello'],
    '1303012': [u'Oromocto', u'Oromocto'],
    '1306020': [u'Riverview', u'Riverview'],
    '1307005': [u'Beaubassin East', u'Beaubassin East\Beaubassin-Est'],
    '1307013': [u'Memramcook', u'Memramcook'],
    '1307022': [u'Moncton', u'Moncton'],
    '1307045': [u'Dieppe', u'Dieppe'],
    '1309027': [u'Upper Miramichi', u'Upper Miramichi'],
    # Fredericton has ward names in its data catalog.
    # '1310032': [u'Fredericton', u'Fredericton'],
    '1311027': [u'Florenceville-Bristol', u'Florenceville-Bristol'],
    '1313002': [u'Saint-André', u'Saint-André'],
    '1313027': [u'Edmundston', u'Edmunston'],
    '1314019': [u'Kedgwick', u'Kedgwick'],
    '1314025': [u'Belledune', u'Belledune'],
    '1315027': [u'Bas-Caraquet', u'Bas-Caraquet'],
    '1315028': [u'Caraquet', u'Caraquet'],
}

for geographic_code, (name, machine_name) in sets.items():
    boundaries.register(u'%s wards' % name,
        file='%s.shp' % name,
        domain=u'%s, NB' % name,
        last_updated=date(2014, 3, 24),
        name_func=lambda f: 'Ward %s' % f.get('WARD_ID'),
        id_func=boundaries.attr('WARD_ID'),
        authority='Her Majesty the Queen in Right of New Brunswick',
        source_url='http://geonb.snb.ca/ArcGIS/rest/services/ElectionsNB/GeoNB_ENB_MunicipalWards/MapServer/0',
        licence_url='http://geonb.snb.ca/downloads/documents/geonb_license_e.pdf',
        encoding='iso-8859-1',
        metadata={'geographic_code': geographic_code},
        ogr2ogr='''-where "MUN_NAME='%s'"''' % machine_name,
        base_file='OGRGeoJSON.shp',
    )

boundaries.register(u'Beresford wards',
    file='Beresford.shp',
    domain=u'Beresford, NB',
    last_updated=date(2014, 3, 24),
    name_func=lambda f: 'Ward B' if f.get('OBJECTID') == 52 else 'Ward A',
    authority='Her Majesty the Queen in Right of New Brunswick',
    source_url='http://geonb.snb.ca/ArcGIS/rest/services/ElectionsNB/GeoNB_ENB_MunicipalWards/MapServer/0',
    licence_url='http://geonb.snb.ca/downloads/documents/geonb_license_e.pdf',
    encoding='iso-8859-1',
    metadata={'geographic_code': '1315015'},
    ogr2ogr='''-where "MUN_NAME='Beresford'"''',
    base_file='OGRGeoJSON.shp',
)

boundaries.register(u'Grand Falls wards',
    file='Grand Falls.shp',
    domain=u'Grand Falls, NB',
    last_updated=date(2014, 3, 24),
    name_func=lambda f: 'South Ward' if f.get('OBJECTID') == 35 else 'North Ward',
    authority='Her Majesty the Queen in Right of New Brunswick',
    source_url='http://geonb.snb.ca/ArcGIS/rest/services/ElectionsNB/GeoNB_ENB_MunicipalWards/MapServer/0',
    licence_url='http://geonb.snb.ca/downloads/documents/geonb_license_e.pdf',
    encoding='iso-8859-1',
    metadata={'geographic_code': '1312019'},
    ogr2ogr='''-where "MUN_NAME='Grand Falls\Grand-Sault'"''',
    base_file='OGRGeoJSON.shp',
)
