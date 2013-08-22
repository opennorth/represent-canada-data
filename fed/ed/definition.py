from datetime import date

import boundaries

boundaries.register('Federal electoral districts',
    domain='Canada',
    last_updated=date(2011, 11, 28),
    name_func=boundaries.clean_attr('FEDENAME'),
    id_func=boundaries.attr('FEDUID'),
    slug_func=boundaries.attr('FEDUID'),
    authority='Her Majesty the Queen in Right of Canada',
    source_url='http://data.gc.ca/data/en/dataset/48f10fb9-78a2-43a9-92ab-354c28d30674',
    licence_url='http://data.gc.ca/eng/open-government-licence-canada',
    data_url='http://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/files-fichiers/gfed000a11a_e.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '01'},
)
