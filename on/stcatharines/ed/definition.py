from datetime import date

import boundaries

boundaries.register('St. Catharines wards',
    domain='St. Catharines, ON',
    last_updated=date(2012, 9, 18),
    name_func=boundaries.clean_attr('WardName'),
    authority='City of St. Catharines',
    encoding='iso-8859-1',
    geographic_code='3526053',
)
