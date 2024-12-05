from datetime import date

import boundaries

boundaries.register('New Brunswick electoral districts (2020)',
    singular='New Brunswick electoral district',
    domain='New Brunswick',
    last_updated=date(2021, 7, 30),
    name_func=boundaries.attr('PED_Name_E'),
    id_func=boundaries.attr('DIST_ID'),
    authority='Her Majesty the Queen in Right of New Brunswick',
    source_url='http://www.snb.ca/geonb1/e/DC/PED-2020.asp',
    licence_url='http://www.snb.ca/e/2000/data-E.html',
    data_url='http://geonb.snb.ca/downloads/prov_electoral_districts/geonb_2020_ped-cep_shp.zip',
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca/province:nb'},
)
