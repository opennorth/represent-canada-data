from __future__ import unicode_literals

from datetime import date

import boundaries


boundaries.register('Saskatoon wards',
    domain='Saskatoon, SK',
    last_updated=date(2016, 10, 14),
    name_func=lambda f: f.get('Name').replace(':', ''),
    authority='City of Saskatoon',
    source_url='http://opendata-saskatoon.cloudapp.net/DataBrowser/SaskatoonOpenDataCatalogueBeta/CurrentWardBoundaries',
    data_url='https://saskatoonopendatastorage.blob.core.windows.net/converteddata/kml.CurrentWardBoundaries.zip',
    licence_url='http://opendata-saskatoon.cloudapp.net/TermsOfUse/TermsOfUse',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:4711066'},
)
