from datetime import date
import re

import boundaries

boundaries.register('Windsor wards',
    domain='Windsor, ON',
    last_updated=date(2010, 10, 27),
    name_func=boundaries.clean_attr('WARD'),
    id_func=lambda f: re.sub(r'\D', '', f.get('WARD')),
    authority='City of Windsor',
    source_url='http://www.citywindsor.ca/003713.asp',
    licence_url='http://www.citywindsor.ca/DataCatalogue/PDF/OpenDataTermsofUse.pdf',
    data_url='http://www.citywindsor.ca/DataCatalogue/SHP/2010_Municipal_Ward_Boundaries.zip',
    encoding='iso-8859-1',
)
