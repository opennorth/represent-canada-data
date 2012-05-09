from datetime import date

import boundaries

def namer(f):
    import boundaries
    n = boundaries.clean_attr('ELEC_DISTR')(f)
    if n == 'Ths Isles of Notre Dame':
        return u'The Isles of Notre Dame'
    return n

boundaries.register('Newfoundland and Labrador electoral districts',
    domain='Newfoundland and Labrador',
    last_updated=date(2011, 12, 13),
    name_func=namer,
    authority='Government of Newfoundland and Labrador',
    notes='We use a shapefile received via email. The shapefile has the MLA name and party, though these may be out-of-date.',
    encoding='iso-8859-1',
)