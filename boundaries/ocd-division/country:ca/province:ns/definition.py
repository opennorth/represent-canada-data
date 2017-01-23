from __future__ import unicode_literals

import re
from datetime import date

import boundaries

boundaries.register('Nova Scotia electoral districts',
    domain='Nova Scotia',
    last_updated=date(2016, 7, 28),
    name_func=boundaries.dashed_attr('DISTRICT'),
    id_func=lambda f: re.sub(r'^0+', '', f.get('DIST_NO')),
    authority='Her Majesty the Queen in Right of Nova Scotia',
    source_url='http://electionsnovascotia.ca/Current-Maps',
    data_url='http://electionsnovascotia.ca/sites/default/files/NS_2012ED_Bnds.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/province:ns'},
)
