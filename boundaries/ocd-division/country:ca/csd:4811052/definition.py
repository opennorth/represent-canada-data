from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Strathcona County wards',
    domain='Strathcona County, AB',
    last_updated=date(2016, 8, 6),
    name_func=lambda f: 'Ward %d' % f.get('ward'),
    id_func=lambda f: '%d' % f.get('ward'),
    authority='Strathcona County',
    source_url='https://data.strathcona.ca/Land-Base/Ward-Boundaries/r8k6-yyk6',
    licence_url='https://data.strathcona.ca/licence',
    data_url='https://data.strathcona.ca/api/geospatial/r8k6-yyk6?method=export&format=Shapefile',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:4811052'},
)
