from datetime import date

import boundaries

boundaries.register('Ottawa wards',
    domain='Ottawa, ON',
    last_updated=date(2012, 7, 22),
    name_func=boundaries.dashed_attr('WARD_EN'),
    id_func=boundaries.attr('WARD_NUM'),
    authority='City of Ottawa',
    source_url='http://data.ottawa.ca/en/dataset/wards-2010',
    licence_url='http://ottawa.ca/en/mobile-apps-and-open-data/open-data-terms-use',
    data_url='http://data.ottawa.ca/en/dataset/wards-2010/resource/6db490f2-f1db-4c7b-bf5a-cc0826a98776',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3506008'},
)
