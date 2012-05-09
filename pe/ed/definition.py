#coding: utf8
from datetime import date

import boundaries

def namer(f):
    import boundaries
    n = boundaries.clean_attr('Descriptio')(f)
    if n.lower().startswith('tracadie'):
        return u'Tracadie—Hillsborough Park'
    elif n.lower().startswith('oleary'):
        return u"O'Leary—Inverness"
    return n

boundaries.register('Prince Edward Island electoral districts',
    domain='Prince Edward Island',
    last_updated=date(2011, 12, 12),
    name_func=namer,
    id_func=boundaries.attr('Name'),
    authority='Elections Prince Edward Island',
    source_url='http://www.electionspei.ca/provincial/districts',
    data_url='http://www.electionspei.ca/provincial/details/gis/kml/pei-provincial-districts-all.kml',
    license_url='http://www.electionspei.ca/api/license/',
    notes='The shapefile from gov.pe.ca has 222 features instead of 27. We use the KML from Elections PEI, which we convert to SHP with: ogr2ogr -f "ESRI Shapefile" ed pei-provincial-districts-all.kml',
    encoding='iso-8859-1',
)

# The bad data from gov.pe.ca is at:
# Source: http://www.gov.pe.ca/gis/index.php3?number=77868&lang=E
# Licence: http://www.gov.pe.ca/gis/license_agreement.php3
# Data: http://www.gov.pe.ca/photos/original/prov_elect_dist.SHP.zip
