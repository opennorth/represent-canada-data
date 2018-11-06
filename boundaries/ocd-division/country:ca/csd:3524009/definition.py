from datetime import date

import boundaries

boundaries.register('Milton wards',
    domain='Milton, ON',
    last_updated=date(2018, 7, 16),
    name_func=boundaries.clean_attr('WARD'),
    id_func=boundaries.attr('WARD_NUM'),
    authority='Town of Milton',
    source_url='https://www.milton.ca/en/townhall/opendata.asp',
    licence_url='https://www.milton.ca/en/townhall/resources/OpenDataAgreement.pdf',
    data_url='http://www.milton.ca/en/resources/FutureWardBoundaries_180620128.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3524009'},
)
