from datetime import date

import boundaries

boundaries.register('Lincoln wards',
    domain='Lincoln, ON',
    last_updated=date(2016, 7, 12),
    name_func=lambda f: 'Ward %s' % f.get('Ward'),
    id_func=boundaries.attr('Ward'),
    authority='Town of Lincoln',
    encoding='iso-8859-1',
    source_url='https://niagaraopendata.ca/dataset/lincoln-ward-map',
    licence_url='https://niagaraopendata.ca/pages/open-government-license-2-0-town-of-lincoln',
    data_url='https://www.niagaraopendata.ca//dataset/354a9f3b-9cbd-496a-9e03-9cd7627bf4d3/resource/4e01f8aa-e9fe-4871-8914-305a44ccd7ab/download/lincolnwards.zip',
    extra={'division_id': 'ocd-division/country:ca/csd:3526057'},
)
