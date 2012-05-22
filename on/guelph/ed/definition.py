from datetime import date

import boundaries

boundaries.register('Guelph wards',
    domain='Guelph, ON',
    last_updated=date(2012, 5, 15),
    name_func=boundaries.attr('WARD'),
    id_func=boundaries.attr('WARD'),
    authority='City of Guelph',
    notes='We use a shapefile received via email.',
    encoding='iso-8859-1',
)
