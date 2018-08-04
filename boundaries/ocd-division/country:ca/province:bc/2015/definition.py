from datetime import date

import boundaries

boundaries.register('British Columbia electoral districts (2015 Redistribution)',
    singular='British Columbia electoral district',
    domain='British Columbia',
    last_updated=date(2016, 11, 30),
    name_func=boundaries.attr('ED_NAME'),
    id_func=boundaries.attr('ED_ABBREV'),
    authority='Her Majesty the Queen in Right of British Columbia',
    source_url='https://catalogue.data.gov.bc.ca/dataset/provincial-electoral-districts-electoral-boundaries-redistribution-2015',
    licence_url='https://www.elections.bc.ca/docs/EBC-Open-Data-Licence.pdf',
    data_url='https://catalogue.data.gov.bc.ca/dataset/9530a41d-6484-41e5-b694-acb76e212a58/resource/34eedf53-c60b-4237-bf6e-81228a51ab12/download/edsre2015.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/province:bc'},
)
