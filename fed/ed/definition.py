# coding: utf-8
from __future__ import unicode_literals

from datetime import date

import boundaries


def namer(f):
    import boundaries
    n = boundaries.clean_attr('FEDENAME')(f)

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

boundaries.register('Federal electoral districts',
    domain='Canada',
    last_updated=date(2011, 11, 28),
    name_func=namer,
    id_func=boundaries.attr('FEDUID'),
    slug_func=boundaries.attr('FEDUID'),
    authority='Her Majesty the Queen in Right of Canada',
    source_url='http://open.canada.ca/data/en/dataset/48f10fb9-78a2-43a9-92ab-354c28d30674',
    licence_url='http://open.canada.ca/en/open-government-licence-canada',
    data_url='http://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/files-fichiers/gfed000a11a_e.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '01'},
)
