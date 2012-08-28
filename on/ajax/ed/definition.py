from datetime import date

import boundaries

boundaries.register('Ajax wards',
    domain='Ajax, ON',
    last_updated=date(2012, 8, 17),
    name_func=lambda f: 'Ward %s' % f.get('WARD'),
    id_func=boundaries.attr('WARD'),
    authority='Town of Ajax',
    notes='We use a shapefile received via email.',
    encoding='iso-8859-1',
)
