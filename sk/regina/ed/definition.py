from datetime import date

import boundaries

boundaries.register('Regina wards',
    domain='Regina, SK',
    last_updated=date(2013, 6, 24),
    name_func=lambda f: 'Ward %s' % f.get('WARD'),
    id_func=boundaries.attr('WARD'),
    authority='City of Regina',
    source_url='http://openregina.cloudapp.net/DataBrowser/OpenRegina/Wards',
    licence_url='http://www.regina.ca/residents/open-government/data/terms/',
    data_url='https://reginaopendatacatstore.blob.core.windows.net/converteddata/shp.Wards.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '4706027'},
)
