from __future__ import unicode_literals

import re
from datetime import date

import boundaries

boundaries.register('Lunenburg districts',
    domain='Lunenburg, NS',
    last_updated=date(2014, 3, 25),
    name_func=lambda f: re.sub(' ?- \d+\Z', '', f.get('Label2')),
    id_func=boundaries.attr('Dletter'),
    authority='Municipality of the District of Lunenburg',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:1206001'},
)
