from datetime import date

import boundaries

boundaries.register('Burlington wards',
    domain='Burlington, ON',
    last_updated=date(2018, 3, 13),
    name_func=lambda f: 'Ward %s' % f.get('WARD_NO'),
    id_func=boundaries.attr('WARD_NO'),
    authority='City of Burlington',
    source_url='https://navburl-burlington.opendata.arcgis.com/datasets/ward-boundaries',
    licence_url='https://www.burlington.ca/en/services-for-you/resources/Ongoing_Projects/Open_Data/OpenDataBurlingtonTermsOfUseSeptember192011.pdf',
    data_url='https://opendata.arcgis.com/datasets/73bee9ff196141a2a1e45be8c04ae404_0.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3524002'},
)
