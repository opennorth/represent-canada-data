from __future__ import unicode_literals

import re
from datetime import date

import boundaries

boundaries.register('Edmonton wards',
    domain='Edmonton, AB',
    last_updated=date(2016, 1, 4),
    name_func=lambda f: 'Ward %s' % re.sub(r'\D+0?', '', f.get('NAME')),
    id_func=lambda f: re.sub(r'\D+0?', '', f.get('NAME')),
    authority='City of Edmonton',
    source_url='https://data.edmonton.ca/Administrative/City-of-Edmonton-Ward-Boundaries/yhng-294h?',
    licence_url='http://www.edmonton.ca/city_government/documents/Web-version2.1-OpenDataAgreement.pdf',
    data_url='https://data.edmonton.ca/api/geospatial/yhng-294h?method=export&format=Shapefile',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:4811061'},
)
