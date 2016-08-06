# coding: utf-8
from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Kirkland districts',
    domain='Kirkland, QC',
    last_updated=date(2016, 1, 13),
    name_func=boundaries.clean_attr('NOM_DISTRI'),
    authority='Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/elections-2009-districts-electoraux',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/dataset/cbc2aeb1-dc73-487e-9b72-d803db631b15/resource/2b1074a3-2e81-456b-abb8-1ebbb0888562/download/elections-2009-districts-multi-poly.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:2466102'},
    ogr2ogr='''-where "MONTREAL='0' AND NUM_ARR='3'"''',
)
