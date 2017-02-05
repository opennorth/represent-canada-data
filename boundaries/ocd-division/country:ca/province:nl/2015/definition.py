from __future__ import unicode_literals

from datetime import date

import boundaries


def namer(f):
    import boundaries
    return boundaries.clean_attr('DIST_NAME')(f) or boundaries.clean_attr('Elec_Distr')(f)


boundaries.register('Newfoundland and Labrador electoral districts',  # (2015)
    singular='Newfoundland and Labrador electoral district',
    domain='Newfoundland and Labrador',
    last_updated=date(2016, 1, 7),
    name_func=namer,
    authority='Her Majesty the Queen in Right of Newfoundland and Labrador',
    source_url='http://www.elections.gov.nl.ca/elections/ElectoralBoundaries/index.html',
    data_url='http://www.elections.gov.nl.ca/elections/ElectoralBoundaries/Island_2015.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/province:nl'},
    notes='Download http://www.elections.gov.nl.ca/elections/ElectoralBoundaries/Labrador_2015.zip. Save Island_2015_EB_Poly_50k.shp as EPSG:2962. Merge the two *_2015_EB_Poly_50k.shp shapefiles.',
)
