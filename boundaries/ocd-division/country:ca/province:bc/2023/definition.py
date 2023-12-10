from datetime import date

import boundaries

boundaries.register('British Columbia electoral districts (2023 Redistribution)',
    singular='British Columbia electoral district',
    domain='British Columbia',
    last_updated=date(2023, 3, 29),
    name_func=boundaries.attr('Dist_Name'),
    id_func=boundaries.attr('Dist_ID'),
    authority='Her Majesty the Queen in Right of British Columbia',
    source_url='https://catalogue.data.gov.bc.ca/dataset/provincial-electoral-districts-electoral-boundaries-redistribution-2023',
    licence_url='https://www.elections.bc.ca/docs/EBC-Open-Data-Licence.pdf',
    data_url='https://bcebc.ca/wp-content/uploads/Proposed_Electoral_Districts._shp.zip',
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca/province:bc'},
)
