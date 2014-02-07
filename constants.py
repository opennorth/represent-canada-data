# coding: utf8

import re

open_data_licenses = [
  'http://data.gc.ca/eng/open-government-licence-canada',
  'http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
  'http://donnees.ville.quebec.qc.ca/licence.aspx',
  'http://opendata.peelregion.ca/terms-of-use.aspx',
  'http://ottawa.ca/en/mobile-apps-and-open-data/open-data-terms-use',
  'http://www.citywindsor.ca/opendata/Documents/OpenDataTermsofUse.pdf',
  'http://www.countygp.ab.ca/EN/main/community/maps-gis/open-data/open-data-licence.html',
  'http://www.edmonton.ca/city_government/initiatives_innovation/open-data-terms-of-use.aspx',
  'http://www.electionspei.ca/apilicense',
  'http://www.hamilton.ca/NR/rdonlyres/C58984A4-FE11-40B9-A231-8572EB922AAA/0/OpenDataTermsAndConditions_Final.htm',
  'http://www.fredericton.ca/en/citygovernment/TermsOfUse.asp',
  'http://www.london.ca/city-hall/open-data/Pages/OpenData-TermsofUse.aspx',
  'http://www.milton.ca/en/resourcesGeneral/Open_Data/Milton_Open_Data_Terms_V1.pdf',
  'http://www.regina.ca/residents/open-government/data/terms/',
  'http://www.regionofwaterloo.ca/en/regionalGovernment/OpenDataLicence.asp',
  'http://www.strathcona.ca/local-government/strathcona-county-elections/election-2013-open-data/#licence',
  'http://www1.toronto.ca/wps/portal/contentonly?vgnextoid=4a37e03bb8d1e310VgnVCM10000071d60f89RCRD&vgnextfmt=default',
  'http://www5.mississauga.ca/research_catalogue/CityofMississauga_TermsofUse.pdf',
  'https://cityonline.calgary.ca/Pages/PdcTermsOfUse.aspx',
]

some_rights_reserved_licenses = [
  'http://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php',  # per CIPPIC
  'https://mli2.gov.mb.ca/app/register/app/index.php',  # no commercial redistribution
  'https://www.geosask.ca/Portal/jsp/terms_popup.jsp',  # per CIPPIC
]

all_rights_reserved_licenses = [
  'http://opendata-saskatoon.cloudapp.net/TermsOfUse/TermsOfUse',  # open data license pending
  'http://www.altalis.com/agreement.html',  # per CIPPIC
  'http://www.elections.on.ca/en-CA/Tools/ElectoralDistricts/LimitedUseDataProductLicenceAgreement.htm',  # per CIPPIC
]

all_rights_reserved_terms_re = re.compile('\ADistributed with permission from .+?.  Please direct licensing inquiries and requests to:\n\n(.+)', re.MULTILINE | re.DOTALL)

