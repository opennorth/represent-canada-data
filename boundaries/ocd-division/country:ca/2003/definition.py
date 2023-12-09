# coding: utf-8
from datetime import date

import boundaries


def namer(f):
    import boundaries
    n = boundaries.clean_attr('FEDENAME')(f)
    # @see http://www.parl.gc.ca/HousePublications/Publication.aspx?Language=E&Mode=1&DocId=6684609&File=4
    if n == 'Western Arctic':
        return 'Northwest Territories'
    else:
        return n


boundaries.register('Federal electoral districts (2003 Representation Order)',
    singular='Federal electoral district',
    domain='Canada',
    last_updated=date(2011, 11, 28),  # historical
    name_func=namer,
    id_func=boundaries.attr('FEDUID'),
    slug_func=boundaries.attr('FEDUID'),
    authority='Her Majesty the Queen in Right of Canada',
    source_url='https://open.canada.ca/data/en/dataset/48f10fb9-78a2-43a9-92ab-354c28d30674',
    licence_url='https://open.canada.ca/en/open-government-licence-canada',
    data_url='https://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/files-fichiers/gfed000a11a_e.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca'},
)
