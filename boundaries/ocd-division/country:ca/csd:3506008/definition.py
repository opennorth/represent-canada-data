from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Ottawa wards',
    domain='Ottawa, ON',
    last_updated=date(2016, 1, 8),
    name_func=boundaries.clean_attr('WARD_EN'),
    id_func=boundaries.attr('WARD_NUM'),
    authority='City of Ottawa',
    source_url='http://data.ottawa.ca/en/dataset/wards-2014',
    licence_url='http://ottawa.ca/en/mobile-apps-and-open-data/open-data-terms-use',
    data_url='http://data.ottawa.ca/dataset/8321248d-0b86-47cd-9c83-c848a1bc0098/resource/8152e707-fc28-409c-9bbe-8cb9f88dca86/download/wards-2014shp.shp.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3506008'},
)
