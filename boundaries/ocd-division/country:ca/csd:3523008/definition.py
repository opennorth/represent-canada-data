from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Guelph wards',
    domain='Guelph, ON',
    last_updated=date(2014, 2, 7),
    name_func=boundaries.attr('NAME'),
    id_func=boundaries.attr('WARD'),
    authority='City of Guelph',
    source_url='http://data.open.guelph.ca/dataset/guelph-wards',
    data_url='http://data.open.guelph.ca/datafiles/gis/Wards.kml',
    licence_url='http://data.open.guelph.ca/pages/open-government-licence',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3523008'},
)
