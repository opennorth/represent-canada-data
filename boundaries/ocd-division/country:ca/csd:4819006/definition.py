from datetime import date

import boundaries

boundaries.register('Grande Prairie County No. 1 divisions',
    domain='Grande Prairie County No. 1, AB',
    last_updated=date(2017, 12, 1),
    name_func=lambda f: 'Division %s' % f.get('ElectoralD'),
    id_func=boundaries.attr('ElectoralD'),
    authority='County of Grande Prairie No. 1',
    source_url='https://data1-cogp.opendata.arcgis.com/datasets/aec068b7976e432f99b7cbd89fe2abc7_0',
    licence_url='https://www.countygp.ab.ca/EN/main/community/maps-gis/open-data/open-data-licence.html',
    data_url='https://opendata.arcgis.com/datasets/aec068b7976e432f99b7cbd89fe2abc7_0.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:4819006'},
)
