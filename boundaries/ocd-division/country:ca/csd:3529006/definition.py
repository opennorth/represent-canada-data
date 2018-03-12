from datetime import date

import boundaries

boundaries.register('Brantford wards',
    domain='Brantford, ON',
    last_updated=date(2017, 5, 9),
    name_func=boundaries.attr('WARD_NAME'),
    id_func=boundaries.attr('WARD'),
    authority='City of Brantford',
    source_url='http://data-brantford.opendata.arcgis.com/datasets/city-of-brantford-ward-boundaries',
    licence_url='http://data-brantford.opendata.arcgis.com/pages/licence',
    data_url='https://opendata.arcgis.com/datasets/6bc1504473ba4235b58494af5bf05227_0.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3529006'},
)
