from __future__ import unicode_literals

import re
from datetime import date

import boundaries

boundaries.register('Fredericton wards',
    domain='Fredericton, NB',
    last_updated=date(2013, 11, 26),
    name_func=lambda f: re.sub(' / ', '/', f.get('Ward')),
    id_func=boundaries.attr('Ward_Num'),
    authority='City of Fredericton',
    source_url='http://data.fredericton.ca/en/dataset/electoral-wards',
    licence_url='http://www2.gnb.ca/content/dam/gnb/Departments/gs-sg/pdf/OpenDataPolicy.pdf',
    data_url='http://data.fredericton.ca/sites/default/files/wards.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:1310032'},
)
