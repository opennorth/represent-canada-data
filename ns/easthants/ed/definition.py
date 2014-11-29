from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('East Hants districts',
    domain='East Hants, NS',
    last_updated=date(2014, 3, 25),
    name_func=lambda f: f.get('District').replace(' Sett.', ' Settlement'),
    id_func=boundaries.attr('Polling_No'),
    authority='Municipality of East Hants',
    encoding='iso-8859-1',
    metadata={'geographic_code': '1208008'},
)
