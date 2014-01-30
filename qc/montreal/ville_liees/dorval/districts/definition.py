#coding: utf-8
from datetime import date

import boundaries

# @see http://www.ville.dorval.qc.ca/en/downloads/pdf/Map_Electoral_Districts.pdf
def ider(f):
    import boundaries
    return {
        'Désiré-Girouard': '1',
        'La Présentation': '2',
        'Fénelon': '3',
        'Pine Beach': '4',
        'Strathmore': '5',
        'Surrey': '6',
    }[boundaries.attr('NOM_DISTRI')]

boundaries.register(u'Dorval districts',
    domain=u'Dorval, QC',
    last_updated=date(2013, 8, 21),
    name_func=boundaries.attr('NOM_DISTRI'),
    id_func=ider,
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/fiche/elections-2009-districts/',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://depot.ville.montreal.qc.ca/elections-2009-districts/multi-poly/data.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '2466087'},
    ogr2ogr='''-where "MONTREAL='0'" -where "NUM_ARR='1'"''',
)
