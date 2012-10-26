from datetime import date

import boundaries

boundaries.register('Thunder Bay wards',
    domain='Thunder Bay, ON',
    last_updated=date(2012, 10, 25),
    name_func=boundaries.attr('WARD_NAME'),
    id_func=boundaries.attr('WARD_NO'),
    authority='City of Thunder Bay',
    notes='We use a shapefile received via email.',
    encoding='iso-8859-1',
)
