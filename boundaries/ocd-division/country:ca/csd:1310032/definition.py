from datetime import date

import boundaries

boundaries.register('Fredericton wards',
    domain='Fredericton, NB',
    last_updated=date(2017, 11, 16),
    name_func=boundaries.attr('Label'),
    id_func=boundaries.attr('Order_'),
    authority='City of Fredericton',
    source_url='http://data-fredericton.opendata.arcgis.com/datasets/wards-2016--quartiers-2016',
    licence_url='https://www2.gnb.ca/content/dam/gnb/Departments/gs-sg/pdf/OpenDataPolicy.pdf',
    data_url='https://opendata.arcgis.com/datasets/fa0dadc5e5204fdfb98df9872ed1ceb5_0.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:1310032'},
)
