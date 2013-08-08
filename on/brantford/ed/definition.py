from datetime import date

import boundaries

boundaries.register('Brantford wards',
    domain='Brantford, ON',
    last_updated=date(2012, 8, 20),
    name_func=boundaries.attr('WARD_NAME'),
    id_func=boundaries.attr('WARD_ID'),
    authority='Town of Brantford',
    notes='We use a shapefile received via email.',
    encoding='iso-8859-1',
    geographic_code='3529006',
)
