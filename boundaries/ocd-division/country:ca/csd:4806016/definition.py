from datetime import date

import boundaries

boundaries.register('Calgary wards',
    domain='Calgary, AB',
    last_updated=date(2017, 2, 6),
    name_func=boundaries.clean_attr('LABEL'),
    id_func=lambda f: int(f.get('WARD_NUM')),
    authority='City of Calgary',
    source_url='https://data.calgary.ca/Base-Maps/Ward-Boundaries/r9vx-mhnf',
    licence_url='https://data.calgary.ca/stories/s/u45n-7awa',
    data_url='https://data.calgary.ca/api/geospatial/r9vx-mhnf?method=export&format=Shapefile',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:4806016'},
)
