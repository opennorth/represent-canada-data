from datetime import date

import boundaries

boundaries.register('Chatham-Kent wards',
    domain='Chatham-Kent, ON',
    last_updated=date(2021, 4, 6),
    name_func=lambda f: 'Ward %s' % f.get('WARD_NO'),
    id_func=boundaries.attr('WARD_NO'),
    authority='Municipality of Chatham-Kent',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3536020'},
    notes='npx esri-dump fetch https://services1.arcgis.com/BlSm9A1poQIGIz9S/arcgis/rest/services/CK_Wards/FeatureServer/0 > boundaries/ocd-division/country:ca/csd:3536020/wards.geojson',
)
