from datetime import date

import boundaries

boundaries.register('Edmonton wards',
    domain='Edmonton, AB',
    last_updated=date(2010, 9, 23),
    name_func=lambda f: f.get('Name').replace(' 0', ' '),
    id_func=lambda f: re.sub(r'\D+0?', '', f.get('Name')),
    authority='City of Edmonton',
    licence_url='http://www.edmonton.ca/city_government/initiatives_innovation/open-data-terms-of-use.aspx',
    notes='We use a KML file that is no longer accessible from the Edmonton Open Data Catalogue. Convert the KML to SHP with: ogr2ogr -f "ESRI Shapefile" . CityWards2010.kml -nlt POLYGON',
    encoding='iso-8859-1',
    geographic_code='4811061',
)
