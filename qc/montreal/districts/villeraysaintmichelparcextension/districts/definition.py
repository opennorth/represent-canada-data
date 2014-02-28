# coding: utf-8
from datetime import date

import boundaries

boundaries.register(u'Villeray—Saint-Michel—Parc-Extension districts',
    domain=u'Villeray—Saint-Michel—Parc-Extension, Montréal, QC',
    last_updated=date(2013, 10, 16),
    name_func=lambda f: re.sub(u'', u'—', f.get('NOM_DISTRI')),  # control character, m-dash
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/elections-2013-districts-electoraux',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/storage/f/2013-10-16T14%3A16%3A09.092Z/districtelect.zip',
    encoding='iso-8859-1',
    metadata={'ocd_division': u'ocd-division/country:ca/csd:2466023/borough:villeray~saint-michel~parc-extension'},
    ogr2ogr=u'''-where "ARRONDISSE='Villeray-Saint-Michel-Parc-Extension'"''',
)
