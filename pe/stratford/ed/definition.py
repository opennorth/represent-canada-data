from __future__ import unicode_literals

import re
from datetime import date

import boundaries


def namer(f):
    import boundaries
    n = boundaries.attr('NAME')(f)
    if n == "Kellys Cove":
        return "Kelly's Cove"
    return n

boundaries.register('Stratford wards',
    domain='Stratford, PE',
    last_updated=date(2013, 7, 19),
    name_func=namer,
    id_func=lambda f: re.sub(r'\D', '', f.get('KEY')),
    authority='Elections Prince Edward Island',
    source_url='http://www.electionspei.ca/municipalities/stratford',
    data_url='http://www.electionspei.ca/municipal/details/gis/shp/stratford_wards.zip',
    licence_url='http://www.electionspei.ca/apilicense',
    encoding='iso-8859-1',
    metadata={'geographic_code': '1102080'},
)
