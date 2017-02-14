from datetime import date

import boundaries


def namer(f):
    import boundaries
    n = boundaries.dashed_attr('CON_NAME')(f)
    if n == 'Regina North East':
        return 'Regina Northeast'
    return n


boundaries.register('Saskatchewan electoral districts (Representation Act, 2002)',
    singular='Saskatchewan electoral district',
    domain='Saskatchewan',
    last_updated=date(2010, 10, 12),
    name_func=namer,
    id_func=boundaries.attr('CON_NUM'),
    authority='Her Majesty the Queen in Right of Saskatchewan',
    source_url='https://www.geosask.ca/',
    licence_url='https://www.geosask.ca/Portal/jsp/terms_popup.jsp',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/province:sk'},
)
