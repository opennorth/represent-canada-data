from datetime import date

import boundaries

boundaries.register('Hamilton wards',
    domain='Hamilton, ON',
    last_updated=date(2018, 10, 31),
    name_func=lambda f: 'Ward %s' % f.get('WARD'),
    id_func=boundaries.attr('WARD'),
    authority='City of Hamilton',
    source_url='http://open.hamilton.ca/datasets/8b0b1f2bf8bb4e1da3a1bf567b17b77f_7',
    licence_url='https://www.hamilton.ca/city-initiatives/strategies-actions/open-data-licence-terms-and-conditions',
    data_url='https://opendata.arcgis.com/datasets/8b0b1f2bf8bb4e1da3a1bf567b17b77f_7.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3525005'},
)
