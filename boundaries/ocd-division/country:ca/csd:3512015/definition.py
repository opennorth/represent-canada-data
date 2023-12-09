from datetime import date

import boundaries

boundaries.register('Quinte West wards',
    domain='Quinte West, ON',
    # "The City of Quinte West was formed in 1998 by the amalgamation of four former municipalities"
    # https://quintewest.ca/council-city-administration/ward-map/
    last_updated=date(2023, 12, 9),
    name_func=boundaries.attr('mapguide'),
    id_func=boundaries.attr('WardNumber'),
    authority='City of Quinte West',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3512015'},
    notes='npx esri-dump fetch "https://services3.arcgis.com/cpi3xYswHz1VWunb/arcgis/rest/services/Quinte_West_Boundary_Detailed_Public_(Public)/FeatureServer/0" > boundaries/ocd-division/country:ca/csd:3512015/wards.geojson',
)
