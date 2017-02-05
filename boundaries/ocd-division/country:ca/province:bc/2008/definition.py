from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('British Columbia electoral districts',  # (2008 Redistribution)
    singular='British Columbia electoral district',
    domain='British Columbia',
    last_updated=date(2016, 11, 30),
    name_func=boundaries.attr('ED_NAME'),
    id_func=boundaries.attr('ED_ABBREV'),
    authority='Her Majesty the Queen in Right of British Columbia',
    source_url='https://catalogue.data.gov.bc.ca/dataset/provincial-electoral-districts-electoral-boundaries-redistribution-2008',
    licence_url='http://www.elections.bc.ca/docs/EBC-Open-Data-Licence.pdf',
    data_url='https://catalogue.data.gov.bc.ca/dataset/c864f294-d302-4630-bde3-a0551735b309/resource/dc567bfb-488b-4765-b544-6bd02f61f736/download/edsre2008.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/province:bc'},
)
