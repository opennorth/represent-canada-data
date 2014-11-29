from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Strathcona County wards',
    domain='Strathcona County, AB',
    last_updated=date(2014, 2, 28),
    name_func=lambda f: 'Ward %d' % f.get('Ward'),
    id_func=lambda f: '%d' % f.get('Ward'),
    authority='Strathcona County',
    source_url='https://data.strathcona.ca/Administration/Ward-Boundaries/r8k6-yyk6',
    licence_url='https://data.strathcona.ca/licence',
    data_url='https://data.strathcona.ca/api/geospatial/r8k6-yyk6?method=export&format=Shapefile',
    encoding='iso-8859-1',
    metadata={'geographic_code': '4811052'},
)
