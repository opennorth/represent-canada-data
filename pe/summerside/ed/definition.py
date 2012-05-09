#coding: utf-8

from datetime import date
import re

import boundaries

boundaries.register('Summerside wards',
    domain='Summerside, PE',
    last_updated=date(2010, 9, 19),
    name_func=boundaries.dashed_attr('NAME'),
    id_func=lambda f: re.sub(r'\D', '', f.get('KEY')),
    authority='Elections Prince Edward Island',
    source_url='http://www.electionspei.ca/municipalities/summerside',
    data_url='http://www.electionspei.ca/municipal/details/gis/shp/summerside_wards.zip',
    license_url='http://www.electionspei.ca/api/license/',
    notes='The Tracadie—Hillsborough Park district is misspelled.',
    encoding='iso-8859-1',
)
