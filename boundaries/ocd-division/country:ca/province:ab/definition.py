from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Alberta electoral districts',
    domain='Alberta',
    last_updated=date(2012, 6, 4),
    name_func=boundaries.clean_attr('EDNAME'),
    id_func=boundaries.attr('EDNUMBER'),
    authority='Her Majesty the Queen in Right of Alberta',
    source_url='http://www.altalis.com/products/base/20k_base_features.html',
    licence_url='http://data.alberta.ca/licence',
    # The data_url contains multiple shapefiles, and the URL expires.
    # data_url='http://data.altalis.com/AltalisDataDownload/Download/525711F29A214C1AB5ED8F5578A983C3',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/province:ab'},
)
