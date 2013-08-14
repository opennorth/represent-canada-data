from datetime import date

import boundaries

boundaries.register('Halifax districts',
    domain='Halifax, NS',
    last_updated=date(2012, 11, 6),
    name_func=boundaries.attr('DISTNAME'),
    id_func=boundaries.attr('DIST_ID'),
    authority='Halifax Regional Municipality',
    encoding='iso-8859-1',
    metadata={'geographic_code': '1209034'},
)
