from datetime import date

import boundaries

boundaries.register('Edmonton wards',
    domain='Edmonton, AB',
    last_updated=date(2010, 9, 23),
    name_func=lambda f: f.get('Name').replace(' 0', ' '),
    id_func=lambda f: re.sub(r'\D+0?', '', f.get('Name')),
    authority='City of Edmonton',
    source_url='https://data.edmonton.ca/City-Administration/City-of-Edmonton-Ward-Boundaries/yhng-294h',
    data_url='https://data.edmonton.ca/api/geospatial/yhng-294h?method=export&format=Shapefile',
    licence_url='http://www.edmonton.ca/city_government/initiatives_innovation/open-data-terms-of-use.aspx',
    encoding='iso-8859-1',
    geographic_code='4811061',
)
