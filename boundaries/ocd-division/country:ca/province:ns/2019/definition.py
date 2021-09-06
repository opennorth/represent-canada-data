import re
from datetime import date

import boundaries

boundaries.register('Nova Scotia electoral districts',  # (2019)
    singular='Nova Scotia electoral district',
    domain='Nova Scotia',
    last_updated=date(2020, 3, 1),
    name_func=boundaries.dashed_attr('ED_NAME'),
    id_func=lambda f: re.sub(r'\A0', '', f.get('ED_NO')),
    authority='Her Majesty the Queen in Right of Nova Scotia',
    source_url='https://www.electionsnovascotia.ca/Maps%20for%20the41st%20Provincial%20General%20Election',
    data_url='https://www.electionsnovascotia.ca/sites/default/files/NS_2019ED_Bnds.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/province:ns'},
)
