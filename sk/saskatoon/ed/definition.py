from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Saskatoon wards',
    domain='Saskatoon, SK',
    last_updated=date(2015, 5, 22),
    name_func=boundaries.clean_attr('Name'),
    authority='City of Saskatoon',
    source_url='http://opendata-saskatoon.cloudapp.net/DataBrowser/SaskatoonOpenDataCatalogueBeta/CurrentWardBoundaries',
    data_url='https://saskatoonopendatastorage.blob.core.windows.net/converteddata/kml.CurrentWardBoundaries.zip',
    licence_url='http://opendata-saskatoon.cloudapp.net/TermsOfUse/TermsOfUse',
    encoding='iso-8859-1',
    metadata={'geographic_code': '4711066'},
)
