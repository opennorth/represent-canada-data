from datetime import date

import boundaries

boundaries.register('Waterloo wards',
    domain='Waterloo, ON',
    last_updated=date(2012, 8, 22),
    name_func=boundaries.attr('WARD'),
    id_func=boundaries.attr('WARD_NO'),
    authority='City of Waterloo',
    notes='We use a shapefile received via email.',
    encoding='iso-8859-1',
)
