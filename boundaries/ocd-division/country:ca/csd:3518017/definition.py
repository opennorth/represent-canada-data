import re
from datetime import date

import boundaries

boundaries.register('Clarington wards',
    domain='Clarington, ON',
    # https://www.clarington.net/en/news/council-highlights-from-the-january-18-2021-meeting.aspx
    last_updated=date(2021, 1, 18),
    name_func=boundaries.attr('WARD'),
    id_func=lambda f: re.sub(r'\D', '', f.get('WARD')),
    authority='Municipality of Clarington',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3518017'},
    notes='npx esri-dump fetch https://gis.clarington.net/arcgis/rest/services/Community/Ward_Boundary_Map/MapServer/1 > boundaries/ocd-division/country:ca/csd:3518017/wards.geojson',
)
