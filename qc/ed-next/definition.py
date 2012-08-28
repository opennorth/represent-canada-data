#coding: utf-8

from datetime import date

import boundaries

boundaries.register(u'Québec electoral districts (next election)',
    singular=u'Québec electoral district (next election)',
    domain=u'Québec',
    last_updated=date(2012, 2, 13),
    name_func=boundaries.clean_attr('NM_CEP'),
    id_func=boundaries.attr('CO_CEP'),
    authority=u'Directeur général des élections du Québec',
    source_url='http://electionsquebec.qc.ca/francais/provincial/carte-electorale/geometrie-des-circonscriptions-provinciales-du-quebec-2011.php',
    licence_url='http://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php',
    data_url='http://electionsquebec.qc.ca/documents/zip/circonscriptions-electorales-2011-shapefile.zip',
    encoding='iso-8859-1',
)
