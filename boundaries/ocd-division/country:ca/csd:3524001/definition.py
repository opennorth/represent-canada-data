from datetime import date

import boundaries

boundaries.register('Oakville wards',
    domain='Oakville, ON',
    last_updated=date(2018, 6, 11),
    name_func=lambda f: 'Ward %s' % f.get('Ward'),
    id_func=boundaries.attr('Ward'),
    authority='Town of Oakville',
    source_url='https://portal-exploreoakville.opendata.arcgis.com/datasets/toak::2018-ward-boundaries',
    licence_url='https://www.oakville.ca/data/open_data_licence.html',
    data_url='https://opendata.arcgis.com/datasets/36137fb86deb4431b53450cf16370a3b_0.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3524001'},
)
