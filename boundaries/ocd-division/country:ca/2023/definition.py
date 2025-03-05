from datetime import date

import boundaries


def namer(f):
    import boundaries
    return boundaries.clean_attr('ED_NAMEE')(f).replace('\u0092', "'")


boundaries.register('2023 Federal electoral districts',  # (2023 Representation Order)
    singular='2023 Federal electoral district',
    domain='Canada',
    last_updated=date(2023, 2, 25),
    name_func=namer,
    id_func=boundaries.attr('FED_NUM '),
    slug_func=boundaries.attr('FED_NUM '),
    authority='Her Majesty the Queen in Right of Canada',
    source_url='https://open.canada.ca/data/en/dataset/18bf3ea7-1940-46ec-af52-9ba3f77ed708',
    licence_url='https://open.canada.ca/en/open-government-licence-canada',
    data_url='https://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/files-fichiers/2016/lfed000a16a_e.zip',
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca'},
)
