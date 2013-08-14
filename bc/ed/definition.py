from datetime import date

import boundaries

boundaries.register('British Columbia electoral districts',
    domain='British Columbia',
    last_updated=date(2012, 9, 27),
    name_func=boundaries.attr('edname'),
    id_func=boundaries.attr('edabbr'),
    authority='Elections BC',
    source_url='http://www.elections.bc.ca/index.php/maps/electoral-maps-profiles/geographic-information-system-spatial-data-files-2012/',
    data_url='http://www3.elections.bc.ca/docs/map/redis12/GIS/Electoral%20District%20Boundaries.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '59'},
)
