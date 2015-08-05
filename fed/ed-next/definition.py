# coding: utf-8
from __future__ import unicode_literals

from datetime import date

import boundaries


def namer(f):
    return boundaries.clean_attr('ENNAME')(f).replace('\x97', '—').replace(' dOr', " d'Or")  # Beauport--Côte-de-Beaupré--Île dOrléans--Charlevoix

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
