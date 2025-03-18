from datetime import date

import boundaries

boundaries.register('Halifax districts',
    domain='Halifax, NS',
    last_updated=date(2020, 11, 22),
    name_func=boundaries.clean_attr('DISTNAME'),
    id_func=boundaries.attr('DIST_ID'),
    authority='Halifax Regional Municipality',
    source_url='https://data-hrm.hub.arcgis.com/datasets/04c5bee564f84b4a8f1c8dd305896079_0',
    licence_url='https://data-hrm.hub.arcgis.com/pages/open-data-licence',
    data_url='https://data-hrm.hub.arcgis.com/datasets/04c5bee564f84b4a8f1c8dd305896079_0.zip',
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca/csd:1209034'},
)
