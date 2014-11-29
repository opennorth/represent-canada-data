from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Halifax districts',
    domain='Halifax, NS',
    last_updated=date(2014, 9, 12),
    name_func=boundaries.attr('DISTNAME'),
    id_func=boundaries.attr('DIST_ID'),
    authority='Halifax Regional Municipality',
    source_url='https://www.halifaxopendata.ca/Zoning/Polling-District/e7u6-by35',
    data_url='https://www.halifaxopendata.ca/api/geospatial/e7u6-by35?method=export&format=Shapefile',
    licence_url='https://www.halifaxopendata.ca/terms',
    encoding='iso-8859-1',
    metadata={'geographic_code': '1209034'},
)
