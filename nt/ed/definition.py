from datetime import date

import boundaries

boundaries.register('Northwest Territories electoral districts',
    domain='Northwest Territories',
    last_updated=date(2014, 4, 9),
    name_func=boundaries.attr('ED'),
    id_func=boundaries.attr('EDNWTF_ID'),
    authority='Government of the Northwest Territories',
    encoding='iso-8859-1',
    metadata={'geographic_code': '61'},
)
