import re
from datetime import date

import boundaries


boundaries.register('Saskatoon wards',
    domain='Saskatoon, SK',
    last_updated=date(2016, 10, 14),
    name_func=lambda f: f.get('Name').replace(':', ''),
    id_func=lambda f: re.sub(r'\D', '', f.get('Name')),
    authority='City of Saskatoon',
    source_url='http://opendata-saskatoon.cloudapp.net/DataBrowser/SaskatoonOpenDataCatalogueBeta/CurrentWardBoundaries',
    data_url='https://saskatoonopendatastorage.blob.core.windows.net/converteddata/kml.CurrentWardBoundaries.zip',
    licence_url='http://opendata-saskatoon.cloudapp.net/TermsOfUse/TermsOfUse',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:4711066'},
)
