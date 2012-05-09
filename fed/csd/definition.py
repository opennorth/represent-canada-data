from datetime import date

import boundaries

boundaries.register('Census subdivisions',
    domain='Canada',
    last_updated=date(2011, 11, 28),
    name_func=boundaries.attr('CSDNAME'),
    id_func=boundaries.attr('CSDUID'),
    slug_func=boundaries.attr('CSDUID'),
    authority='Statistics Canada',
    source_url='http://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/bound-limit-eng.cfm',
    licence_url='http://www.statcan.gc.ca/reference/licence-eng.html',
    data_url='http://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/files-fichiers/gcsd000a11a_e.zip',
    notes='Census subdivision names are not unique across provinces.',
    encoding='iso-8859-1',
)