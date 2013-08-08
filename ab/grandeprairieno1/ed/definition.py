from datetime import date

import boundaries

boundaries.register('Grande Prairie County No. 1 divisions',
    domain='Grande Prairie County No. 1, AB',
    last_updated=date(2012, 6, 18),
    name_func=lambda f: 'Division %s' % f.get('ElectoralD'),
    id_func=boundaries.attr('ElectoralD'),
    authority='County of Grande Prairie No. 1',
    source_url='http://data.countygp.ab.ca/',
    licence_url='http://www.countygp.ab.ca/EN/main/community/maps-gis/open-data/open-data-licence.html',
    data_url='http://data.countygp.ab.ca/data/CouncillorDivisions/Councillor_Divisions.zip',
    encoding='iso-8859-1',
    geographic_code='4819006',
)
