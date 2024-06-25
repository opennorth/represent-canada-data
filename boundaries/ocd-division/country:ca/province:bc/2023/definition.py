from datetime import date

import boundaries

boundaries.register('British Columbia electoral districts (2023 Redistribution)',
    singular='British Columbia electoral district',
    domain='British Columbia',
    last_updated=date(2023, 3, 29),
    name_func=boundaries.attr('ED_NAME'),
    id_func=boundaries.attr('ED_ABBREV'),
    authority='Her Majesty the Queen in Right of British Columbia',
    source_url='https://catalogue.data.gov.bc.ca/dataset/provincial-electoral-districts-electoral-boundaries-redistribution-2023',
    licence_url='https://www.elections.bc.ca/docs/EBC-Open-Data-Licence.pdf',
    # Google Chrome: "Export data or view details from the BC Geographic Warehouse (custom download)" "Access/Download"
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca/province:bc'},
)
