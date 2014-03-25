# coding: utf-8
from datetime import date

import boundaries

# Superceded by DGEQ.
boundaries.register('Saint-Jean-sur-Richelieu districts',
    domain='Saint-Jean-sur-Richelieu, QC',
    last_updated=date(2012, 10, 31),
    name_func=lambda f: 'District %s' % re.sub(r'\A0', '', f.get('DISTRICT')),
    id_func=lambda f: re.sub(r'\A0', '', f.get('DISTRICT')),
    authority='Ville de Saint-Jean-sur-Richelieu',
    encoding='iso-8859-1',
    metadata={'geographic_code': '2456083'},
)
