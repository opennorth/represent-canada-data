from datetime import date

import boundaries

boundaries.register('Saskatoon wards',
    domain='Saskatoon, SK',
    last_updated=date(2012, 5, 14),
    name_func=lambda f: 'Ward %s' % f.get('Ward'),
    id_func=boundaries.attr('Ward'),
    authority='City of Saskatoon',
    notes='Ward 1 is split into two features. We merge them using Quantum GIS.',
    encoding='iso-8859-1',
    geographic_code='4711066',
)
