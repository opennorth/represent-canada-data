# coding: utf-8
from datetime import date

import boundaries

boundaries.register('Quebec electoral districts (2017)',
    singular='Quebec electoral district',
    domain='Quebec',
    last_updated=date(2017, 10, 4),
    name_func=boundaries.clean_attr('NM_CEP'),
    id_func=boundaries.attr('CO_CEP'),
    authority='Directeur général des élections du Québec',
    source_url='https://www.electionsquebec.qc.ca/francais/provincial/carte-electorale/geometrie-des-circonscriptions-provinciales-du-quebec.php',
    licence_url='https://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php',
    data_url='https://www.electionsquebec.qc.ca/documents/zip/circonscriptions_electorales_2017_shapefile.zip',
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca/province:qc'},
)
