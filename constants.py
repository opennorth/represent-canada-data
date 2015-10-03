# coding: utf-8
from __future__ import unicode_literals

import re

open_data_licenses = [
    'http://cms.burlington.ca/AssetFactory.aspx?did=18762',
    'http://data.alberta.ca/licence',
    'http://open.canada.ca/en/open-government-licence-canada',
    'http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/',
    'http://donnees.ville.sherbrooke.qc.ca/licence.html',
    'http://geonb.snb.ca/downloads/documents/geonb_license_e.pdf',
    'http://www.greatersudbury.ca/inside-city-hall/open-data/licence/',
    'http://oakville.ca/data/open_data_licence.html',
    'http://opendata.peelregion.ca/terms-of-use.aspx',
    'http://openguelph.wpengine.com/open-data-guelph/city-of-guelph-open-government-licence/',
    'http://ottawa.ca/en/mobile-apps-and-open-data/open-data-terms-use',
    'http://www.citywindsor.ca/opendata/Documents/OpenDataTermsofUse.pdf',
    'http://www.countygp.ab.ca/EN/main/community/maps-gis/open-data/open-data-licence.html',
    'http://www.edmonton.ca/city_government/documents/Web-version2.1-OpenDataAgreement.pdf',
    'http://www.electionspei.ca/apilicense',
    'http://www.hamilton.ca/city-initiatives/strategies-actions/open-accessible-data',
    'http://www.fredericton.ca/en/citygovernment/TermsOfUse.asp',
    'http://www.halifax.ca/opendata/OD_TermsOfUse.php',
    'http://www.london.ca/city-hall/open-data/Pages/OpenData-TermsofUse.aspx',
    'http://www.milton.ca/en/resourcesGeneral/Open_Data/Milton_Open_Data_Terms_V1.pdf',
    'http://www.regina.ca/residents/open-government/open-government-licence/',
    'http://www.regionofwaterloo.ca/en/regionalGovernment/OpenDataLicence.asp',
    'http://www.welland.ca/open/OpendataTermUse.asp',
    'http://www1.toronto.ca/wps/portal/contentonly?vgnextoid=4a37e03bb8d1e310VgnVCM10000071d60f89RCRD&vgnextfmt=default',
    'http://www5.mississauga.ca/research_catalogue/CityofMississauga_TermsofUse.pdf',
    'https://creativecommons.org/licenses/by/4.0/legalcode',
    'https://data.calgary.ca/OpenData/Pages/TermsofUse.aspx',
    'https://data.strathcona.ca/licence',
    'https://data.winnipeg.ca/open-data-licence',
    'https://www.arcgis.com/sharing/rest/content/items/2ffb1ce148804fe4ade2414e6ef10d21/data',
]

some_rights_reserved_licenses = [
    'http://mli2.gov.mb.ca/app/register/app/index.php',  # no commercial redistribution
    'http://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php',  # per CIPPIC
    'https://www.geosask.ca/Portal/jsp/terms_popup.jsp',  # per CIPPIC
]

all_rights_reserved_licenses = [
    'http://opendata-saskatoon.cloudapp.net/TermsOfUse/TermsOfUse',  # open data license pending
    'http://www.elections.on.ca/en/voting-in-ontario/electoral-districts/electoral-districts--maps--shapefiles-and-street-index-guide/limited-use-data-product-licence-agreement.html',  # per CIPPIC
]

all_rights_reserved_terms_re = re.compile('\ADistributed with permission from .+?.  Please direct licensing inquiries and requests to:\n\n(.+)', re.MULTILINE | re.DOTALL)

