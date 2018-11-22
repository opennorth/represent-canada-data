from datetime import date

import boundaries

boundaries.register('Winnipeg wards',
    domain='Winnipeg, MB',
    last_updated=date(2018, 11, 22),
    name_func=boundaries.clean_attr('name'),
    id_func=lambda f: int(f.get('id')),
    authority='City of Winnipeg',
    source_url='https://data.winnipeg.ca/Council-Services/Electoral-Boundaries-as-of-September-17th-2018/qake-hdwc',
    licence_url='https://data.winnipeg.ca/open-data-licence',
    data_url='https://data.winnipeg.ca/api/geospatial/qake-hdwc?method=export&format=Shapefile',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:4611040'},
)
