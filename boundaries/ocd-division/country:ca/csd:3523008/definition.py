from datetime import date

import boundaries

boundaries.register('Guelph wards',
    domain='Guelph, ON',
    last_updated=date(2018, 7, 13),
    name_func=lambda f: 'Ward %s' % f.get('WARD'),
    id_func=boundaries.attr('WARD'),
    authority='City of Guelph',
    source_url='http://data.open.guelph.ca/dataset/guelph-wards',
    licence_url='http://data.open.guelph.ca/pages/open-government-licence',
    data_url='http://data.open.guelph.ca/datafiles/gis/Wards.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3523008'},
)
