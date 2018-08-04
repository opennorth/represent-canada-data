from datetime import date

import boundaries

boundaries.register('Edmonton wards',
    domain='Edmonton, AB',
    last_updated=date(2018, 8, 4),
    name_func=lambda f: 'Ward %s' % f.get('name'),
    id_func=boundaries.attr('name'),
    authority='City of Edmonton',
    source_url='https://data.edmonton.ca/Administrative/City-of-Edmonton-Ward-Boundaries-effective-at-12-0/xre8-g6yf',
    licence_url='https://www.edmonton.ca/city_government/documents/Web-version2.1-OpenDataAgreement.pdf',
    data_url='https://data.edmonton.ca/api/geospatial/xre8-g6yf?method=export&format=Shapefile',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:4811061'},
)
