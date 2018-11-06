from datetime import date

import boundaries

boundaries.register('Scugog wards',
    domain='Scugog, ON',
    last_updated=date(2018, 10, 1),
    name_func=lambda f: 'Ward %s' % f.get('WARD'),
    id_func=boundaries.attr('WARD'),
    authority='Township of Scugog',
    source_url='https://city-oshawa.opendata.arcgis.com/datasets/DurhamRegion::scugog-ward-boundaries',
    licence_url='https://www.durham.ca/en/regional-government/resources/Documents/OpenDataLicenceAgreement.pdf',
    data_url='https://opendata.arcgis.com/datasets/7cd08057dadd4d45bb7b1868ce244a22_31.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3518020'},
)
