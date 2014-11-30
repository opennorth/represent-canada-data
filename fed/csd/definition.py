from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Census subdivisions',
    domain='Canada',
    last_updated=date(2011, 11, 28),
    name_func=boundaries.attr('CSDNAME'),
    id_func=boundaries.attr('CSDUID'),  # Census subdivision names are not unique across provinces and territories
    slug_func=boundaries.attr('CSDUID'),
    authority='Her Majesty the Queen in Right of Canada',
    source_url='http://data.gc.ca/data/en/dataset/8b577e89-8c56-4048-b4db-b9d5c753d419',
    licence_url='http://open.canada.ca/en/open-government-licence-canada',
    data_url='http://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/files-fichiers/gcsd000a11a_e.zip',
    encoding='iso-8859-1',
)
