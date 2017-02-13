from __future__ import unicode_literals

from datetime import date

import boundaries


def namer(f):
    import boundaries
    if f.get('NM_DIS'):
        return {
            "Champlain-L'Île-des-Soeurs": "Champlain—L'Île-des-Soeurs",
            "d'Ahuntsic": 'Ahuntsic',
            'de Bordeaux-Cartierville': 'Bordeaux-Cartierville',
            'de Saint-Sulpice': 'Saint-Sulpice',
            'du Sault-au-Récollet': 'Sault-au-Récollet',
            'Est (Pierrefonds-Roxboro)': 'Bois-de-Liesse',
            'Maisonneuve-Longue-Pointe': 'Maisonneuve—Longue-Pointe',
            'Ouest (Pierrefonds-Roxboro)': 'Cap-Saint-Jacques',
            'Saint-Paul-Émard': 'Saint-Paul—Émard',
            'St-Henri-Petite-Bourgogne-Pte-St-Charles': 'Saint-Henri—Petite-Bourgogne—Pointe-Saint-Charles',
            'Étienne-Desmarteaux': 'Étienne-Desmarteau',
        }.get(f.get('NM_DIS'), f.get('NM_DIS'))
    else:
        return {
            'Le Plateau-Mont-Royal': 'Plateau-Mont-Royal',
            'Le Sud-Ouest': 'Sud-Ouest',
            'Pierrefond-Roxboro': 'Pierrefonds-Roxboro',
            'Rosemont--La-Petite-Patrie': 'Rosemont—La Petite-Patrie',
        }.get(f.get('NM_ARON'), boundaries.clean_attr('NM_ARON')(f))


def ider(f):
    if f.get('NO_DIS'):
        return f.get('NO_DIS')
    else:
        return int(f.get('NO_ARON'))


boundaries.register('Montréal boroughs and districts',
    domain='Montréal, QC',
    last_updated=date(2014, 2, 28),
    name_func=namer,
    id_func=ider,
    authority='Directeur général des élections du Québec',
    licence_url='http://www.electionsquebec.qc.ca/francais/conditions-d-utilisation-de-notre-site-web.php',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:2466023'},
    notes='ogr2ogr -f "ESRI Shapefile" boundaries/ocd-division/country:ca/csd:2466023/merge.shp boundaries/ca_qc_boroughs/Montreal.shp -select NM_ARON,NO_ARON\nogr2ogr -f "ESRI Shapefile" boundaries/ocd-division/country:ca/csd:2466023/merge.shp boundaries/ca_qc_districts/Montreal-2466023.shp -append -addfields',
)
