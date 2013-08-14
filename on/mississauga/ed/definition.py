from datetime import date

import boundaries

boundaries.register('Mississauga wards',
    domain='Mississauga, ON',
    last_updated=date(2010, 12, 16),
    name_func=boundaries.attr('Name'),
    id_func=lambda f: re.sub(r'\D', '', f.get('Name')),
    authority='City of Mississauga',
    source_url='http://www.mississauga.ca/portal/residents/publicationsopendatacatalogue',
    licence_url='http://www.mississauga.ca/file/COM/CityOfMississaugaTermsOfUse.pdf',
    data_url='http://www5.mississauga.ca/research_catalogue/G_5_Municipal_Wards.kmz',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3521005'},
)
