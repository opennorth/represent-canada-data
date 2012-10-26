from datetime import date

import boundaries

boundaries.register('St. Catharines wards',
    domain='St. Catharines, ON',
    last_updated=date(2012, 9, 18),
    name_func=boundaries.clean_attr('WardName'),
    authority='City of St. Catharines',
    notes='We use a shapefile received via email.',
    encoding='iso-8859-1',
)
