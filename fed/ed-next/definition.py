# coding: utf-8
from __future__ import unicode_literals

from datetime import date

import boundaries


def namer(f):
    import boundaries
    n = boundaries.clean_attr('ENNAME')(f).replace('\x97', '—')

    # @see http://www.parl.gc.ca/HousePublications/Publication.aspx?Language=E&Mode=1&DocId=6684609&File=4
    mappings = {
        "Western Arctic": "Northwest Territories",
        # "Blainville": "Thérèse-De Blainville",
        # "Boucher—Les Patriotes—Verchères": "Pierre-Boucher—Les Patriotes—Verchères",
        # "Centre-du-Bas-Saint-Laurent": "Rimouski-Neigette—Témiscouata—Les Basques",
        # "Charlevoix—Montmorency": "Beauport—Côte-de-Beaupré—Île d’Orléans—Charlevoix",
        # "Chicoutimi": "Chicoutimi—Le Fjord",
        # "Dorval—Lachine": "Dorval—Lachine—LaSalle",
        # "LaSalle—Verdun": "LaSalle—Émard—Verdun",
        # "LeMoyne": "Longueuil—Charles-LeMoyne",
        # "Longueuil": "Longueuil—Saint-Hubert",
        # "Mont-Royal": "Mount Royal",
        # "Sainte-Rose": "Marc-Aurèle-Fortin",
        # "Soulanges—Vaudreuil": "Vaudreuil—Soulanges",
        # "Ville-Marie": "Ville-Marie—Le Sud-Ouest—Île-des-Soeurs",
        # "Brant": "Brantford—Brant",
        # "Lanark—Frontenac": "Lanark—Frontenac—Kingston",
        # "Leeds—Grenville": "Leeds—Grenville—Thousand Islands and Rideau Lakes",
        # "Mississauga—Cooksville": "Mississauga East—Cooksville",
        # "Northumberland—Pine Ridge": "Northumberland—Peterborough South",
        # "Ottawa—Orléans": "Orléans",
        # "Peterborough": "Peterborough—Kawartha",
        # "Rideau—Carleton": "Carleton",
        # "St. Paul's": "Toronto—St. Paul's",
        # "York West": "Humber River—Black Creek",
        # "Humboldt—Warman—Martensville—Rosetown": "Carlton Trail—Eagle Creek",
        # "Grande Prairie": "Grande Prairie—Mackenzie",
        # "Medicine Hat": "Medicine Hat—Cardston—Warner",
        # "Red Deer—Wolf Creek": "Red Deer—Lacombe",
        # "Sturgeon River": "Sturgeon River—Parkland",
        # "Saanich—Esquimalt—Juan de Fuca": "Esquimalt—Saanich—Sooke",
        # "Vancouver Island North—Comox—Powell River": "North Island—Powell River",
    }

    for key, value in mappings.items():
        if n == key:
            return value
    return n

boundaries.register('Federal electoral districts (next election)',
    singular='Federal electoral district',
    domain='Canada',
    last_updated=date(2014, 9, 23),
    name_func=namer,
    id_func=boundaries.attr('FEDNUM'),
    slug_func=boundaries.attr('FEDNUM'),
    authority='Her Majesty the Queen in Right of Canada',
    source_url='http://geogratis.gc.ca/api/en/nrcan-rncan/ess-sst/56124851-71fc-4f94-8df2-40f59cd1dd46.html',
    licence_url='http://open.canada.ca/en/open-government-licence-canada',
    data_url='http://ftp2.cits.rncan.gc.ca/pub/geobase/official/fed_cf/shp_eng/fed_cf_CA_2_1_shp_en.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '01'},
    notes='Merge electoral districts with multiple features into single features.',
)
