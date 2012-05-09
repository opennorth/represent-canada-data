from datetime import date

import boundaries

boundaries.register('British Columbia electoral districts',
    domain='British Columbia',
    last_updated=date(2011, 12, 12),
    name_func=boundaries.attr('edname'),
    id_func=boundaries.attr('edabbr'),
    authority='Elections BC',
    source_url='http://www.elections.bc.ca/index.php/voting/electoral-maps-profiles/geographic-information-system-spatial-data-files-2011/',
    data_url='http://www.elections.bc.ca/docs/map/redis11/GIS/ED_Province.exe',
    encoding='iso-8859-1',
)