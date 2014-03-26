from datetime import date

import boundaries

boundaries.register('East Hants districts',
    domain='East Hants, NS',
    last_updated=date(2014, 3, 25),
    name_func=boundaries.attr('District'),
    id_func=boundaries.attr('Polling_No'),
    authority='Municipality of East Hants',
    encoding='iso-8859-1',
    metadata={'geographic_code': '1208008'},
)