terms = {
  # @see https://www.cippic.ca/sites/default/files/CIPPIC%20-%20How%20to%20Redistribute%20Open%20Data.pdf
  'http://ottawa.ca/en/mobile-apps-and-open-data/open-data-terms-use': 'I. Terms of Use. This work is provided under the terms of “City of Ottawa – Terms of Use” (http://ottawa.ca/en/mobile-apps-and-open-data/open-data-terms-use).  Any use of the work other than as authorized under these terms is strictly prohibited.',
  'http://www.citywindsor.ca/opendata/Documents/OpenDataTermsofUse.pdf': 'I. Terms of Use. This work is provided under the terms of “City of Windsor – Terms of Use” (http://www.citywindsor.ca/opendata/Documents/OpenDataTermsofUse.pdf).  Any use of the work other than as authorized under these terms is strictly prohibited.',
  'http://www.edmonton.ca/city_government/initiatives_innovation/open-data-terms-of-use.aspx': 'I. Terms of Use. This work is provided under the terms of City of Edmonton Open Data Terms of Use (http://www.edmonton.ca/city_government/initiatives_innovation/open-data-terms-of-use.aspx).  Any use of the work other than as authorized under these terms is strictly prohibited.',
  'http://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php': """Attribution: This data is provided by the Directeur général des élections du Québec (http://www.electionsquebec.qc.ca), reproduced according to the terms of the "Conditions d'utilisation de notre site Web" (http://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php). Copyright in the work belongs to the Government of Quebec.""",
  'http://www.london.ca/d.aspx?s=/Open_Data/Open_Data_Terms_Use.htm': 'I. Terms of Use. This work is provided under the terms of “Open Data London – Terms of Use” (http://www.london.ca/d.aspx?s=/Open_Data/Open_Data_Terms_Use.htm).  Any use of the work other than as authorized under these terms is strictly prohibited.',
  'http://www5.mississauga.ca/research_catalogue/CityofMississauga_TermsofUse.pdf': 'I. Terms of Use. This work is provided under the terms of “City of Mississauga – Terms of Use” (http://www.mississauga.ca/file/COM/CityOfMississaugaTermsOfUse.pdf).  Any use of the work other than as authorized under these terms is strictly prohibited.',
  'https://cityonline.calgary.ca/Pages/PdcTermsOfUse.aspx': 'I. Terms of Use. This data is provided by the City of Calgary and is made available under the Open Data Catalogue Terms of Use (https://cityonline.calgary.ca/Pages/PdcTermsOfUse.aspx).',
  # Open Government Licence.
  'http://data.gc.ca/eng/open-government-licence-canada':
    'I. Terms of Use. Contains information licensed under the Open Government Licence – Canada (http://data.gc.ca/eng/open-government-licence-canada).',
  'http://www.countygp.ab.ca/EN/main/community/maps-gis/open-data/open-data-licence.html':
    'I. Terms of Use. Contains information licensed under the Open Government Licence – County of Grande Prairie (http://www.countygp.ab.ca/EN/main/community/maps-gis/open-data/open-data-licence.html).',
  'http://www.nanaimo.ca/EN/main/departments/106/DataCatalogue/Licence.html':
    'I. Terms of Use. Contains information licensed under the Open Government Licence - Nanaimo (http://www.nanaimo.ca/EN/main/departments/106/DataCatalogue/Licence.html).',
  'http://www.strathcona.ca/local-government/strathcona-county-elections/election-2013-open-data/#licence':
    'I. Terms of Use. Contains information licensed under the Open Government Licence – Strathcona County (http://www.strathcona.ca/local-government/strathcona-county-elections/election-2013-open-data/#licence).',
  'http://www1.toronto.ca/wps/portal/contentonly?vgnextoid=4a37e03bb8d1e310VgnVCM10000071d60f89RCRD&vgnextfmt=default':
    'I. Terms of Use. Contains information licensed under the Open Government Licence – Toronto (http://www1.toronto.ca/wps/portal/contentonly?vgnextoid=4a37e03bb8d1e310VgnVCM10000071d60f89RCRD&vgnextfmt=default).',
  # Text provided by license.
  'http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/': "I. Termes d'utilisation. Contient des données reproduites, modifiées, traduites ou distribuées « telles quelles » avec la permission de la Ville de Montréal (http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/).",
  'http://donnees.ville.quebec.qc.ca/licence.aspx': "I. Conditions d'utilisation. Contient des données reproduites et distribuées « telles quelles » avec la permission de la Ville de Québec (http://donnees.ville.quebec.qc.ca/licence.aspx).",
  'http://opendata.peelregion.ca/terms-of-use.aspx': "I. Terms of Use. Contains public sector Information made available under The Regional Municipality of Peel's Open Data Licence - Version 1.0 (http://opendata.peelregion.ca/terms-of-use.aspx).",
  'http://www.electionspei.ca/apilicense': 'I. Terms of Use. This information is provided by Elections PEI under the Elections PEI Data License (http://www.electionspei.ca/apilicense).',
  'http://www.hamilton.ca/NR/rdonlyres/C58984A4-FE11-40B9-A231-8572EB922AAA/0/OpenDataTermsAndConditions_Final.htm': "I. Terms of Use. Contains public sector Data made available under the City of Hamilton’s Open Data Licence (http://www.hamilton.ca/NR/rdonlyres/C58984A4-FE11-40B9-A231-8572EB922AAA/0/OpenDataTermsAndConditions_Final.htm).",
  'http://www.milton.ca/en/resourcesGeneral/Open_Data/Milton_Open_Data_Terms_V1.pdf': "I. Terms of Use. Contains public sector Datasets made available under the Town of Milton's Open Data License v.1 (http://www.milton.ca/en/resourcesGeneral/Open_Data/Milton_Open_Data_Terms_V1.pdf).",
  'http://www.regionofwaterloo.ca/en/regionalGovernment/OpenDataLicence.asp': 'I. Terms of Use. Contains information provided by the Regional Municipality of Waterloo under licence (http://www.regionofwaterloo.ca/en/regionalGovernment/OpenDataLicence.asp).',
  # Kent Mewhort email (2012-02-10).
  'https://mli2.gov.mb.ca/app/register/app/index.php': '© 2001 Her Majesty the Queen in Right of Manitoba, as represented by the Minister of Conservation. All rights reserved. Distributed under the terms of the Manitoba Land Initiative Terms and Conditions of Use (https://mli2.gov.mb.ca//app/register/app/index.php).',
}

