from datetime import date

import boundaries

boundaries.register('Chatham-Kent wards',
    domain='Chatham-Kent, ON',
    last_updated=date(2016, 8, 12),
    name_func=lambda f: 'Ward %s' % f.get('WARD_NO'),
    id_func=boundaries.attr('WARD_NO'),
    authority='Municipality of Chatham-Kent',
    source_url='http://chathamkentopendata-chatham-kent.opendata.arcgis.com/datasets/1f4428dd5d764320b4246d190cfb70cb_0',
    licence_url='https://www.arcgis.com/sharing/rest/content/items/2ffb1ce148804fe4ade2414e6ef10d21/data',
    data_url='http://chathamkentopendata-chatham-kent.opendata.arcgis.com/datasets/1f4428dd5d764320b4246d190cfb70cb_0.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3536020'},
)
