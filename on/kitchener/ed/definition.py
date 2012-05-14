from datetime import date

import boundaries

boundaries.register('Kitchener wards',
    domain='Kitchener, ON',
    last_updated=date(2012, 5, 14),
    name_func=boundaries.attr('WARD'),
    id_func=boundaries.attr('WARDID'),
    authority='City of Kitchener',
    notes='We use a shapefile received via email.',
    encoding='iso-8859-1',
)
