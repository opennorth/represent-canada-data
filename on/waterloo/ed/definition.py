from datetime import date

import boundaries

boundaries.register('Waterloo wards',
    domain='Waterloo, ON',
    last_updated=date(2012, 8, 22),
    name_func=boundaries.attr('WARD'),
    id_func=boundaries.attr('WARD_NO'),
    authority='City of Waterloo',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3530016'},
)
