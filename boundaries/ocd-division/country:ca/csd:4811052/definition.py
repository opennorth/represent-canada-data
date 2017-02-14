from datetime import date

import boundaries

boundaries.register('Strathcona County wards',
    domain='Strathcona County, AB',
    last_updated=date(2017, 2, 6),
    name_func=lambda f: 'Ward %d' % f.get('ward'),
    id_func=lambda f: '%d' % f.get('ward'),
    authority='Strathcona County',
    # Effective 2016-10-16 https://data.strathcona.ca/Boundaries/2017-Ward-Boundaries/g2xw-827r
    source_url='https://data.strathcona.ca/Boundaries/2007-Ward-Boundaries/r8k6-yyk6',
    licence_url='https://data.strathcona.ca/licence',
    # Effective 2017-10-16 https://data.strathcona.ca/api/geospatial/g2xw-827r?method=export&format=Shapefile
    data_url='https://data.strathcona.ca/api/geospatial/r8k6-yyk6?method=export&format=Shapefile',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:4811052'},
)
