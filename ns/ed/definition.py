from __future__ import unicode_literals

from datetime import date
import re

import boundaries

boundaries.register('Nova Scotia electoral districts',
    domain='Nova Scotia',
    last_updated=date(2013, 8, 6),
    name_func=boundaries.dashed_attr('DISTRICT'),
    id_func=lambda f: re.sub(r'^0+', f.get('DIST_NO')),
    authority='Her Majesty the Queen in Right of Nova Scotia',
    source_url='http://electionsnovascotia.ca/content/maps-0',
    data_url='http://electionsnovascotia.ca/sites/default/files/NS_EDBoundaries2012.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '12'},
)
