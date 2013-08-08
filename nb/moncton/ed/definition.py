from datetime import date

import boundaries

boundaries.register('Moncton wards',
    domain='Moncton, NB',
    last_updated=date(2012, 8, 21),
    name_func=lambda f: 'Ward %s' % f.get('WARDNUMB'),
    id_func=boundaries.attr('WARDNUMB'),
    authority='City of Moncton',
    notes='We use a shapefile received via email with NAD83(CSRS) / New Brunswick Stereographic (EPSG:2953) from http://spatialreference.org/ref/epsg/2953/prj/.',
    encoding='iso-8859-1',
    geographic_code='1307022',
)
