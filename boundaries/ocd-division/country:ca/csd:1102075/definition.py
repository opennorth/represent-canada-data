import re
from datetime import date

import boundaries

boundaries.register('Charlottetown wards',
    domain='Charlottetown, PE',
    last_updated=date(2013, 7, 19),
    name_func=boundaries.attr('NAME'),
    id_func=lambda f: re.sub(r'\D', '', f.get('KEY')),
    authority='Elections Prince Edward Island',
    source_url='http://www.electionspei.ca/index.php?number=1051954&lang=F',
    data_url='http://www.electionspei.ca/municipal/details/gis/shp/charlottetown_wards.zip',
    licence_url='http://www.electionspei.ca/apilicense',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:1102075'},
)
