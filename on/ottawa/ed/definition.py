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
    data_url='http://data.ottawa.ca/en/storage/f/2013-05-15T145937/Wards-2010-SHP.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3506008'},
)
