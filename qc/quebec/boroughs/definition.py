#coding: utf-8
from datetime import date

import boundaries

boundaries.register(u'Québec boroughs',
    domain=u'Québec, QC',
    last_updated=date(2014, 2, 4),
    name_func=lambda f: re.sub('?', u'—', f.get('NOM')), # m-dash
    id_func=boundaries.attr('CODE'),
    authority=u'Ville de Québec',
    source_url='http://donnees.ville.quebec.qc.ca/donne_details.aspx?jdid=2',
    licence_url='http://donnees.ville.quebec.qc.ca/licence.aspx',
    data_url='http://donnees.ville.quebec.qc.ca/Handler.ashx?id=2&f=SHP',
    encoding='iso-8859-1',
    metadata={'geographic_code': '2423027'},
    prj='http://spatialreference.org/ref/epsg/4326/prj/',
)
