# coding: utf-8
from datetime import date

from unidecode import unidecode

import boundaries

sets = {
    # QGIS errors when merging or dissolving features.
    # '23027': u"Québec",
    # '25213': u"Lévis",
    '43027': u"Sherbrooke",
    '58227': u"Longueuil",
    '66023': u"Montréal",
    '94068': u"Saguenay",
}

def namer(f):
    import boundaries
    if f.get('CO_MUNCP') == 43027:
        return {
            u'Le Mont-Bellevue': 'Mont-Bellevue',
            u'Rock Rorest--Saint-lie--Deauville': 'Rock Forest—Saint-Élie—Deauville',
        }.get(f.get('NM_ARON'), f.get('NM_ARON'))
    else:
        return boundaries.attr('NM_ARON')(f)

for geographic_code, name in sets.items():
    boundaries.register(u'%s boroughs' % name,
        file='%s.shp' % unidecode(name),
        domain=u'%s, QC' % name,
        last_updated=date(2014, 2, 28),
        name_func=namer,
        id_func=lambda f: int(f.get('NO_ARON')),
        authority=u'Directeur général des élections du Québec',
        licence_url='http://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php',
        encoding='iso-8859-1',
        metadata={'geographic_code': '24%s' % geographic_code},
    )
