from datetime import date

import boundaries

boundaries.register('Welland wards',
    domain='Welland, ON',
    last_updated=date(2017, 1, 14),
    name_func=lambda f: 'Ward %s' % f.get('Ward'),
    id_func=boundaries.attr('Ward'),
    authority='City of Welland',
    source_url='https://niagaraopendata.ca/dataset/city-of-welland-ward-boundaries',
    licence_url='https://niagaraopendata.ca/pages/open-government-license-2-0-city-of-welland',
    data_url='https://www.niagaraopendata.ca//dataset/438bb42f-5678-451b-9b59-33f85f460fe0/resource/31d495aa-0448-4450-80c6-4bcf75ed4790/download/city-of-welland-ward-boundaries.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3526032'},
    prj='http://spatialreference.org/ref/epsg/26917/prj/',
)
