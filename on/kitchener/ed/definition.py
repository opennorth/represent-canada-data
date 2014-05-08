from datetime import date

import boundaries

# Also available from http://app.kitchener.ca/opendata/shp/wards.zip
boundaries.register('Kitchener wards',
    domain='Kitchener, ON',
    last_updated=date(2013, 2, 20),
    name_func=boundaries.attr('WardName'),
    id_func=boundaries.attr('WardNumber'),
    authority='Regional Municipality of Waterloo',
    source_url='http://www.regionofwaterloo.ca/en/regionalGovernment/WardBoundaries.asp',
    licence_url='http://www.regionofwaterloo.ca/en/regionalGovernment/OpenDataLicence.asp',
    data_url='http://www.regionofwaterloo.ca/opendatadownloads/WardBoundaries.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3530013'},
    ogr2ogr='''-where "Municipali='Kitchener'"''',
)
