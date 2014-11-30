from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Census divisions',
    domain='Canada',
    last_updated=date(2011, 11, 28),
    name_func=boundaries.attr('CDNAME'),
    id_func=boundaries.attr('CDUID'),
    slug_func=boundaries.attr('CDUID'),
    authority='Her Majesty the Queen in Right of Canada',
    source_url='http://open.canada.ca/data/en/dataset/515dbfa9-9069-4877-8fe8-177edaa4ca76',
    licence_url='http://open.canada.ca/en/open-government-licence-canada',
    data_url='http://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/files-fichiers/gcd_000a11a_e.zip',
    encoding='iso-8859-1',
)
