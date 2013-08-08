from datetime import date

import boundaries

boundaries.register('Nova Scotia electoral districts',
    domain='Nova Scotia',
    last_updated=date(2011, 3, 29),
    name_func=boundaries.dashed_attr('DISTRICT'),
    id_func=boundaries.attr('DIST_NO'),
    authority='Elections Nova Scotia',
    source_url='http://electionsnovascotia.ca/content/maps-0',
    data_url='http://electionsnovascotia.ca/sites/default/files/NS_EDBoundaries2012.zip',
    notes='The Halifax Citadel-Sable Island district is split into two features. We merge them using Quantum GIS. The geospatial metadata file contains the license.',
    encoding='iso-8859-1',
)
