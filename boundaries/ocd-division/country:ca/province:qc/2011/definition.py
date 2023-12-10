from datetime import date

import boundaries

boundaries.register('Quebec electoral districts (2011)',
    singular='Quebec electoral district',
    domain='Quebec',
    last_updated=date(2012, 2, 24),  # historical
    name_func=boundaries.clean_attr('NM_CEP'),
    id_func=boundaries.attr('CO_CEP'),
    authority='Directeur général des élections du Québec',
    source_url='https://www.electionsquebec.qc.ca/francais/provincial/carte-electorale/geometrie-des-circonscriptions-provinciales-du-quebec.php',
    licence_url='https://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php',
    data_url='https://www.electionsquebec.qc.ca/documents/zip/circonscriptions-electorales-2011-shapefile-v2.zip',
    encoding='windows-1252',
    extra={'division_id': 'ocd-division/country:ca/province:qc'},
)