terms_re = {
  # @see https://www.cippic.ca/sites/default/files/CIPPIC%20-%20How%20to%20Redistribute%20Open%20Data.pdf
  'https://www.geosask.ca/Portal/jsp/terms_popup.jsp': re.compile("\AAttribution: (Source|Adapted from): Her Majesty In Right Of Saskatchewan or Information Services Corporation of Saskatchewan, [^.]+\. The incorporation of data sourced from Her Majesty In Right Of Saskatchewan and/or Information Services Corporation of Saskatchewan, within this product shall not be construed as constituting an endorsement by Her Majesty In Right Of Saskatchewan or Information Services Corporation of Saskatchewan of such product\.\Z"),
}

valid_keys = set([
  # Added by boundaries.register.
  'file',
  # Used by represent-boundaries.
  'name',
  'singular',
  'domain',
  'last_updated',
  'slug_func',
  'name_func',
  'id_func',
  'is_valid_func',
  'authority',
  'source_url',
  'licence_url',
  'data_url',
  'metadata',
  'notes',
  'encoding',
  # Used by this script. Not validated.
  'ogr2ogr',
  'prj',
])

valid_metadata_keys = set([
  'geographic_code',
  'ocd_division',
])

authorities = [
  u'Elections Prince Edward Island',
  u'Regional Municipality of Peel',
  u'Regional Municipality of Waterloo',
  u'Ville de Montréal',
]

# @todo Make a list of SGC codes with wards
# http://www.electionsquebec.qc.ca/francais/municipal/carte-electorale/liste-des-municipalites-divisees-en-districts-electoraux.php?index=1
# @todo Add census subdivision type to be able to flag municipalities with potential wards?
# http://www.municipalaffairs.gov.ab.ca/am_types_of_municipalities_in_alberta.cfm
# http://www.gov.ns.ca/snsmr/election/FinalCouncillistElected2008.pdf
no_municipal_subdivisions = [
  # NL
  '1001542',
  '1005018',
  # QC
  '2426030',
  '2461035',
  '2466047',
  '2466062',
  '2466072',
  '2466092',
  '2466112',
  '2473020',
  '2479088',
  '2488055',
  '2491025',
  '2491042',
  '2492022',
  # ON
  '3501012',
  '3518013',
  '3519046',
  '3526043',
  '3531011',
  '3532042',
  '3534021',
  '3538030',
  '3548044',
  # MB
  '4602044',
  '4609029',
  '4622026',
  # SK
  '4701024',
  '4707039',
  '4708004',
  '4709012',
  '4716029',
  # AB
  '4801006',
  '4802012',
  '4802034',
  '4805018',
  '4806006',
  '4806012',
  '4806019',
  '4806021',
  '4808011',
  '4808012',
  '4808031',
  '4810011',
  '4811002',
  '4811016',
  '4811048',
  '4811049',
  '4811056',
  '4811062',
  '4812002',
  '4815023',
  '4819012',
  # YT
  '6001009',
  # NT
  '6106023',
]

request_headers = [
  'Contact',
  'Highrise URL',
  'Request notes',
  'Received via',
]

receipt_headers = [
  'Last boundary',
  'Next boundary',
  'Permission to distribute',
  'Type of license',
  'License URL',
  'Denial notes',
]

headers = [
  'OCD',
  'Geographic code',
  'Geographic name',
  'Province or territory',
  'Population',
  'Scraper?',
  'Shapefile?',
] + request_headers + receipt_headers
