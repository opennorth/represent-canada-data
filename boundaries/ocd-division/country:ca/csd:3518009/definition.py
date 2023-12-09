from datetime import date

import boundaries

boundaries.register('Whitby wards',
    domain='Whitby, ON',
    last_updated=date(2023, 2, 15),
    name_func=boundaries.attr('WARD_DESC'),
    id_func=boundaries.attr('WARD'),
    source_url='https://geohub-whitby.hub.arcgis.com/datasets/Whitby::ward-boundaries/about',
    data_url='https://opendata.arcgis.com/api/v3/datasets/31ab4780b412445db594aaadc2bf0de2_0/downloads/data?format=shp&spatialRefId=26917&where=1%3D1',
    licence_url='https://whitby.maps.arcgis.com/sharing/rest/content/items/223810efc31c40b3aff99dd74f809a97/data',
    authority='Town of Whitby',
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca/csd:3518009'},
)
