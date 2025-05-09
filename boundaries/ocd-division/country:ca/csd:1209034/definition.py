from datetime import date

import boundaries


def namer(f):
    import boundaries
    return boundaries.clean_attr('DISTNAME')(f).replace('&', "and")


boundaries.register('Halifax districts',
    domain='Halifax, NS',
    last_updated=date(2024, 11, 6),
    name_func=namer,
    id_func=boundaries.attr('DIST_ID'),
    authority='Halifax Regional Municipality',
    source_url='https://data-hrm.hub.arcgis.com/datasets/04c5bee564f84b4a8f1c8dd305896079_0',
    licence_url='https://data-hrm.hub.arcgis.com/pages/open-data-licence',
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca/csd:1209034'},
)
