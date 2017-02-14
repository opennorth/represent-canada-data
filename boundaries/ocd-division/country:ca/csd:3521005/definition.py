from datetime import date

import boundaries

boundaries.register('Mississauga wards',
    domain='Mississauga, ON',
    last_updated=date(2010, 12, 16),
    name_func=lambda f: 'Ward %s' % f.get('Name'),
    id_func=boundaries.attr('Name'),
    authority='City of Mississauga',
    source_url='http://www.mississauga.ca/portal/residents/publicationsopendatacatalogue',
    licence_url='http://www5.mississauga.ca/research_catalogue/CityofMississauga_TermsofUse.pdf',
    data_url='http://www5.mississauga.ca/research_catalogue/G_5_Municipal_Wards.kmz',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3521005'},
)
