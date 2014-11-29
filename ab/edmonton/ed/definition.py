from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Edmonton wards',
    domain='Edmonton, AB',
    last_updated=date(2014, 2, 28),
    name_func=lambda f: 'Ward %s' % re.sub(r'\D+0?', '', f.get('NAME')),
    id_func=lambda f: re.sub(r'\D+0?', '', f.get('NAME')),
    authority='City of Edmonton',
    source_url='https://data.edmonton.ca/Administrative/City-of-Edmonton-Ward-Boundaries/yhng-294h?',
    licence_url='http://www.edmonton.ca/city_government/initiatives_innovation/open-data-terms-of-use.aspx',
    data_url='https://data.edmonton.ca/api/geospatial/yhng-294h?method=export&format=Shapefile',
    encoding='iso-8859-1',
    metadata={'geographic_code': '4811061'},
)
