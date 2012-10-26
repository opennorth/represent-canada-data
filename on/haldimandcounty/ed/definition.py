from datetime import date

import boundaries

boundaries.register('Haldimand County wards',
    domain='Haldimand County, ON',
    last_updated=date(2012, 9, 25),
    name_func=boundaries.attr('Ward'),
    id_func=lambda f: re.sub(r'\D', '', f.get('Ward')),
    authority='The Corporation of Haldimand County',
    notes='We use a shapefile received via email.',
    encoding='iso-8859-1',
)
