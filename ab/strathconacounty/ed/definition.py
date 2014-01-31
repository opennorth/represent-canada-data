from datetime import date

import boundaries

boundaries.register('Strathcona County wards',
    domain='Strathcona County, AB',
    last_updated=date(2013, 10, 16),
    name_func=boundaries.attr('Name'),
    id_func=lambda f: re.sub('\D', '', f.get('Name')),
    authority='Strathcona County',
    source_url='http://www.strathcona.ca/local-government/strathcona-county-elections/election-2013-open-data/#ward',
    licence_url='http://www.strathcona.ca/local-government/strathcona-county-elections/election-2013-open-data/#licence',
    data_url='http://www.strathcona.ca/files/files/at-lls-2013election-ward_boundaries.kmz',
    encoding='iso-8859-1',
    metadata={'geographic_code': '4811052'},
)
