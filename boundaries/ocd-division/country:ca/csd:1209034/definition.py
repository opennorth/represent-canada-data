from datetime import date

import boundaries

boundaries.register('Halifax districts',
    domain='Halifax, NS',
    last_updated=date(2017, 10, 31),
    name_func=boundaries.clean_attr('DISTNAME'),
    id_func=boundaries.attr('DIST_ID'),
    authority='Halifax Regional Municipality',
    source_url='http://catalogue-hrm.opendata.arcgis.com/datasets/polling-districts',
    licence_url='https://www.halifax.ca/home/open-data/open-data-license',
    data_url='https://opendata.arcgis.com/datasets/04c5bee564f84b4a8f1c8dd305896079_0.zip',
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca/csd:1209034'},
)
