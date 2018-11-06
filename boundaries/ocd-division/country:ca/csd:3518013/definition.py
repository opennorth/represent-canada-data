from datetime import date

import boundaries

boundaries.register('Oshawa wards',
    domain='Oshawa, ON',
    last_updated=date(2018, 10, 19),
    name_func=lambda f: 'Ward %s' % f.get('WARDNUMBER'),
    id_func=boundaries.attr('WARDNUMBER'),
    authority='City of Oshawa',
    source_url='https://city-oshawa.opendata.arcgis.com/datasets/oshawa-2018-ward-boundaries',
    licence_url='https://map.oshawa.ca/OpenData/Open%20Government%20Licence%20version%202.0%20-%20Oshawa.pdf',
    data_url='https://opendata.arcgis.com/datasets/a9257f99b2d941a3bff928f4a19d6f9d_11.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3518013'},
)
