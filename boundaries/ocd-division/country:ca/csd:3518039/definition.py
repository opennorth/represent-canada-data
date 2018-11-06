from datetime import date

import boundaries

boundaries.register('Brock wards',
    domain='Brock, ON',
    last_updated=date(2018, 11, 2),
    name_func=lambda f: 'Ward %s' % f.get('WARD'),
    id_func=boundaries.attr('WARD'),
    authority='Township of Brock',
    source_url='https://city-oshawa.opendata.arcgis.com/datasets/DurhamRegion::brock-ward-boundaries',
    licence_url='https://www.durham.ca/en/regional-government/resources/Documents/OpenDataLicenceAgreement.pdf',
    data_url='https://opendata.arcgis.com/datasets/f48be88029db4e959269cf1d0773998a_30.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3518039'},
)
