from datetime import date

import boundaries

boundaries.register('Ajax wards',
    domain='Ajax, ON',
    last_updated=date(2017, 6, 13),
    name_func=lambda f: 'Ward %s' % f.get('WARD'),
    id_func=boundaries.attr('WARD'),
    authority='Town of Ajax',
    source_url='http://opendata.ajax.ca/datasets/f441095b72ad4c3da2638a73a0c9e412_23',
    licence_url='http://townofajax.maps.arcgis.com/sharing/rest/content/items/22e2d8e248724d7cb0310dc2db675abd/data',
    data_url='http://opendata.ajax.ca/datasets/f441095b72ad4c3da2638a73a0c9e412_23.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3518005'},
)
