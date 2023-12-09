from datetime import date

import boundaries

boundaries.register('New Brunswick electoral districts (2013)',
    singular='New Brunswick electoral district',
    domain='New Brunswick',
    last_updated=date(2015, 6, 23),  # historical
    name_func=boundaries.attr('PED_Name_E'),
    id_func=boundaries.attr('DIST_ID'),
    authority='Her Majesty the Queen in Right of New Brunswick',
    source_url='http://www.snb.ca/geonb1/e/DC/catalogue-E.asp',
    licence_url='http://geonb.snb.ca/documents/license/geonb-odl_en.pdf',
    data_url='http://geonb.snb.ca/downloads/prov_electoral_districts/geonb_2014_ped-cep_shp.zip',
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca/province:nb'},
)
