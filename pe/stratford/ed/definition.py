from datetime import date
import re

import boundaries

boundaries.register('Stratford, PE wards',
    domain='Stratford, PE',
    last_updated=date(2010, 9, 19),
    name_func=boundaries.attr('NAME'),
    id_func=lambda f: re.sub(r'\D', '', f.get('KEY')),
    authority='Elections Prince Edward Island',
    source_url='http://www.electionspei.ca/municipalities/stratford',
    data_url='http://www.electionspei.ca/municipal/details/gis/shp/stratford_wards.zip',
    license_url='http://www.electionspei.ca/api/license/',
    encoding='iso-8859-1',
)
