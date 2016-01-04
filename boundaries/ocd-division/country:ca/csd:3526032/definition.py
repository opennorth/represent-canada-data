from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Welland wards',
    domain='Welland, ON',
    last_updated=date(2015, 12, 1),
    name_func=lambda f: 'Ward %s' % f.get('Ward'),
    id_func=boundaries.attr('Ward'),
    authority='City of Welland',
    source_url='http://www.welland.ca/open/OpendataResp.asp?utitle=Ward%20Boundaries',
    licence_url='http://www.welland.ca/open/OpendataTermUse.asp',
    data_url='http://www.welland.ca/open/Datasheets/Welland_ward_boundaries.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3526032'},
    prj='http://spatialreference.org/ref/epsg/26917/prj/',
)
