from datetime import date

import boundaries

boundaries.register('Halifax districts',
    domain='Halifax, NS',
    last_updated=date(2016, 11, 5),
    name_func=boundaries.clean_attr('DISTNAME'),
    id_func=boundaries.attr('DIST_ID'),
    authority='Halifax Regional Municipality',
    source_url='http://catalogue.hrm.opendata.arcgis.com/datasets/91dd3d978e3d4324bdb88f9fc5e675e4_0',
    data_url='http://catalogue.hrm.opendata.arcgis.com/datasets/91dd3d978e3d4324bdb88f9fc5e675e4_0.zip',
    licence_url='http://www.halifax.ca/opendata/OD_TermsOfUse.php',
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca/csd:1209034'},
)
