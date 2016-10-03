from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Brantford wards',
    domain='Brantford, ON',
    last_updated=date(2016, 8, 12),
    name_func=boundaries.attr('WARD_NAME'),
    id_func=boundaries.attr('WARD'),
    authority='City of Brantford',
    source_url='http://data.brantford.opendata.arcgis.com/datasets/10acbe7b336a428e892b8aa5f3383fbe_0',
    licence_url='http://data.brantford.opendata.arcgis.com/',
    data_url='http://data.brantford.opendata.arcgis.com/datasets/10acbe7b336a428e892b8aa5f3383fbe_0.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3529006'},
)
