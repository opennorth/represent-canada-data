from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Lunenburg districts',
    domain='Lunenburg, NS',
    last_updated=date(2014, 3, 25),
    name_func=lambda f: re.sub(' ?- \d+\Z', '', f.get('Label2')),
    id_func=boundaries.attr('Dletter'),
    authority='Municipality of the District of Lunenburg',
    encoding='iso-8859-1',
    metadata={'geographic_code': '1206001'},
)
