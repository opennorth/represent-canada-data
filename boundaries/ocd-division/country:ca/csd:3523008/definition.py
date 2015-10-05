from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Guelph wards',
    domain='Guelph, ON',
    last_updated=date(2014, 2, 7),
    name_func=boundaries.attr('NAME'),
    id_func=boundaries.attr('WARD'),
    authority='City of Guelph',
    source_url='http://openguelph.wpengine.com/dataset/ward-boundaries/',
    data_url='http://openguelph.wpengine.com/wp-content/uploads/2014/02/wards.zip',
    licence_url='http://openguelph.wpengine.com/open-data-guelph/city-of-guelph-open-government-licence/',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3523008'},
)
