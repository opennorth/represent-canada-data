# coding: utf-8
from datetime import date

import boundaries

boundaries.register(u'Les Rivières districts',
    domain=u'Les Rivières, Québec, QC',
    last_updated=date(2014, 3, 1),
    name_func=lambda f: re.sub(u'', u'—', f.get('NOM')), # unknown character, m-dash
    id_func=boundaries.attr('CODE'),
    authority=u'Ville de Québec',
    source_url='http://donnees.ville.quebec.qc.ca/donne_details.aspx?jdid=2',
    licence_url='https://creativecommons.org/licenses/by/4.0/legalcode',
    data_url='http://donnees.ville.quebec.qc.ca/Handler.ashx?id=43&f=SHP',
    encoding='iso-8859-1',
    metadata={'ocd_division': u'ocd-division/country:ca/csd:2423027/borough:2'},
    ogr2ogr='''-where "DATE_FIN='2017/11/05' AND ARROND='Les Rivières'"''',
)
