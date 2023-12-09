from datetime import date

import boundaries

boundaries.register('Northwest Territories electoral districts (2013)',
    singular='Northwest Territories electoral district',
    domain='Northwest Territories',
    last_updated=date(2022, 5, 24),  # https://nwtelectoralboundaries.ca/wp-content/uploads/sites/6/2022/05/2021-electoral-boundaries-final-report-web.pdf
    name_func=boundaries.attr('ED'),
    id_func=lambda f: int(f.get('EDNWTF_ID')),
    authority='Her Majesty the Queen in Right of Northwest Territories',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/territory:nt'},
    notes='npx esri-dump fetch https://www.apps.geomatics.gov.nt.ca/arcgis/rest/services/GNWT/Boundaries_LCC/MapServer/2 > boundaries/ocd-division/country:ca/territory:nt/districts.geojson',
)
