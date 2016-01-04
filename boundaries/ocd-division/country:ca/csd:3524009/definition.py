from __future__ import unicode_literals

import re
from datetime import date

import boundaries

boundaries.register('Milton wards',
    domain='Milton, ON',
    last_updated=date(2016, 1, 4),
    name_func=lambda f: 'Ward %s' % re.search('WARD (\d+)', f.get('Descriptio')).group(1),
    id_func=lambda f: re.search('WARD (\d+)', f.get('Descriptio')).group(1),
    authority='Town of Milton',
    source_url='http://icreateopendata.public.esolutionsgroup.ca/home/details/1a3d6722-a3a9-4591-abc8-ac55c060a65a',
    licence_url='http://www.milton.ca/en/resourcesGeneral/Open_Data/Milton_Open_Data_Terms_V1.pdf',
    data_url='http://icreateopendata.public.esolutionsgroup.ca/home/ServeFile/1a3d6722-a3a9-4591-abc8-ac55c060a65a?FileType=6',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3524009'},
)
