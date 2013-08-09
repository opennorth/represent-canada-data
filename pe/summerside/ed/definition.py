#coding: utf-8

from datetime import date
import re

import boundaries

boundaries.register('Summerside wards',
    domain='Summerside, PE',
    last_updated=date(2013, 7, 19),
    name_func=boundaries.dashed_attr('NAME'),
    id_func=lambda f: re.sub(r'\D', '', f.get('KEY')),
    authority='Elections Prince Edward Island',
    source_url='http://www.electionspei.ca/municipalities/summerside',
    data_url='http://www.electionspei.ca/municipal/details/gis/shp/summerside_wards.zip',
    licence_url='http://www.electionspei.ca/api/license/',
    encoding='iso-8859-1',
    geographic_code='1103025',
)
