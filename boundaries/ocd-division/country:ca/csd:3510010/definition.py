import re
from datetime import date

import boundaries

boundaries.register('Kingston wards',
    domain='Kingston, ON',
    last_updated=date(2017, 2, 2),
    name_func=lambda f: f.get('NAME').replace('\x92', "'"),
    id_func=lambda f: re.sub(r'\D', '', f.get('URL')),
    source_url='https://opendatakingston.cityofkingston.ca/explore/dataset/electoral-districts/',
    licence_url='https://www.cityofkingston.ca/documents/10180/144997/CityofKingston_OpenDataLicense.pdf',
    data_url='https://opendatakingston.cityofkingston.ca/explore/dataset/electoral-districts/download/?format=shp&timezone=America/New_York',
    authority='City of Kingston',
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca/csd:3510010'},
)
