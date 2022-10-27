import re
from datetime import date

import boundaries

boundaries.register('Ontario electoral districts (2022)',
    singular='Ontario electoral district',
    domain='Ontario',
    last_updated=date(2021, 3, 29),
    name_func=boundaries.dashed_attr('ED_NAME'),
    id_func=lambda f: re.sub(r'\A0', '', f.get('ED_NO')),
    authority='Her Majesty the Queen in right of Ontario, as represented by the Chief Electoral Officer',
    source_url='https://www.elections.on.ca/en/voting-in-ontario/electoral-district-shapefiles.html',
    data_url='https://www.elections.on.ca/content/dam/NGW/sitecontent/2017/preo/shapefiles/Electoral%20District%20Shapefile%20-%202022%20General%20Election.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/province:on'},
)