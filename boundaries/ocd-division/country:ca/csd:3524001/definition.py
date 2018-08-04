from datetime import date

import boundaries

boundaries.register('Oakville wards',
    domain='Oakville, ON',
    last_updated=date(2016, 4, 1),
    name_func=boundaries.attr('FULL_NAME'),
    id_func=boundaries.attr('WARD'),
    authority='Town of Oakville',
    # 2018-10-22: https://portal-exploreoakville.opendata.arcgis.com/datasets/toak::2018-ward-boundaries
    source_url='https://portal-exploreoakville.opendata.arcgis.com/datasets/toak::ward-boundaries',
    licence_url='https://www.oakville.ca/data/open_data_licence.html',
    data_url='https://opendata.arcgis.com/datasets/06e1062918f043258ebcada195527120_0.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3524001'},
)
