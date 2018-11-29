from datetime import date

import boundaries

boundaries.register('Whitby wards',
    domain='Whitby, ON',
    last_updated=date(2013, 1, 8),
    name_func=boundaries.attr('WARD_DESC'),
    id_func=lambda f: f.get('WARD_TEXT').replace('0', ''),
    authority='Town of Whitby',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3518009'},
)
