from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Chatham-Kent wards',
    domain='Chatham-Kent, ON',
    last_updated=date(2013, 10, 8),
    name_func=boundaries.attr('WardName'),
    id_func=boundaries.attr('WardNum'),
    authority='Municipality of Chatham-Kent',
    source_url='http://www.chatham-kent.ca/sp_training/OpenData/Pages/DataCatalogue.aspx',
    data_url='http://www.chatham-kent.ca/sp_training/OpenData/Documents/Wards.shp.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3536020'},
)
