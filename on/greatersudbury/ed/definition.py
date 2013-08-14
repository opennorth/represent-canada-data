from datetime import date

import boundaries

boundaries.register('Greater Sudbury wards',
    domain='Greater Sudbury, ON',
    last_updated=date(2012, 2, 21),
    name_func=lambda f: 'Ward %s' % f.get('Ward'),
    id_func=boundaries.attr('Ward'),
    authority='City of Greater Sudbury',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3553005'},
)
