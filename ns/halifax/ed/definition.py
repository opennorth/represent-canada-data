from datetime import date

import boundaries

boundaries.register('Halifax districts',
    domain='Halifax, NS',
    last_updated=date(2012, 5, 15),
    name_func=boundaries.attr('DISTNAME'),
    id_func=boundaries.attr('DIST_ID'),
    authority='Halifax Regional Municipality',
    notes='We use a shapefile received via email.',
    encoding='iso-8859-1',
)
