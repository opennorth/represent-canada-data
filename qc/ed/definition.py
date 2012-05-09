#coding: utf-8

from datetime import date

import boundaries

boundaries.register('Quebec electoral districts',
    domain='Québec',
    last_updated=date(2009, 5, 14),
    name_func=boundaries.clean_attr('NM_CEP'),
    id_func=boundaries.attr('CO_CEP'),
    authority='Directeur général des élections du Québec',
    source_url='http://www.electionsquebec.qc.ca/francais/provincial/carte-electorale/geometrie-des-circonscriptions-provinciales-du-quebec.php',
    licence_url='http://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php',
    data_url='http://www.electionsquebec.qc.ca/documents/zip/shapefile-circonscriptions-electorales-2001-elections-generales-2008.zip',
    encoding='iso-8859-1',
)
