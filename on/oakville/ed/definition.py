from datetime import date

import boundaries

boundaries.register('Oakville wards',
    domain='Oakville, ON',
    last_updated=date(2012, 5, 14),
    name_func=boundaries.attr('FULL_NAME'),
    id_func=boundaries.attr('WARD'),
    authority='Town of Oakville',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3524001'},
)
