from datetime import date

import boundaries

boundaries.register('Brantford wards',
    domain='Brantford, ON',
    last_updated=date(2012, 8, 20),
    name_func=boundaries.attr('WARD_NAME'),
    id_func=boundaries.attr('WARD_ID'),
    authority='Town of Brantford',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3529006'},
)
