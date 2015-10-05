from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Ajax wards',
    domain='Ajax, ON',
    last_updated=date(2012, 8, 17),
    name_func=lambda f: 'Ward %s' % f.get('WARD'),
    id_func=boundaries.attr('WARD'),
    authority='Town of Ajax',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3518005'},
)
