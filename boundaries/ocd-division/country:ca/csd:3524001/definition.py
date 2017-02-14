from datetime import date

import boundaries

boundaries.register('Oakville wards',
    domain='Oakville, ON',
    last_updated=date(2016, 4, 1),
    name_func=boundaries.attr('FULL_NAME'),
    id_func=boundaries.attr('WARD'),
    authority='Town of Oakville',
    source_url='http://oakville.ca/data/ward-boundaries.html',
    licence_url='http://oakville.ca/data/open_data_licence.html',
    data_url='http://opendata.oakville.ca/Ward_Boundaries/Ward_Boundaries.shp.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3524001'},
)
