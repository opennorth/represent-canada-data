from datetime import date

import boundaries

boundaries.register('Peterborough wards',
    domain='Peterborough, ON',
    last_updated=date(2012, 9, 05),
    name_func=boundaries.attr('NAME'),
    id_func=boundaries.attr('WARD_ID'),
    authority='Town of Peterborough',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3515014'},
)
