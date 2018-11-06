from datetime import date

import boundaries

boundaries.register('Census subdivisions',
    domain='Canada',
    last_updated=date(2016, 11, 8),
    name_func=boundaries.attr('CSDNAME'),
    id_func=boundaries.attr('CSDUID'),
    slug_func=boundaries.attr('CSDUID'),
    authority='Her Majesty the Queen in Right of Canada',
    source_url='https://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/bound-limit-2016-eng.cfm',
    licence_url='https://open.canada.ca/en/open-government-licence-canada',
    data_url='https://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/files-fichiers/2016/lcsd000b16a_e.zip',
    encoding='utf-8',
)
