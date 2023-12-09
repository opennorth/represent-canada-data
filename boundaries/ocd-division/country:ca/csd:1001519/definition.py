from datetime import date

import boundaries

boundaries.register("St. John's wards",
    domain="St. John's, NL",
    # "The ward boundaries for the City of St. John's were established in October, 1993"
    # https://apps.stjohns.ca/wardlookup/WardLookup.aspx
    last_updated=date(2023, 12, 9),
    name_func=boundaries.attr('WARDNAME'),
    id_func=boundaries.attr('WARD'),
    authority="City of St. John's",
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:1001519'},
    is_valid_func=lambda f: f.get('WARDNAME'),
    notes='npx esri-dump fetch https://map.stjohns.ca/mapsrv/rest/services/WardMap/MapServer/0 > boundaries/ocd-division/country:ca/csd:1001519/wards.geojson',
)
