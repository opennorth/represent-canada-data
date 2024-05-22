from datetime import date

import boundaries

boundaries.register('Edmonton wards',
    domain='Edmonton, AB',
    last_updated=date(2024, 5, 21),
    name_func=boundaries.attr('name_1'),
    id_func=boundaries.attr('name_1'),
    authority='City of Edmonton',
    source_url='https://data.edmonton.ca/Administrative/City-of-Edmonton-Ward-Boundary-and-Council-Composi/b4er-5rp2',
    licence_url='https://data.edmonton.ca/stories/s/City-of-Edmonton-Open-Data-Terms-of-Use/msh8-if28/',
    data_url='https://data.edmonton.ca/api/geospatial/b4er-5rp2?method=export&format=Shapefile',
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca/csd:4811061'},
)
