from datetime import date

import boundaries

boundaries.register('New Brunswick electoral districts (2018)',
    singular='New Brunswick electoral district',
    domain='New Brunswick',
    last_updated=date(2022, 5, 10),
    name_func=boundaries.attr('PED_Name_E'),
    id_func=boundaries.attr('DIST_ID'),
    authority='Her Majesty the Queen in Right of New Brunswick',
    source_url='https://www.electionsnb.ca/content/enb/en/maps/PED.html',
    data_url='https://www.electionsnb.ca/content/dam/enb/pdf/2016PEDMaps-CEPCartes/Provincial_Electoral_Districts_2018.zip',
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca/province:nb'},
)
