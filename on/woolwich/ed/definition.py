from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Woolwich wards',
    domain='Woolwich, ON',
    last_updated=date(2015, 1, 6),
    name_func=boundaries.attr('WardName'),
    id_func=boundaries.attr('WardNumber'),
    authority='Regional Municipality of Waterloo',
    source_url='http://www.regionofwaterloo.ca/en/regionalGovernment/WardBoundaries.asp',
    licence_url='http://www.regionofwaterloo.ca/en/regionalGovernment/OpenDataLicence.asp',
    data_url='http://www.regionofwaterloo.ca/opendatadownloads/WardBoundaries.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3530035'},
    ogr2ogr='''-where "Municipali='Woolwich'"''',
    skip_crc32=True,
)
