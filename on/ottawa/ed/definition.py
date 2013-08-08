from datetime import date

import boundaries

boundaries.register('Ottawa wards',
    domain='Ottawa, ON',
    last_updated=date(2010, 8, 27),
    name_func=boundaries.dashed_attr('WARD_EN'),
    id_func=boundaries.attr('WARD_NUM'),
    authority='City of Ottawa',
    source_url='http://ottawa.ca/online_services/opendata/info/wards2010_en.html',
    licence_url='http://ottawa.ca/online_services/opendata/terms_en.html',
    data_url='http://ottawa.ca/online_services/opendata/data/wards2010.zip',
    notes='Convert the features to 2D with: ogr2ogr -f "ESRI Shapefile" -overwrite . Wards_2010.shp -nlt POLYGON',
    encoding='iso-8859-1',
    geographic_code='3506008',
)
