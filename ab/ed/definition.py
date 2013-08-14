from datetime import date

import boundaries

boundaries.register('Alberta electoral districts',
    domain='Alberta',
    last_updated=date(2011, 11, 25),
    name_func=boundaries.clean_attr('EDNAME'),
    id_func=boundaries.attr('EDNUMBER'),
    authority='Government of Alberta',
    source_url='http://www.altalis.com/prod_base_bound.html',
    licence_url='http://www.altalis.com/agreement.html',
    data_url='http://www.altalis.com/Samples/Provincial%20Electoral%20Divisions.zip',
    encoding='iso-8859-1',
    geographic_code='48',
)
