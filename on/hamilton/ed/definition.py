from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Hamilton wards',
    domain='Hamilton, ON',
    last_updated=date(2015, 10, 2),
    name_func=lambda f: 'Ward %s' % f.get('WARD'),
    id_func=boundaries.attr('WARD'),
    authority='City of Hamilton',
    source_url='http://www.hamilton.ca/city-initiatives/strategies-actions/open-accessible-data',
    licence_url='http://www.hamilton.ca/city-initiatives/strategies-actions/open-accessible-data',
    data_url='http://opendata.hamilton.ca/SHP/Wards.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3525005'},
)
