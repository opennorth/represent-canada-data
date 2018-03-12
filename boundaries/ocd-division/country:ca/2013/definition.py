# coding: utf-8
from datetime import date

import boundaries


def namer(f):
    import boundaries
    return boundaries.clean_attr('FEDENAME')(f).replace('\u0092', "'")


boundaries.register('Federal electoral districts',  # (2013 Representation Order)
    singular='Federal electoral district',
    domain='Canada',
    last_updated=date(2017, 8, 23),
    name_func=namer,
    id_func=boundaries.attr('FEDUID'),
    slug_func=boundaries.attr('FEDUID'),
    authority='Her Majesty the Queen in Right of Canada',
    source_url='https://open.canada.ca/data/en/dataset/5f1c2e06-405a-4357-9566-872e69ee2ade',
    licence_url='https://open.canada.ca/en/open-government-licence-canada',
    data_url='http://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/files-fichiers/2016/lfed000a16a_e.zip',
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca'},
)
