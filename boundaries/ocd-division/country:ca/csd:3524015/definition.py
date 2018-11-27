import re
from datetime import date

import boundaries

boundaries.register('Halton Hills wards',
    domain='Halton Hills, ON',
    last_updated=date(2017, 1, 16),
    name_func=boundaries.attr('WARD'),
    id_func=lambda f: re.sub(r'\D+', '', f.get('WARD')),
    authority='Town of Halton Hills',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3524015'},
)
