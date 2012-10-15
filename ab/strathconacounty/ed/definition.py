from datetime import date

import boundaries

boundaries.register('Strathcona County wards',
    domain='Strathcona County, AB',
    last_updated=date(2012, 10, 11),
    name_func=lambda f: 'Ward %s' % f.get('Ward'),
    id_func=boundaries.attr('Ward'),
    authority='Strathcona County',
    notes='We use a shapefile received via email.',
    encoding='iso-8859-1',
)
