# coding: utf-8
from datetime import date

import boundaries

boundaries.register('Grand Falls wards',
    domain='Grand Falls, NB',
    last_updated=date(2018, 11, 5),
    name_func=lambda f: 'South Ward' if f.get('OBJECTID') == 35 else 'North Ward',
    authority='Her Majesty the Queen in Right of New Brunswick',
    source_url='http://geonb.snb.ca/arcgis/rest/services/GeoNB_ENB_MunicipalElections/MapServer',
    licence_url='http://geonb.snb.ca/downloads/documents/geonb_license_e.pdf',
    data_url='http://geonb.snb.ca/arcgis/rest/services/GeoNB_ENB_MunicipalElections/MapServer/1',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:1312019'},
    is_valid_func=lambda f: f.get('Mun_Name') == 'Grand Falls\\Grand-Sault',
)

sets = {
    1314013: ['Atholville', 'Atholville'],
    1315027: ['Bas-Caraquet', 'Bas-Caraquet'],
    1307005: ['Beaubassin East', 'Beaubassin East\\Beaubassin-Est'],
    1314025: ['Belledune', 'Belledune'],
    1302004: ['Campobello Island', 'Campobello'],
    1315028: ['Caraquet', 'Caraquet'],
    1308002: ['Cocagne', 'Cocagne'],
    1307045: ['Dieppe', 'Dieppe'],
    1313027: ['Edmundston', 'Edmunston'],
    1311027: ['Florenceville-Bristol', 'Florenceville-Bristol'],
    # Fredericton has ward names in its data catalog.
    # Grand Falls is above.
    1310017: ['Hanwell', 'Hanwell'],
    # Haut-Madawaska incorporated after Census 2016: https://www2.gnb.ca/content/gnb/en/news/news_release.2017.03.0385.html
    1314020: ['Kedgwick', 'Kedgwick'],
    1307022: ['Moncton', 'Moncton'],
    1303012: ['Oromocto', 'Oromocto'],
    1306020: ['Riverview', 'Riverview'],
    1301006: ['Saint John', 'Saint John'],
    1313002: ['Saint-André', 'Saint-André'],
    1315002: ['Tracadie', 'Tracadie'],
    1309027: ['Upper Miramichi', 'Upper Miramichi'],
    # Beresford was present in 2014-03-24, not in 2017-02-06.
    # Memramcook was present in 2014-03-24, not in 2017-02-04.
}

for geographic_code, (name, machine_name) in sets.items():
    boundaries.register('%s wards' % name,
        domain='%s, NB' % name,
        last_updated=date(2018, 11, 5),
        name_func=lambda f: 'Ward %s' % f.get('Ward_ID_2'),
        id_func=boundaries.attr('Ward_ID_2'),
        authority='Her Majesty the Queen in Right of New Brunswick',
        source_url='http://geonb.snb.ca/arcgis/rest/services/GeoNB_ENB_MunicipalElections/MapServer',
        licence_url='http://geonb.snb.ca/downloads/documents/geonb_license_e.pdf',
        data_url='http://geonb.snb.ca/arcgis/rest/services/GeoNB_ENB_MunicipalElections/MapServer/1',
        encoding='iso-8859-1',
        extra={'division_id': 'ocd-division/country:ca/csd:%d' % geographic_code},
        is_valid_func=lambda f, machine_name=machine_name: f.get('Mun_Name') == machine_name,
        notes='Compare the subdivisions in boundaries/ca_nb_wards/definition.py to:\nogrinfo -al -geom=NO boundaries/ca_nb_wards | grep " Mun_Name" | sort | uniq | cut -d= -f 2',
    )
