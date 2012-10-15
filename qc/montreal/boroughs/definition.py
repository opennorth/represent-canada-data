#coding: utf-8
from datetime import date

import boundaries

boundaries.register(u'Montréal boroughs',
    domain=u'Montréal, QC',
    last_updated=date(2011, 11, 8),
    name_func=boundaries.clean_attr('ARROND'),
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/fiche/polygones-arrondissements/',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet',
    data_url='http://depot.ville.montreal.qc.ca/polygones-arrondissements/data.zip',
    notes='The Ahuntsic-Cartierville borough is split into two features. We merge them using Quantum GIS.',
    encoding='iso-8859-1',
)
