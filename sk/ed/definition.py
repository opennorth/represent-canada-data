from datetime import date

import boundaries

def namer(f):
    import boundaries
    n = boundaries.dashed_attr('CON_NAME')(f)
    if n == 'Regina North East':
        return u'Regina Northeast'
    return n

boundaries.register('Saskatchewan electoral districts',
    domain='Saskatchewan',
    last_updated=date(2010, 10, 12),
    name_func=namer,
    id_func=boundaries.attr('CON_NUM'),
    authority='Elections Saskatchewan',
    source_url='https://www.geosask.ca/',
    licence_url='https://www.geosask.ca/Portal/jsp/terms_popup.jsp',
    data_url='ftp://portaldata:freedata@ftp.isc.ca/PackagedData/ElectionsSask/Boundaries.zip',
    encoding='iso-8859-1',
    geographic_code='47',
)
