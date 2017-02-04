from __future__ import unicode_literals

from datetime import date

import boundaries

sets = {
    3530004: 'North Dumfries',
    3530010: 'Cambridge',
    # Also available from http://app.kitchener.ca/opendata/shp/wards.zip
    3530013: 'Kitchener',
    3530016: 'Waterloo',
    3530020: 'Wilmot',
    3530027: 'Wellesley',
    3530035: 'Woolwich',
}

for geographic_code, name in sets.items():
    boundaries.register('%s wards' % name,
        domain='%s, ON' % name,
        last_updated=date(2015, 1, 6),
        name_func=lambda f: 'Ward %s' % f.get('WardNumber'),
        id_func=boundaries.attr('WardNumber'),
        authority='Regional Municipality of Waterloo',
        source_url='http://www.regionofwaterloo.ca/en/regionalGovernment/WardBoundaries.asp',
        licence_url='http://www.regionofwaterloo.ca/en/regionalGovernment/OpenDataLicence.asp',
        data_url='http://www.regionofwaterloo.ca/opendatadownloads/WardBoundaries.zip',
        encoding='iso-8859-1',
        extra={'division_id': 'ocd-division/country:ca/csd:%d' % geographic_code},
        is_valid_func=lambda f, name=name: f.get('Municipali') == name,
        skip_crc32=True,
    )
