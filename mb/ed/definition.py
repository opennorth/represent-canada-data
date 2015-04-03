from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Manitoba electoral districts',
    domain='Manitoba',
    last_updated=date(2011, 12, 14),
    name_func=boundaries.dashed_attr('ED'),
    authority='Her Majesty the Queen in Right of Manitoba',
    source_url='http://represent:weakpass@mli2.gov.mb.ca/adminbnd/index.html',
    licence_url='http://mli2.gov.mb.ca/app/register/app/index.php',
    data_url='http://represent:weakpass@mli2.gov.mb.ca/adminbnd/shp_zip_files/bdy_mb_electoral_divisions_shp.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '46'},
)
