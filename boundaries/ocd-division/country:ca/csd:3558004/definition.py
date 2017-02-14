from datetime import date

import boundaries

boundaries.register('Thunder Bay wards',
    domain='Thunder Bay, ON',
    last_updated=date(2014, 3, 25),
    name_func=boundaries.clean_attr('WARD_NAME'),
    id_func=lambda f: f.get('WARD_NO').replace('00', ''),
    authority='City of Thunder Bay',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3558004'},
)
