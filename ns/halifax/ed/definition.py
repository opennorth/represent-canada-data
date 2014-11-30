from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Halifax districts',
    domain='Halifax, NS',
    last_updated=date(2014, 11, 30),
    name_func=boundaries.attr('DISTNAME'),
    id_func=boundaries.attr('DIST_ID'),
    authority='Halifax Regional Municipality',
    source_url='http://catalogue.hrm.opendata.arcgis.com/datasets/b2c71fb0d90f41488fae2ad2c8278f6d_0',
    data_url='http://catalogue.hrm.opendata.arcgis.com/datasets/b2c71fb0d90f41488fae2ad2c8278f6d_0.zip',
    licence_url='http://www.halifax.ca/opendata/OD_TermsOfUse.php',
    encoding='utf-8',
    metadata={'geographic_code': '1209034'},
)
