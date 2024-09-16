from datetime import date

import boundaries

boundaries.register('Ottawa wards',
    domain='Ottawa, ON',
    last_updated=date(2024, 6, 13),
    name_func=boundaries.clean_attr('NAME'),
    id_func=boundaries.attr('WARD'),
    authority='City of Ottawa',
    source_url='https://open.ottawa.ca/datasets/ottawa::wards-2022-2026/about',
    licence_url='https://ottawa.ca/en/city-hall/open-transparent-and-accountable-government/open-data',
    data_url='https://opendata.arcgis.com/api/v3/datasets/5aec8bb2e9c84132afe9522ce513afb8_105/downloads/data?format=shp&spatialRefId=4326&where=1%3D1',
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca/csd:3506008'},
)
