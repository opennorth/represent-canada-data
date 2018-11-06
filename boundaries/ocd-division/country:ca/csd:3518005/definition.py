from datetime import date

import boundaries

boundaries.register('Ajax wards',
    domain='Ajax, ON',
    last_updated=date(2018, 11, 4),
    name_func=lambda f: 'Ward %s' % f.get('WARD_NUM'),
    id_func=boundaries.attr('WARD_NUM'),
    authority='Town of Ajax',
    source_url='http://opendata.ajax.ca/datasets/2018-ward-boundaries',
    licence_url='http://townofajax.maps.arcgis.com/sharing/rest/content/items/22e2d8e248724d7cb0310dc2db675abd/data',
    data_url='https://opendata.arcgis.com/datasets/c45b387629404a6fb0a2f59f501b124c_28.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3518005'},
)
