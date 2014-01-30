from datetime import date

import boundaries

def namer(f):
    import boundaries
    return re.sub(' Ward \d+\Z', '', boundaries.clean_attr('NAME')(f))

boundaries.register('Peterborough wards',
    domain='Peterborough, ON',
    last_updated=date(2012, 9, 05),
    name_func=namer,
    id_func=lambda f: re.sub(r'\D', '', f.get('NAME')),
    authority='City of Peterborough',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3515014'},
)
