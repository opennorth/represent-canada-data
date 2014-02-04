from datetime import date
import re

import boundaries

boundaries.register('Fredericton wards',
    domain='Fredericton, NB',
    last_updated=date(2013, 11, 26),
    name_func=lambda f: re.sub(' / ', '/', f.get('Ward')),
    id_func=boundaries.attr('Ward_Num'),
    authority='City of Fredericton',
    source_url='http://www.fredericton.ca/en/citygovernment/DataMain.asp',
    licence_url='http://www.fredericton.ca/en/citygovernment/TermsOfUse.asp',
    data_url='http://files.fredericton.ca/data/GISData/wards.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '1310032'},
)