terms = {
    # @see https://www.cippic.ca/sites/default/files/CIPPIC%20-%20How%20to%20Redistribute%20Open%20Data.pdf
    'http://ottawa.ca/en/mobile-apps-and-open-data/open-data-terms-use': 'I. Terms of Use. This work is provided under the terms of “City of Ottawa – Terms of Use” (http://ottawa.ca/en/mobile-apps-and-open-data/open-data-terms-use).  Any use of the work other than as authorized under these terms is strictly prohibited.',
    'http://www.citywindsor.ca/opendata/Documents/OpenDataTermsofUse.pdf': 'I. Terms of Use. This work is provided under the terms of “City of Windsor – Terms of Use” (http://www.citywindsor.ca/opendata/Documents/OpenDataTermsofUse.pdf).  Any use of the work other than as authorized under these terms is strictly prohibited.',
    'http://www.edmonton.ca/city_government/documents/Web-version2.1-OpenDataAgreement.pdf': 'I. Terms of Use. This work is provided under the terms of City of Edmonton Open Data Terms of Use (http://www.edmonton.ca/city_government/documents/Web-version2.1-OpenDataAgreement.pdf).  Any use of the work other than as authorized under these terms is strictly prohibited.',
    'http://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php': """Attribution: This data is provided by the Directeur général des élections du Québec (http://www.electionsquebec.qc.ca), reproduced according to the terms of the "Conditions d'utilisation de notre site Web" (http://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php). Copyright in the work belongs to the Government of Quebec.""",
    'http://www5.mississauga.ca/research_catalogue/CityofMississauga_TermsofUse.pdf': 'I. Terms of Use. This work is provided under the terms of “City of Mississauga – Terms of Use” (http://www.mississauga.ca/file/COM/CityOfMississaugaTermsOfUse.pdf).  Any use of the work other than as authorized under these terms is strictly prohibited.',
    'https://data.calgary.ca/OpenData/Pages/TermsofUse.aspx': 'I. Terms of Use. This data is provided by the City of Calgary and is made available under the Open Data Catalogue Terms of Use (https://cityonline.calgary.ca/Pages/PdcTermsOfUse.aspx).',
    # @see Gowlings advice.
    'http://cms.burlington.ca/AssetFactory.aspx?did=18762': 'I. Terms of Use. This work is provided under the terms of “Terms of Use for Open Data Burlington” (http://cms.burlington.ca/AssetFactory.aspx?did=18762).  Any use of the work other than as authorized under these terms is strictly prohibited.',
    'http://geonb.snb.ca/downloads/documents/geonb_license_e.pdf': 'I. Attribution. This data is provided by GeoNB – www.snb.ca/geonb. This attribution does not constitute an endorsement by Service New Brunswick or its GeoNB partners.\n\nII. Warranty, Liability, Indemnity of Service New Brunswick and its GeoNB partners.\n1. Except as expressly provided in the “GeoNB License Agreement” (http://geonb.snb.ca/downloads/documents/geonb_license_e.pdf), this data is provided “As is” without any representations, warranties, guarantees or conditions, of any kind, whether expressed or implied, statutory or otherwise.\n2. Service New Brunswick (SNB) makes no representation or warranty of any kind with respect to the accuracy, usefulness, novelty, validity, scope, completeness or currency of the data and expressly disclaims any implied warranty of merchantability or fitness for a particular purpose of the data. SNB does not ensure or warrant compatibility with past, current or future versions of your browser to access the data.\n3. The Licensee shall have no recourse against SNB, nor its GeoNB partners, whether by way of any suit or action, for any loss, liability, damage or cost that the Licensee may suffer or incur at any time, by reason of the Licensee’s possession or use of the data.\n4. The Licensee shall indemnify SNB, and its GeoNB partners, and their officers, employees, agents and contractors from all claims alleging loss, costs, expenses, damages or injuries (including injuries resulting in death) arising out of the Licensee’s possession or use of the data.\n5. The Licensee shall license all individuals (or companies) who obtain data or derivative products from the Licensee the right to use the data or derivative products by way of a license agreement, and that agreement shall impose upon these individuals (or companies) the same terms and conditions as those contained in Section II of this agreement.\n6. The Licensee’s liability to indemnify SNB under this agreement shall not affect or prejudice SNB from exercising any other rights under law.\n7. SNB assumes no obligation to update the data. The data may be changed without notice to the Licensee.',
    'http://www.fredericton.ca/en/citygovernment/TermsOfUse.asp': 'I. Terms of Use. This work is provided under the terms of "City of Fredericton - Terms of Use" (http://fredericton.icreate2.esolutionsgroup.ca/cityfredericton/en/citygovernment/TermsOfUse.asp).  Any use of the work other than as authorized under these terms is strictly prohibited.',
    'http://www.london.ca/city-hall/open-data/Pages/OpenData-TermsofUse.aspx': 'I. Terms of Use. This work is provided under the terms of “Open Data London – Terms of Use” (http://www.london.ca/city-hall/open-data/Pages/OpenData-TermsofUse.aspx).  Any use of the work other than as authorized under these terms is strictly prohibited.',
    # Open Government Licence.
    'http://data.alberta.ca/licence':
    'I. Terms of Use. Contains information licensed under the Open Government Licence – Alberta (http://data.alberta.ca/licence).',
    'http://open.canada.ca/en/open-government-licence-canada':
    'I. Terms of Use. Contains information licensed under the Open Government Licence – Canada (http://open.canada.ca/en/open-government-licence-canada).',
    'http://oakville.ca/data/open_data_licence.html':
    'I. Terms of Use. Contains information licensed under the Open Government Licence — Town of Oakville (http://oakville.ca/data/open_data_licence.html).',
    'http://openguelph.wpengine.com/open-data-guelph/city-of-guelph-open-government-licence/':
    'I. Terms of Use. Contains information provided by the City of Guelph under an open government license (http://openguelph.wpengine.com/open-data-guelph/city-of-guelph-open-government-licence/).',
    'http://www.countygp.ab.ca/EN/main/community/maps-gis/open-data/open-data-licence.html':
    'I. Terms of Use. Contains information licensed under the Open Government Licence – County of Grande Prairie (http://www.countygp.ab.ca/EN/main/community/maps-gis/open-data/open-data-licence.html).',
    'http://www.halifax.ca/opendata/OD_TermsOfUse.php':
    'I. Terms of Use. Contains information licenced under the Open Government Licence - Halifax (http://www.halifax.ca/opendata/OD_TermsOfUse.php).',
    'http://www.nanaimo.ca/EN/main/departments/106/DataCatalogue/Licence.html':
    'I. Terms of Use. Contains information licensed under the Open Government Licence - Nanaimo (http://www.nanaimo.ca/EN/main/departments/106/DataCatalogue/Licence.html).',
    'http://www.regina.ca/residents/open-government/open-government-licence/':
    'I. Terms of Use. Contains information licensed under the Open Government Licence – City of Regina (http://www.regina.ca/residents/open-government/open-government-licence/).',
    'https://data.strathcona.ca/licence':
    'I. Terms of Use. Contains information licensed under the Open Government Licence – Strathcona County (https://data.strathcona.ca/licence).',
    'https://data.winnipeg.ca/open-data-licence':
    'I. Terms of Use. Contains information licensed under the Open Government Licence – Winnipeg (https://data.winnipeg.ca/open-data-licence).',
    'http://www1.toronto.ca/wps/portal/contentonly?vgnextoid=4a37e03bb8d1e310VgnVCM10000071d60f89RCRD&vgnextfmt=default':
    'I. Terms of Use. Contains information licensed under the Open Government Licence – Toronto (http://www1.toronto.ca/wps/portal/contentonly?vgnextoid=4a37e03bb8d1e310VgnVCM10000071d60f89RCRD&vgnextfmt=default).',
    # Text provided by license.
    'http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/': "I. Termes d'utilisation. Contient des données reproduites, modifiées, traduites ou distribuées « telles quelles » avec la permission de la Ville de Montréal (http://donnees.ville.montreal.qc.ca/licence/licence-texte-complet/).",
    'http://donnees.ville.sherbrooke.qc.ca/licence.html': "I. Termes d'utilisation. Contient des données reproduites et distribuées « telles quelles » avec la permission de la Ville de Sherbrooke (http://donnees.ville.sherbrooke.qc.ca/licence.html).",
    'http://opendata.peelregion.ca/terms-of-use.aspx': "I. Terms of Use. Contains public sector Information made available under The Regional Municipality of Peel's Open Data Licence - Version 1.0 (http://opendata.peelregion.ca/terms-of-use.aspx).",
    'http://www.electionspei.ca/apilicense': 'I. Terms of Use. This information is provided by Elections PEI under the Elections PEI Data License (http://www.electionspei.ca/apilicense).',
    'http://www.greatersudbury.ca/inside-city-hall/open-data/licence/': 'I. Terms of Use. Contains information licensed under the Open Data Licence – City of Greater Sudbury (http://www.greatersudbury.ca/inside-city-hall/open-data/licence/).',
    'http://www.hamilton.ca/city-initiatives/strategies-actions/open-accessible-data': "I. Terms of Use. Contains public sector Data made available under the City of Hamilton’s Open Data Licence (http://www.hamilton.ca/city-initiatives/strategies-actions/open-accessible-data).",
    'http://www.milton.ca/en/resourcesGeneral/Open_Data/Milton_Open_Data_Terms_V1.pdf': "I. Terms of Use. Contains public sector Datasets made available under the Town of Milton's Open Data License v.1 (http://www.milton.ca/en/resourcesGeneral/Open_Data/Milton_Open_Data_Terms_V1.pdf).",
    'http://www.regionofwaterloo.ca/en/regionalGovernment/OpenDataLicence.asp': 'I. Terms of Use. Contains information provided by the Regional Municipality of Waterloo under licence (http://www.regionofwaterloo.ca/en/regionalGovernment/OpenDataLicence.asp).',
    'http://www.welland.ca/open/OpendataTermUse.asp': 'I. Terms of Use. Contains public sector datasets made available under The Corporation of the City of Welland Open Data Licence v1.0 (http://www.welland.ca/open/OpendataTermUse.asp).',
    'https://www.arcgis.com/sharing/rest/content/items/2ffb1ce148804fe4ade2414e6ef10d21/data': 'I. Terms of Use. Contains information licensed under the Open Government Licence – The Corporation of the Municipality of Chatham-Kent (https://www.arcgis.com/sharing/rest/content/items/2ffb1ce148804fe4ade2414e6ef10d21/data).',
    # Kent Mewhort email (2012-02-10).
    'http://mli2.gov.mb.ca/app/register/app/index.php': '© 2001 Her Majesty the Queen in Right of Manitoba, as represented by the Minister of Conservation. All rights reserved. Distributed under the terms of the Manitoba Land Initiative Terms and Conditions of Use (http://mli2.gov.mb.ca//app/register/app/index.php).',
}

terms_re = {
    # Creative Commons.
    'https://creativecommons.org/licenses/by/4.0/legalcode': re.compile("\AI\. Terms of Use\. This material is licensed under a Creative Commons Attribution 4\.0 International License\. To view a copy of this license, visit http://creativecommons\.org/licenses/by/4\.0/legalcode\. It is attributed to .+, and the original version can be found at .+\.\Z"),
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
    'base_file',
])

valid_metadata_keys = set([
    'geographic_code',
    'ocd_division',
])

# Authorities that are responsible for multiple shapefiles.
authorities = [
    'Elections Prince Edward Island',
    'Regional Municipality of Peel',
    'Regional Municipality of Waterloo',
    'Ville de Montréal',
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
    'Shapefile?',
] + request_headers + receipt_headers
