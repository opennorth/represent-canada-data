from datetime import date

import boundaries

boundaries.register('Markham wards',
    domain='Markham, ON',
    last_updated=date(2018, 12, 19),
    name_func=lambda f: 'Ward %s' % int(f.get('WARD')),
    id_func=lambda f: int(f.get('WARD')),
    source_url='http://data-markham.opendata.arcgis.com/datasets/e18e684f2f004f0e98d707cad60234be_0',
    licence_url='http://data-markham.opendata.arcgis.com/pages/terms-of-use',
    data_url='https://opendata.arcgis.com/datasets/e18e684f2f004f0e98d707cad60234be_0.zip?outSR=%7B%22wkid%22%3A26917%2C%22latestWkid%22%3A26917%7D',
    authority='City of Markham',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3519036'},
)
