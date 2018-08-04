from datetime import date

import boundaries

boundaries.register('Hamilton wards',
    domain='Hamilton, ON',
    last_updated=date(2018, 8, 4),
    name_func=lambda f: 'Ward %s' % f.get('WARD'),
    id_func=boundaries.attr('WARD'),
    authority='City of Hamilton',
    source_url='https://www.hamilton.ca/city-initiatives/strategies-actions/open-data-program',
    licence_url='https://www.hamilton.ca/city-initiatives/strategies-actions/open-data-licence-terms-and-conditions',
    data_url='http://opendata.hamilton.ca/SHP/WARDS.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3525005'},
)
