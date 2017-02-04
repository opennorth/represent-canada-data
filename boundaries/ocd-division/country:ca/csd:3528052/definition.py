from datetime import date

import boundaries

boundaries.register('Norfolk County wards',
    domain='Norfolk County, ON',
    last_updated=date(2017, 1, 16),
    name_func=lambda f: 'Ward %s' % f.get('Ward'),
    id_func=boundaries.attr('Ward'),
    authority='City of Norfolk County',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3528052'},
)
