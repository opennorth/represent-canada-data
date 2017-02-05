from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Alberta electoral districts',  # (2010)
    singular='Alberta electoral district',
    domain='Alberta',
    last_updated=date(2016, 1, 6),
    name_func=boundaries.attr('EDName2010'),
    id_func=boundaries.attr('EDNum2010'),
    authority='Her Majesty the Queen in Right of Alberta',
    source_url='https://open.alberta.ca/opendata/electoral-division',
    licence_url='https://open.alberta.ca/licence',
    data_url='http://www.elections.ab.ca/wp-content/uploads/EDs_Act2010_FINAL.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/province:ab'},
)
