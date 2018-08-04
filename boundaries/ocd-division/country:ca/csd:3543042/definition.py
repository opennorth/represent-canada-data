from datetime import date

import boundaries

boundaries.register('Barrie wards',
    domain='Barrie, ON',
    last_updated=date(2018, 2, 16),
    name_func=lambda f: 'Ward %s' % f.get('WARD_NO'),
    id_func=boundaries.attr('WARD_NO'),
    authority='City of Barrie',
    source_url='http://public-barrie.opendata.arcgis.com/datasets/wards',
    licence_url='https://www.barrie.ca/Online%20Services/PublishingImages/OpenData_Images/COB_DataLicense.pdf',
    data_url='https://opendata.arcgis.com/datasets/f811e32b3f244bc08f3a4e2082c67401_0.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3543042'},
)
