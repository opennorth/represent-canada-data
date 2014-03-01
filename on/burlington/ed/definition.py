from datetime import date

import boundaries

boundaries.register('Burlington wards',
    domain='Burlington, ON',
    last_updated=date(2014, 2, 27),
    name_func=lambda f: 'Ward %s' % f.get('WARD_NO'),
    id_func=boundaries.attr('WARD_NO'),
    authority='City of Burlington',
    source_url='http://cms.burlington.ca/Page12956.aspx',
    licence_url='http://cms.burlington.ca/AssetFactory.aspx?did=18762',
    data_url='http://cms.burlington.ca/AssetFactory.aspx?did=30505',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3524002'},
)
