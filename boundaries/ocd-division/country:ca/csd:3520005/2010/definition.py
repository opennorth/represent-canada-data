import re
from datetime import date

import boundaries

boundaries.register('Toronto wards (2010)',
    singular='Toronto ward',
    domain='Toronto, ON',
    last_updated=date(2018, 1, 16),
    name_func=boundaries.attr('NAME'),
    id_func=lambda f: re.sub(r'\A0', '', f.get('SCODE_NAME')),
    authority='City of Toronto',
    source_url='https://www.toronto.ca/city-government/data-research-maps/open-data/open-data-catalogue/#29b6fadf-0bd6-2af9-4a8c-8c41da285ad7',
    licence_url='https://www.toronto.ca/city-government/data-research-maps/open-data/open-data-licence/',
    data_url='http://opendata.toronto.ca/gcc/wards_may2010_wgs84.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3520005'},
)
