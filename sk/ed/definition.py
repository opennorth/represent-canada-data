from __future__ import unicode_literals

from datetime import date

import boundaries


def namer(f):
    n = boundaries.dashed_attr('CON_NAME')(f)
    if n == 'Regina North East':
        return 'Regina Northeast'
    return n

boundaries.register('Saskatchewan electoral districts',
    domain='Saskatchewan',
    last_updated=date(2010, 10, 12),
    name_func=namer,
    id_func=boundaries.attr('CON_NUM'),
    authority='Her Majesty the Queen in Right of Saskatchewan',
    source_url='https://www.geosask.ca/',
    licence_url='https://www.geosask.ca/Portal/jsp/terms_popup.jsp',
    data_url='ftp://portaldata:freedata@ftp.isc.ca/PackagedData/ElectionsSask/Boundaries.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '47'},
)
