from datetime import date

import boundaries

boundaries.register('Kingston districts',
    domain='Kingston, ON',
    last_updated=date(2012, 10, 25),
    name_func=boundaries.attr('ELECTORAL_'),
    id_func=boundaries.attr('ELECTORAL1'),
    authority='City of Kingston',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3510010'},
)
