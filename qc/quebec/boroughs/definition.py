# coding: utf-8
from __future__ import unicode_literals

from datetime import date

import boundaries

# @see http://www.toponymie.gouv.qc.ca/ct/toponymie-municipale/municipalites-arrondissements/arrondissement.aspx
# @see http://www.mamrot.gouv.qc.ca/repertoire-des-municipalites/fiche/arrondissement/?tx_mamrotrepertoire_pi1[order]=asc_nom_mun
boundaries.register('Québec boroughs',
    domain='Québec, QC',
    last_updated=date(2015, 10, 3),
    name_func=lambda f: f.get('NOM').replace('?', '—'),  # m-dash
    id_func=boundaries.attr('CODE'),
    authority='Ville de Québec',
    source_url='http://donnees.ville.quebec.qc.ca/donne_details.aspx?jdid=2',
    licence_url='https://creativecommons.org/licenses/by/4.0/legalcode',
    data_url='http://donnees.ville.quebec.qc.ca/Handler.ashx?id=2&f=SHP',
    encoding='iso-8859-1',
    metadata={'geographic_code': '2423027'},
)
