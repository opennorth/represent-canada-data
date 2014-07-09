from datetime import date

import boundaries

boundaries.register('Federal electoral districts (next election)',
    domain='Canada',
    last_updated=date(2014, 5, 12),
    name_func=boundaries.clean_attr('ENNAME'),
    id_func=boundaries.attr('FEDNUM'),
    slug_func=boundaries.attr('FEDNUM'),
    authority='Her Majesty the Queen in Right of Canada',
    source_url='http://www.geobase.ca/geobase/en/search.do?produit=fed&language=en',
    licence_url='http://data.gc.ca/eng/open-government-licence-canada',
    data_url='http://ftp2.cits.rncan.gc.ca/pub/geobase/official/fed_cf/shp_eng/fed_cf_CA_2_0_shp_en.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '01'},
)
