from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('British Columbia electoral districts',
    domain='British Columbia',
    last_updated=date(2012, 9, 27),
    name_func=boundaries.attr('edName'),
    id_func=boundaries.attr('edAbbr'),
    authority='Her Majesty the Queen in Right of British Columbia',
    source_url='http://www.elections.bc.ca/index.php/maps/electoral-maps/geographic-information-system-spatial-data-files-2012/',
    data_url='http://www3.elections.bc.ca/docs/map/redis12/GIS/Electoral%20District%20Boundaries.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/province:bc'},
)
