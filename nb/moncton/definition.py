from datetime import date

import boundaries

boundaries.register('Moncton wards',
    domain='Moncton, NB',
    last_updated=date(2012, 8, 21),
    name_func=lambda f: 'Ward %s' % f.get('WARDNUMB'),
    id_func=boundaries.attr('WARDNUMB'),
    authority='City of Moncton',
    notes='We use a shapefile received via email.',
    encoding='iso-8859-1',
)
