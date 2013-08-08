from datetime import date

import boundaries

boundaries.register('Oakville wards',
    domain='Oakville, ON',
    last_updated=date(2012, 5, 14),
    name_func=boundaries.attr('FULL_NAME'),
    id_func=boundaries.attr('WARD'),
    authority='Town of Oakville',
    notes='We use a shapefile received via email.',
    encoding='iso-8859-1',
    geographic_code='3524001',
)
