from datetime import date

import boundaries

boundaries.register('Census divisions',
    domain='Canada',
    last_updated=date(2011, 11, 28),
    name_func=boundaries.attr('CDNAME'),
    id_func=boundaries.attr('CDUID'),
    slug_func=boundaries.attr('CDUID'),
    authority='Statistics Canada',
    source_url='http://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/bound-limit-eng.cfm',
    licence_url='http://data.gc.ca/eng/open-government-licence-canada',
    data_url='http://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/files-fichiers/gcd_000a11a_e.zip',
    encoding='iso-8859-1',
)