# coding: utf-8
from datetime import date

import boundaries

boundaries.register('Sherbrooke boroughs',
    domain='Sherbrooke, QC',
    last_updated=date(2013, 12, 16),
    name_func=boundaries.clean_attr('NOM'),
    id_func=boundaries.attr('NUMERO'),
    source_url='http://donnees.ville.sherbrooke.qc.ca/catalogue-de-donnees/fiche-du-jeu-de-donnees/jeu/arrondissements.html',
    data_url='http://donnees.ville.sherbrooke.qc.ca/fileadmin/donnees_ouvertes/Arrondissement.shp.zip',
    licence_url='http://donnees.ville.sherbrooke.qc.ca/licence.html',
    authority='Ville de Sherbrooke',
    encoding='iso-8859-1',
    metadata={'geographic_code': '2443027'},
)
