import re
from datetime import date

import boundaries

boundaries.register('Pickering wards',
    domain='Pickering, ON',
    last_updated=date(2018, 5, 11),
    name_func=boundaries.attr('TEXT_'),
    id_func=lambda f: re.sub(r'\D', '', f.get('TEXT_')),
    authority='City of Pickering',
    source_url='http://opendata.pickering.ca/datasets/pickering-ward-boundaries',
    licence_url='https://www.pickering.ca/en/city-hall/resources/OpenDataLicencePickeringV1.pdf',
    data_url='https://opendata.arcgis.com/datasets/9dde9f0bc8bb42ceb4988acc2ed23523_5.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3518001'},
)
