import re
from datetime import date

import boundaries

boundaries.register('Nova Scotia electoral districts (2012)',
    singular='Nova Scotia electoral district',
    domain='Nova Scotia',
    last_updated=date(2016, 12, 8),
    name_func=boundaries.dashed_attr('ED_NAME'),
    id_func=lambda f: re.sub(r'\A0', '', f.get('ED_NO')),
    authority='Her Majesty the Queen in Right of Nova Scotia',
    source_url='https://electionsnovascotia.ca/Current-Maps',
    data_url='https://electionsnovascotia.ca/sites/default/files/NS_2012ED_Bnds.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/province:ns'},
)
