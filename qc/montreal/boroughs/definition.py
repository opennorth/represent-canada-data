#coding: utf-8
from datetime import date

import boundaries

boundaries.register(u'Montréal boroughs',
    domain=u'Montréal, QC',
    last_updated=date(2014, 2, 1),
    name_func=boundaries.clean_attr('ARROND'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/polygones-arrondissements',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/storage/f/2014-02-01T01%3A40%3A15.962Z/arrondissements-shapefile.zip',
    notes='The Ahuntsic-Cartierville borough is split into two features. We merge them using Quantum GIS.',
    encoding='iso-8859-1',
    metadata={'geographic_code': '2466023'},
)
