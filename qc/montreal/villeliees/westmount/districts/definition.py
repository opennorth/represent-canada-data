# coding: utf-8
from datetime import date

import boundaries

boundaries.register(u'Westmount districts',
    domain=u'Westmount, QC',
    last_updated=date(2013, 10, 6),
    name_func=lambda f: 'District %s' % re.sub(r'\D', '', f.get('NOM_DISTRI')),
    id_func=lambda f: re.sub(r'\D', '', f.get('NOM_DISTRI')),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/elections-2009-districts-electoraux',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/storage/f/2013-10-06T16:49:49.153Z/elections-2009-districts-multi-poly.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '2466032'},
    ogr2ogr='''-where "MONTREAL='0' AND NUM_ARR='4'"''',
)
