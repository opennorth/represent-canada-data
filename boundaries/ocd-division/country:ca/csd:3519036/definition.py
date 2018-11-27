from datetime import date

import boundaries

boundaries.register('Markham wards',
    domain='Markham, ON',
    last_updated=date(2018, 11, 27),
    name_func=lambda f: 'Ward %s' % int(f.get('WARD')),
    id_func=lambda f: int(f.get('WARD')),
    authority='City of Markham',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3519036'},
)
