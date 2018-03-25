from datetime import date

import boundaries


boundaries.register('Saskatoon wards',
    domain='Saskatoon, SK',
    last_updated=date(2016, 10, 14),
    name_func=boundaries.clean_attr('Name'),
    authority='City of Saskatoon',
    source_url='http://opendata-saskatoon.cloudapp.net/DataBrowser/SaskatoonOpenDataCatalogueBeta/MunicipalWardArea#param=NOFILTER--DataView--Results',
    licence_url='http://opendata-saskatoon.cloudapp.net/TermsOfUse/TermsOfUse',
    data_url='http://opendata-saskatoon.cloudapp.net:8080/v1/SaskatoonOpenDataCatalogueBeta/MunicipalWardArea/?format=kml',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:4711066'},
)
