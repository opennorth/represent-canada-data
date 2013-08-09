from datetime import date

import boundaries

boundaries.register('Haldimand County wards',
    domain='Haldimand County, ON',
    last_updated=date(2012, 9, 25),
    name_func=boundaries.attr('Ward'),
    id_func=lambda f: re.sub(r'\D', '', f.get('Ward')),
    authority='The Corporation of Haldimand County',
    encoding='iso-8859-1',
    geographic_code='3528018',
)
