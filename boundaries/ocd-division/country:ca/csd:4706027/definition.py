from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Regina wards',
    domain='Regina, SK',
    last_updated=date(2014, 11, 25),
    name_func=lambda f: 'Ward %s' % f.get('WARD'),
    id_func=boundaries.attr('WARD'),
    authority='City of Regina',
    source_url='http://open.regina.ca/dataset/wards',
    licence_url='http://www.regina.ca/residents/open-government/open-government-licence/',
    data_url='https://reginaopendata.blob.core.windows.net/opendata/Wards/SHP_ZIP/shp.Wards.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:4706027'},
)
