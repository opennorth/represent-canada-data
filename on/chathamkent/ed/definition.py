from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Chatham-Kent wards',
    domain='Chatham-Kent, ON',
    last_updated=date(2013, 10, 8),
    name_func=boundaries.attr('WardName'),
    id_func=boundaries.attr('WardNum'),
    authority='Municipality of Chatham-Kent',
    source_url='http://chathamkentopendata.chatham-kent.opendata.arcgis.com/',
    licence_url='https://www.arcgis.com/sharing/rest/content/items/2ffb1ce148804fe4ade2414e6ef10d21/data',
    data_url='http://www.chatham-kent.ca/sp_training/OpenData/Documents/Wards.shp.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3536020'},
)
