import re
from datetime import date

import boundaries

# The shapefile contains features for towns without subdivisions:
# * Amherst
# * Annapolis Royal
# * Antigonish
# * Bridgewater
# * Clark's Harbour
# * Digby
# * Kentville
# * Lockeport
# * Lunenburg
# * Mahone Bay
# * Middleton
# * Mulgrave
# * Oxford
# * Parrsboro
# * Part Hawkesbury
# * Pictou
# * Shelburne
# * Stewiacke
# * Trenton
# * Westville
# * Windsor
# * Wolfville
# * Yarmouth
sets = {
    'cd:1205': ['Annapolis', 'AP', 'district'],
    'cd:1207': ['Kings', 'KI', 'district'],
    'cd:1210': ['Colchester', 'CO', 'district'],
    'cd:1211': ['Cumberland', 'CU', 'district'],
    'cd:1212': ['Pictou', 'PI', 'district'],
    'cd:1214': ['Antigonish', 'AT', 'district'],
    'cd:1215': ['Inverness', 'IN', 'district'],
    'cd:1216': ['Richmond, NS', 'RI', 'district'],
    'cd:1218': ['Victoria', 'VI', 'district'],
    'csd:1201001': ['Barrington', 'BA', 'district'],
    'csd:1201006': ['Shelburne', 'SH', 'district'],
    'csd:1202001': ['Argyle', 'AY', 'district'],
    'csd:1202004': ['Yarmouth', 'YA', 'district'],
    'csd:1203001': ['Clare', 'CL', 'district'],
    'csd:1203004': ['Digby', 'DI', 'district'],
    'csd:1204010': ['Queens', 'QU', 'district'],
    'csd:1206001': ['Lunenburg', 'LU', 'district'],
    'csd:1206009': ['Chester', 'CT', 'district'],
    'csd:1208001': ['West Hants', 'WH', 'district'],
    'csd:1208008': ['East Hants', 'EH', 'district'],
    # Halifax has ward names in its data catalog.
    # 'csd:1209034': ['Halifax', 'HX', 'district'],
    'csd:1210006': ['Truro', 'TU', 'ward'],
    'csd:1212014': ['New Glasgow', 'NG', 'ward'],
    'csd:1212009': ['Stellarton', 'SL', 'ward'],
    'csd:1213001': ["St. Mary's", 'SM', 'district'],
    'csd:1213004': ['Guysborough', 'GU', 'district'],
    'csd:1217030': ['Cape Breton', 'CB', 'district'],
}

for fragment, (name, machine_name, type) in sets.items():
    boundaries.register('%s %ss' % (name, type),
        domain=name if ', NS' in name else '%s, NS' % name,
        last_updated=date(2017, 2, 6),
        name_func=lambda f: '%s %s' % (type.capitalize(), re.sub(r'^\D+0?', '', f.get('poll_dist'))),
        id_func=lambda f: re.sub(r'^\D+0?', '', f.get('poll_dist')),
        authority='Her Majesty the Queen in Right of Nova Scotia',
        source_url='https://data.novascotia.ca/Municipalities/Municipal-Polling-Districts/gcep-xeci',
        licence_url='https://novascotia.ca/opendata/licence.asp',
        data_url='https://data.novascotia.ca/api/geospatial/gcep-xeci?method=export&format=Shapefile',
        encoding='iso-8859-1',
        extra={'division_id': 'ocd-division/country:ca/%s' % fragment},
        is_valid_func=lambda f, machine_name=machine_name: f.get('mu_code') == machine_name and f.get('poll_dist') != 'Unresolved' and not f.get('poll_dist').endswith('AL'),
        notes='Compare the subdivisions in boundaries/ca_ns_districts/definition.py to:\nogrinfo -al -geom=NO boundaries/ca_ns_districts | grep " mun" | sort | uniq | cut -d= -f 2\nLoad the shapefile manually:\nfab alpheus update_boundaries:args="-r --merge union -d data/shapefiles/public/boundaries/ca_ns_districts"',
    )
