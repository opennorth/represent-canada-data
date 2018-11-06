import re
from datetime import date

import boundaries

boundaries.register('Fort Erie wards',
    domain='Fort Erie, ON',
    last_updated=date(2016, 1, 6),
    name_func=boundaries.attr('Name'),
    id_func=lambda f: re.sub(r'\D', '', f.get('Name')),
    source_url='https://niagaraopendata.ca/dataset/town-of-fort-erie-wards-2014',
    licence_url='https://niagaraopendata.ca/pages/open-government-licence-2-0-fort-erie',
    data_url='https://niagaraopendata.ca/dataset/dcaa1fd0-a3ea-4d51-a350-79a0918ea13e/resource/d441e46b-a1a4-4b7c-8efa-56155106a6fa/download/fort-erie-wards-2014.zip',
    authority='Town of Fort Erie',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3526003'},
)
