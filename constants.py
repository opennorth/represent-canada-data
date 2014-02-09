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

# Authorities that are responsible for multiple shapefiles.
authorities = [
  u'Elections Prince Edward Island',
  u'Regional Municipality of Peel',
  u'Regional Municipality of Waterloo',
  u'Ville de Montréal',
]

municipal_subdivisions = {
  # NL
  '1001542': 'N',
  '1005018': 'N',
  # ON
  '3501012': 'N',
  '3518013': 'N',
  '3519046': 'N',
  '3526043': 'N',
  '3531011': 'N',
  '3532042': 'N',
  '3534021': 'N',
  '3538030': 'N',
  '3548044': 'N',
  # MB
  '4602044': 'N',
  '4609029': 'N',
  '4622026': 'N',
  # SK
  '4701024': 'N',
  '4707039': 'N',
  '4708004': 'N',
  '4709012': 'N',
  '4716029': 'N',
  # YT
  '6001009': 'N',
  # NT
  '6106023': 'N',
}

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
  'URL',
  'Scraper?',
  'Shapefile?',
] + request_headers + receipt_headers
