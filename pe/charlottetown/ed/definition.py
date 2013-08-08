from datetime import date
import re

import boundaries

boundaries.register('Charlottetown wards',
    domain='Charlottetown, PE',
    last_updated=date(2010, 9, 19),
    name_func=boundaries.attr('NAME'),
    id_func=lambda f: re.sub(r'\D', '', f.get('KEY')),
    authority='Elections Prince Edward Island',
    source_url='http://www.electionspei.ca/municipalities/charlottetown',
    data_url='http://www.electionspei.ca/municipal/details/gis/shp/charlottetown_wards.zip',
    licence_url='http://www.electionspei.ca/api/license/',
    encoding='iso-8859-1',
    geographic_code='1102075',
)
