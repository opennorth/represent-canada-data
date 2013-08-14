from datetime import date

import boundaries

boundaries.register('Nova Scotia electoral districts',
    domain='Nova Scotia',
    last_updated=date(2013, 8, 6),
    name_func=boundaries.dashed_attr('DISTRICT'),
    id_func=boundaries.attr('DIST_NO'),
    authority='Elections Nova Scotia',
    source_url='http://electionsnovascotia.ca/content/maps-0',
    data_url='http://electionsnovascotia.ca/sites/default/files/NS_EDBoundaries2012.zip',
    encoding='iso-8859-1',
    geographic_code='12',
)
