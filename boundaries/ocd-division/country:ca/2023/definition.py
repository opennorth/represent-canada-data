from datetime import date

import boundaries


def namer(f):
    import boundaries
    return boundaries.clean_attr('ED_NAMEE')(f).replace('\u0092', "'")


boundaries.register('Federal electoral districts (2023 Representation Order)',
    singular='Federal electoral district',
    domain='Canada',
    last_updated=date(2024, 12, 17),
    name_func=namer,
    id_func=boundaries.attr('FED_NUM'),
    slug_func=boundaries.attr('FED_NUM'),
    authority='Her Majesty the Queen in Right of Canada',
    source_url='https://open.canada.ca/data/en/dataset/18bf3ea7-1940-46ec-af52-9ba3f77ed708',
    licence_url='https://open.canada.ca/en/open-government-licence-canada',
    data_url='https://ftp.maps.canada.ca/pub/elections_elections/Electoral-districts_Circonscription-electorale/federal_electoral_districts_boundaries_2023/FED_CA_2023_EN-SHP.zip',
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca'},
)
