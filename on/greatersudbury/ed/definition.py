from datetime import date

import boundaries

boundaries.register('Greater Sudbury wards',
    domain='Greater Sudbury, ON',
    last_updated=date(2012, 2, 21),
    name_func=lambda f: 'Ward %s' % f.get('Ward'),
    id_func=boundaries.attr('Ward'),
    authority='City of Greater Sudbury',
    notes='We use a shapefile received via email.',
    encoding='iso-8859-1',
    geographic_code='3553005',
)
