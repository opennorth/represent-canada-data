from datetime import date

import boundaries

boundaries.register('Thunder Bay wards',
    domain='Thunder Bay, ON',
    last_updated=date(2019, 3, 14),
    name_func=boundaries.clean_attr('WARD_NAME'),  # all caps
    id_func=lambda f: f.get('WARD_NO').replace('00', ''),  # 100, etc.
    authority='City of Thunder Bay',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3558004'},
    notes='env NODE_TLS_REJECT_UNAUTHORIZED=0 npx esri-dump fetch https://ctb.gisportal.thunderbay.ca/web/rest/services/Webmaps/GeneralMap/MapServer/3 > boundaries/ocd-division/country:ca/csd:3558004/wards.geojson',
)
