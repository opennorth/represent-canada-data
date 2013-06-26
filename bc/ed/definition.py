from datetime import date

import boundaries

boundaries.register('British Columbia electoral districts',
    domain='British Columbia',
    last_updated=date(2013, 06, 25),
    name_func=boundaries.attr('edname'),
    id_func=boundaries.attr('edabbr'),
    authority='Elections BC',
    source_url='http://www3.elections.bc.ca/docs/map/redis12/GIS/Electoral%20District%20Boundaries.zip',
    data_url='http://www3.elections.bc.ca/docs/map/redis12/GIS/Electoral%20District%20Boundaries.zip',
    encoding='iso-8859-1',
)