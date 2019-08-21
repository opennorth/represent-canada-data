from datetime import date

import boundaries

boundaries.register('Manitoba electoral districts 2018',
    singular='Manitoba electoral district',
    domain='Manitoba',
    last_updated=date(2018, 11, 30),
    name_func=boundaries.attr('ED'),
    authority='Her Majesty the Queen in Right of Manitoba',
    source_url='https://www.electionsmanitoba.ca/en/Resources/Maps',
    licence_url='http://www.boundariescommission.mb.ca/disclaimer/',
    data_url='https://www.electionsmanitoba.ca/downloads/2018_Final_ED_Manitoba_Public_Urban.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/province:mb'},
)
