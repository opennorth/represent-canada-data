from datetime import date
import re

import boundaries

boundaries.register('Windsor wards',
    domain='Windsor, ON',
    last_updated=date(2014, 7, 31),
    name_func=boundaries.clean_attr('WARD'),
    id_func=lambda f: re.sub(r'\D', '', f.get('WARD')),
    authority='City of Windsor',
    source_url='http://www.citywindsor.ca/opendata/pages/open-data-catalogue.aspx',
    licence_url='http://www.citywindsor.ca/opendata/Documents/OpenDataTermsofUse.pdf',
    data_url='http://www.citywindsor.ca/opendata/Lists/OpenData/Attachments/9/2014_Municipal_Ward_Boundaries_UTM83.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3537039'},
)
