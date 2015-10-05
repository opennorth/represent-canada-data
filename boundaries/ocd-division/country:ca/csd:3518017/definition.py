from __future__ import unicode_literals

import re
from datetime import date

import boundaries

boundaries.register('Clarington wards',
    domain='Clarington, ON',
    last_updated=date(2012, 11, 15),
    name_func=boundaries.attr('WARD'),
    id_func=lambda f: re.sub(r'\D', '', f.get('WARD')),
    authority='Municipality of Clarington',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3518017'},
)
