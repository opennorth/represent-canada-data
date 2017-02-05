from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Barrie wards',
    domain='Barrie, ON',
    last_updated=date(2017, 1, 30),
    name_func=lambda f: 'Ward %s' % f.get('WARD_NO'),
    id_func=boundaries.attr('WARD_NO'),
    authority='City of Barrie',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3543042'},
)
