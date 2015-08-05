from __future__ import unicode_literals

import re
from datetime import date

import boundaries


def namer(f):
    return re.sub(' Ward \d+\Z', '', boundaries.clean_attr('NAME')(f))

boundaries.register('Peterborough wards',
    domain='Peterborough, ON',
    last_updated=date(2014, 2, 28),
    name_func=namer,
    id_func=lambda f: re.sub(r'\D', '', f.get('NAME')),
    authority='City of Peterborough',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3515014'},
)
