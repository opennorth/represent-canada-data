import re
from datetime import date

import boundaries

boundaries.register('Windsor wards',
    domain='Windsor, ON',
    last_updated=date(2014, 7, 31),
    name_func=boundaries.clean_attr('WARD'),
    id_func=lambda f: re.sub(r'\D', '', f.get('WARD')),
    authority='City of Windsor',
    source_url='https://opendata.citywindsor.ca/opendata/details/222',
    licence_url='https://citywindsor.ca/opendata/Documents/OpenDataTermsofUse.pdf',
    data_url='https://opendata.citywindsor.ca/Uploads/2014_Municipal_Ward_Boundaries_UTM83.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3537039'},
)
