from datetime import date

import boundaries

boundaries.register('Brampton wards',
    domain='Brampton, ON',
    last_updated=date(2023, 10, 6),
    name_func=lambda f: 'Ward %s' % f.get('WardNumber'),
    id_func=boundaries.attr('WardNumber'),
    authority='Regional Municipality of Peel',
    source_url='https://data.peelregion.ca/datasets/RegionofPeel::peel-ward-boundary',
    licence_url='https://data.peelregion.ca/pages/license',
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca/csd:3521010'},
    is_valid_func=lambda f: f.get('Municipali') == 'Brampton',
    notes='npx esri-dump fetch "https://services6.arcgis.com/ONZht79c8QWuX759/arcgis/rest/services/Peel_Ward_Boundary/FeatureServer/0" > boundaries/ocd-division/country:ca/csd:3521010/wards.geojson',
)
