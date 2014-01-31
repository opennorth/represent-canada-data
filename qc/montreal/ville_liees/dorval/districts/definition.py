#coding: utf-8
from datetime import date

import boundaries

# @see http://www.ville.dorval.qc.ca/en/downloads/pdf/Map_Electoral_Districts.pdf
def ider(f):
    import boundaries
    return {
        u'Désiré-Girouard': '1',
        u'La Présentation': '2',
        u'Fénelon': '3',
        u'Pine Beach': '4',
        u'Strathmore': '5',
        u'Surrey': '6',
    }[boundaries.attr('NOM_DISTRI')(f)]

boundaries.register(u'Dorval districts',
    domain=u'Dorval, QC',
    last_updated=date(2013, 8, 21),
    name_func=boundaries.attr('NOM_DISTRI'),
    id_func=ider,
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/elections-2009-districts-electoraux',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/storage/f/2013-10-06T16:49:49.153Z/elections-2009-districts-multi-poly.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '2466087'},
    ogr2ogr='''-where "MONTREAL='0'" -where "NUM_ARR='1'"''',
)
