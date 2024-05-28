from datetime import date

import boundaries

boundaries.register('Peel wards',
    domain='Peel, ON',
    last_updated=date(2023, 10, 6),
    name_func=boundaries.attr('WardName'),
    id_func=boundaries.attr('WardID'),
    authority='Regional Municipality of Peel',
    source_url='https://data.peelregion.ca/datasets/RegionofPeel::peel-ward-boundary',
    licence_url='https://data.peelregion.ca/pages/license',
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca/cd:3521'},
    notes='npx esri-dump fetch "https://services6.arcgis.com/ONZht79c8QWuX759/arcgis/rest/services/Peel_Ward_Boundary/FeatureServer/0" > boundaries/ocd-division/country:ca/cd:3521/wards.geojson',
)
