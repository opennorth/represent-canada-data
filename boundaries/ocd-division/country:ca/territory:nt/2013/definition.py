from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Northwest Territories electoral districts',  # (2013)
    singular='Northwest Territories electoral district',
    domain='Northwest Territories',
    last_updated=date(2014, 4, 9),
    name_func=boundaries.attr('ED'),
    id_func=lambda f: int(f.get('EDNWTF_ID')),
    authority='Her Majesty the Queen in Right of Northwest Territories',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/territory:nt'},
)
