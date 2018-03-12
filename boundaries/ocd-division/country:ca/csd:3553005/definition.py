from datetime import date

import boundaries

boundaries.register('Greater Sudbury wards',
    domain='Greater Sudbury, ON',
    last_updated=date(2016, 8, 12),
    name_func=lambda f: 'Ward %s' % f.get('WardNumber'),
    id_func=boundaries.attr('WardNumber'),
    authority='City of Greater Sudbury',
    source_url='http://data-sudbury.opendata.arcgis.com/datasets/2fd80bad151b42cea9a6ee103d0dbc3d_0',
    licence_url='https://www.greatersudbury.ca/city-hall/open-government/open-data/licence/',
    data_url='http://data-sudbury.opendata.arcgis.com/datasets/2fd80bad151b42cea9a6ee103d0dbc3d_0.zip',
    is_valid_func=lambda f: f.get('WardNumber'),
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3553005'},
)
