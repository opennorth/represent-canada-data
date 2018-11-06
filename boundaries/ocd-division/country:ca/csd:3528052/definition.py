from datetime import date

import boundaries

boundaries.register('Norfolk County wards',
    domain='Norfolk County, ON',
    last_updated=date(2018, 4, 2),
    name_func=lambda f: 'Ward %s' % f.get('Ward'),
    id_func=boundaries.attr('Ward'),
    authority='City of Norfolk County',
    source_url='http://opendata.norfolkcounty.ca/datasets/wards',
    licence_url='http://data-norfolk.opendata.arcgis.com/pages/terms-of-use',
    data_url='https://opendata.arcgis.com/datasets/d421a70e797349caa9ca5c6d93a516b5_0.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3528052'},
)
