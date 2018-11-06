from datetime import date

import boundaries

boundaries.register('Uxbridge wards',
    domain='Uxbridge, ON',
    last_updated=date(2018, 11, 3),
    name_func=lambda f: 'Ward %s' % f.get('WARD'),
    id_func=boundaries.attr('WARD'),
    authority='Township of Uxbridge',
    source_url='https://city-oshawa.opendata.arcgis.com/datasets/DurhamRegion::uxbridge-ward-boundaries',
    licence_url='https://www.durham.ca/en/regional-government/resources/Documents/OpenDataLicenceAgreement.pdf',
    data_url='https://opendata.arcgis.com/datasets/6881ab21ee78498e90d7317d20b3f8e9_32.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3518029'},
)
