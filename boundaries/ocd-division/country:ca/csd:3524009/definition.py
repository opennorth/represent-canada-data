import re
from datetime import date

import boundaries

boundaries.register('Milton wards',
    domain='Milton, ON',
    last_updated=date(2017, 2, 6),
    name_func=lambda f: 'Ward %s' % re.search(r'WARD (\d+)', f.get('Descriptio')).group(1),
    id_func=lambda f: re.search(r'WARD (\d+)', f.get('Descriptio')).group(1),
    authority='Town of Milton',
    source_url='https://www.milton.ca/en/townhall/opendata.asp',
    licence_url='https://www.milton.ca/en/townhall/resources/OpenDataAgreement.pdf',
    # 2018-10-22: https://www.milton.ca/en/resources/FutureWardBoundaries_180620128.zip
    data_url='https://www.milton.ca/en/resources/WardBoundaries_18062018.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3524009'},
)
