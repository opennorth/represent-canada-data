# coding: utf-8
from __future__ import unicode_literals

from datetime import date

from unidecode import unidecode

import boundaries

sets = {
    # QGIS errors when merging or dissolving features.
    # 23027: "Québec",
    # 25213: "Lévis",
    43027: "Sherbrooke",
    58227: "Longueuil",
    66023: "Montréal",
    94068: "Saguenay",
}


def namer(f):
    import boundaries
    if f.get('CO_MUNCP') == 43027:
        return {
            'Le Mont-Bellevue': 'Mont-Bellevue',
            'Rock Rorest--Saint-lie--Deauville': 'Rock Forest—Saint-Élie—Deauville',
        }.get(f.get('NM_ARON'), boundaries.clean_attr('NM_ARON')(f))
    elif f.get('CO_MUNCP') == 66023:
        return {
            'Pierrefond-Roxboro': 'Pierrefonds-Roxboro',
        }.get(f.get('NM_ARON'), boundaries.clean_attr('NM_ARON')(f))
    else:
        return boundaries.clean_attr('NM_ARON')(f)

for geographic_code, name in sets.items():
    boundaries.register('%s boroughs' % name,
        file='%s.shp' % unidecode(name),
        domain='%s, QC' % name,
        last_updated=date(2014, 2, 28),
        name_func=namer,
        id_func=lambda f: int(f.get('NO_ARON')),
        authority='Directeur général des élections du Québec',
        licence_url='http://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php',
        encoding='iso-8859-1',
        metadata={'geographic_code': '24%05d' % geographic_code},
    )
