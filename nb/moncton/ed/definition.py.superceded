from datetime import date

import boundaries

boundaries.register('Moncton wards',
    domain='Moncton, NB',
    last_updated=date(2012, 8, 21),
    name_func=lambda f: 'Ward %s' % f.get('WARDNUMB'),
    id_func=boundaries.attr('WARDNUMB'),
    authority='City of Moncton',
    encoding='iso-8859-1',
    metadata={'geographic_code': '1307022'},
)
