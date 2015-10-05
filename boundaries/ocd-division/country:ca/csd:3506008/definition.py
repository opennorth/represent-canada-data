from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Ottawa wards',
    domain='Ottawa, ON',
    last_updated=date(2013, 5, 15),
    name_func=boundaries.clean_attr('WARD_EN'),
    id_func=boundaries.attr('WARD_NUM'),
    authority='City of Ottawa',
    source_url='http://data.ottawa.ca/en/dataset/wards-2010',
    licence_url='http://ottawa.ca/en/mobile-apps-and-open-data/open-data-terms-use',
    data_url='http://data.ottawa.ca/dataset/13deeed4-1cd5-4a68-a10d-9839d3677446/resource/6abe3aa1-4ad8-4061-bb18-dad5054b85fb/download/wards-2010-2.shp.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3506008'},
)
