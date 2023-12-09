from datetime import date

import boundaries

boundaries.register('Mississauga wards',
    domain='Mississauga, ON',
    last_updated=date(2023, 9, 20),
    name_func=lambda f: 'Ward %s' % f.get('WARD'),
    id_func=boundaries.attr('WARD'),
    authority='City of Mississauga',
    source_url='https://data.mississauga.ca/datasets/mississauga::2022-ward-boundaries/about',
    licence_url='https://smartcity.mississauga.ca/wp-content/uploads/2021/04/CityofMississauga_TermsofUse.pdf',
    data_url='https://opendata.arcgis.com/api/v3/datasets/f1cad02b3a40422dac2ea99b59cc36a5_2/downloads/data?format=shp&spatialRefId=4326&where=1%3D1',
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca/csd:3521005'},
)
