from datetime import date

import boundaries

boundaries.register('Ottawa wards',
    domain='Ottawa, ON',
    last_updated=date(2012, 7, 22),
    name_func=boundaries.dashed_attr('WARD_EN'),
    id_func=boundaries.attr('WARD_NUM'),
    authority='City of Ottawa',
    source_url='http://app06.ottawa.ca/en/city_hall/statisticsdata/opendata/info/wards2010/index.htm',
    licence_url='http://ottawa.ca/en/mobile-apps-and-open-data/open-data-terms-use',
    data_url='http://app06.ottawa.ca/cs/groups/content/@webottawa/documents/pdf/mdaw/mty4/~edisp/odata0335.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3506008'},
)
