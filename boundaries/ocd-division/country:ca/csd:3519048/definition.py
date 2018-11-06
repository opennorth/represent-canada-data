from datetime import date

import boundaries

boundaries.register('Newmarket wards',
    domain='Newmarket, ON',
    last_updated=date(2016, 8, 6),
    name_func=lambda f: 'Ward %s' % f.get('WARD'),
    id_func=boundaries.attr('WARD'),
    authority='Town of Newmarket',
    encoding='iso-8859-1',
    source_url='http://open.newmarket.ca/opendata/navigo/#/show/4e404ea7c3cb6e3c?disp=6b625f5',
    licence_url='https://www.newmarket.ca/TownGovernment/Documents/Newmarket_OpenData_Licence.pdf',
    extra={'division_id': 'ocd-division/country:ca/csd:3519048'},
)
