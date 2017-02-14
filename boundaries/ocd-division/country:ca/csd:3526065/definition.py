from datetime import date

import boundaries

boundaries.register('Grimsby wards',
    domain='Grimsby, ON',
    last_updated=date(2016, 1, 1),
    name_func=lambda f: 'Ward %s' % f.get('Ward'),
    id_func=boundaries.attr('Ward'),
    authority='Town of Grimsby',
    licence_url='https://niagaraopendata.ca/pages/open-government-license-2-0-grimsby',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3526065'},
)
