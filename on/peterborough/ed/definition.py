from datetime import date

import boundaries

boundaries.register('Peterborough wards',
    domain='Peterborough, ON',
    last_updated=date(2012, 9, 05),
    name_func=boundaries.attr('NAME'),
    id_func=boundaries.attr('WARD_ID'),
    authority='Town of Peterborough',
    notes='We use a shapefile received via email.',
    encoding='iso-8859-1',
)
