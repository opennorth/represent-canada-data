from datetime import date

import boundaries

boundaries.register('London wards',
    domain='London, ON',
    last_updated=date(2012, 2, 13),
    name_func=lambda f: 'Ward %s' % f.get('WARDS'),
    id_func=boundaries.attr('WARDS'),
    authority='City of London',
    source_url='http://www.london.ca/d.aspx?s=/Open_Data/Data_Catalogue.htm',
    licence_url='http://www.london.ca/d.aspx?s=/Open_Data/Open_Data_Terms_Use.htm',
    data_url='http://www.london.ca/OpenData/ShapeFiles_Zipped/2010_electoral_wards.zip',
    notes='We use NAD83 / UTM zone 17N (EPSG:26917) from http://spatialreference.org/ref/epsg/26917/',
    encoding='iso-8859-1',
    geographic_code='3539036',
)
