from __future__ import unicode_literals

from datetime import date

import boundaries


boundaries.register('Newfoundland and Labrador electoral districts (2006)',
    singular='Newfoundland and Labrador electoral district',
    domain='Newfoundland and Labrador',
    last_updated=date(2012, 9, 27),
    name_func=boundaries.attr('ELEC_DISTR'),
    authority='Her Majesty the Queen in Right of Newfoundland and Labrador',
    source_url='http://www.elections.gov.nl.ca/elections/ElectoralBoundaries/index.html',
    data_url='http://www.elections.gov.nl.ca/elections/ElectoralBoundaries/Distibution_2011.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/province:nl'},
)
