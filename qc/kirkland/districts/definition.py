# coding: utf-8
from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Kirkland districts',
    domain='Kirkland, QC',
    last_updated=date(2013, 10, 6),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority='Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/elections-2009-districts-electoraux',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/storage/f/2013-10-06T16:49:49.153Z/elections-2009-districts-multi-poly.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:2466102'},
    ogr2ogr='''-where "MONTREAL='0' AND NUM_ARR='3'"''',
)
