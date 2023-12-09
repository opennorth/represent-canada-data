from datetime import date

import boundaries

boundaries.register('Greater Sudbury wards',
    domain='Greater Sudbury, ON',
    last_updated=date(2023, 5, 31),
    name_func=boundaries.attr('WardName_E'),
    id_func=boundaries.attr('WardNumber'),
    authority='City of Greater Sudbury',
    source_url='https://opendata.greatersudbury.ca/datasets/Sudbury::ward-map-and-council-layer/about',
    data_url='https://opendata.arcgis.com/api/v3/datasets/2fd80bad151b42cea9a6ee103d0dbc3d_0/downloads/data?format=shp&spatialRefId=3857&where=1%3D1',
    licence_url='https://www.greatersudbury.ca/city-hall/open-government/open-data/licence/',
    is_valid_func=lambda f: f.get('WardNumber'),
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca/csd:3553005'},
)
