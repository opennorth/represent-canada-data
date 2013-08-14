from datetime import date
import re

import boundaries

boundaries.register('Windsor wards',
    domain='Windsor, ON',
    last_updated=date(2012, 2, 5),
    name_func=boundaries.clean_attr('WARD'),
    id_func=lambda f: re.sub(r'\D', '', f.get('WARD')),
    authority='City of Windsor',
    source_url='http://www.citywindsor.ca/opendata/Pages/Ward-Boundaries.aspx',
    licence_url='http://www.citywindsor.ca/opendata/Documents/OpenDataTermsofUse.pdf',
    data_url='http://www.citywindsor.ca/opendata/Documents/2010_Municipal_Ward_Boundaries.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3537039'},
)
