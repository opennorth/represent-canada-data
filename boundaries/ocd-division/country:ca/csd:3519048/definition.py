from datetime import date

import boundaries

boundaries.register('Newmarket wards',
    domain='Newmarket, ON',
    last_updated=date(2023, 10, 4),
    name_func=lambda f: 'Ward %s' % f.get('WARD'),
    id_func=boundaries.attr('WARD'),
    authority='Town of Newmarket',
    source_url='https://navigate-newmarket.hub.arcgis.com/datasets/f0537eeb8e7e4f8f8f9922083e34d0e0_0/about',
    data_url='https://opendata.arcgis.com/api/v3/datasets/f0537eeb8e7e4f8f8f9922083e34d0e0_0/downloads/data?format=shp&spatialRefId=4326&where=1%3D1',
    licence_url='https://www.newmarket.ca/TownGovernment/Documents/Newmarket_OpenData_Licence.pdf',
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca/csd:3519048'},
)
