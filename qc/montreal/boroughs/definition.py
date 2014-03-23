# coding: utf-8
from datetime import date

import boundaries


def namer(f):
    import boundaries
    n = boundaries.attr('ARROND')(f)
    return {
        u'Cote-des-Neiges--Notre-Dame-de-Grace': u'Côte-des-Neiges—Notre-Dame-de-Grâce',
        u"L'Ile-Bizard--Sainte-Genevieve": u"L'Île-Bizard—Sainte-Geneviève",
        u'Mercier-Hochelaga-Maisonneuve': u'Mercier—Hochelaga-Maisonneuve',
        u'Montreal-Nord': u'Montréal-Nord',
        u'Pierrefonds--Roxboro': u'Pierrefonds-Roxboro',
        u'Plateau-Mont-Royal': u'Le Plateau-Mont-Royal',
        u'Pointe-aux-Trembles-Rivieres-des-Prairies': u'Rivière-des-Prairies—Pointe-aux-Trembles',
        u'Rosemont--La-Petite-Patrie': u'Rosemont—La Petite-Patrie',
        u'St-Leonard': u'Saint-Léonard',
        u'Sud-Ouest': u'Le Sud-Ouest',
        u'Verdun--Ile-des-Soeurs': u'Verdun',
        u'Villeray-Saint-Michel-Parc-Extension': u'Villeray—Saint-Michel—Parc-Extension',
    }.get(n, n)

# @see http://www.toponymie.gouv.qc.ca/ct/toponymie-municipale/municipalites-arrondissements/arrondissement.aspx
# @see http://www.mamrot.gouv.qc.ca/repertoire-des-municipalites/fiche/arrondissement/?tx_mamrotrepertoire_pi1[order]=asc_nom_mun
boundaries.register(u'Montréal boroughs',
    domain=u'Montréal, QC',
    last_updated=date(2014, 2, 1),
    name_func=namer,
    authority=u'Ville de Montréal',
    source_url='http://donnees.ville.montreal.qc.ca/dataset/polygones-arrondissements',
    licence_url='http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    data_url='http://donnees.ville.montreal.qc.ca/storage/f/2014-02-01T01%3A40%3A15.962Z/arrondissements-shapefile.zip',
    notes='The Ahuntsic-Cartierville borough is split into two features. We merge them using Quantum GIS.',
    encoding='iso-8859-1',
    metadata={'geographic_code': '2466023'},
)
