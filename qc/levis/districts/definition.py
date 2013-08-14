#coding: utf-8
from datetime import date

import boundaries

boundaries.register(u'Lévis districts',
    domain=u'Lévis, QC',
    last_updated=date(2012, 5, 30),
    name_func=boundaries.clean_attr('NOM'),
    id_func=boundaries.attr('NUMERO'),
    authority=u'Ville de Lévis',
    encoding='iso-8859-1',
    metadata={'geographic_code': '2425213'},
)
