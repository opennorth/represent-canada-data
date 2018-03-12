import re
from datetime import date

import boundaries

boundaries.register('Kingston wards',
    domain='Kingston, ON',
    last_updated=date(2017, 2, 2),
    name_func=lambda f: f.get('NAME').replace('\x92', "'"),
    id_func=lambda f: re.sub(r'\D', '', f.get('URL')),
    source_url='https://www.cityofkingston.ca/explore/data-catalogue',
    licence_url='https://www.cityofkingston.ca/documents/10180/144997/GIS_OpenDataLicense.pdf/72f5a9ac-afbc-4fe3-959d-9111c9393bfa',
    data_url='https://apps.cityofkingston.ca/data/gis/Electoral_District_SHP.zip',
    authority='City of Kingston',
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca/csd:3510010'},
)
