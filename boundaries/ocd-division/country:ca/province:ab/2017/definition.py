from datetime import date

import boundaries

boundaries.register('Alberta electoral districts (2017)',
    singular='Alberta electoral district',
    domain='Alberta',
    last_updated=date(2018, 3, 1),
    name_func=boundaries.attr('EDName2017'),
    id_func=boundaries.attr('EDNumber20'),
    authority='Her Majesty the Queen in Right of Alberta',
    source_url='http://www.elections.ab.ca/resources/2019-boundary-maps/',
    licence_url='https://open.alberta.ca/licence',
    data_url='http://www.elections.ab.ca/wp-content/uploads/2019Boundaries_ED-Shapefiles.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/province:ab'},
)
