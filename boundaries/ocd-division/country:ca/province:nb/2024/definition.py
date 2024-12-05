from datetime import date

import boundaries

boundaries.register('New Brunswick electoral districts (2024)',
    singular='New Brunswick electoral district',
    domain='New Brunswick',
    last_updated=date(2024, 8, 22),
    name_func=lambda f: f.get('PED_Names_').split(' / ')[0],
    authority='Her Majesty the Queen in Right of New Brunswick',
    source_url='http://www.snb.ca/geonb1/e/DC/PED.asp',
    licence_url='http://www.snb.ca/e/2000/data-E.html',
    data_url='http://geonb.snb.ca/downloads/provincial_elections/geonb_2024_ped-cep_shp.zip',
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca/province:nb'},
)
