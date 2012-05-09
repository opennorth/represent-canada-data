from datetime import date
import re

import boundaries

boundaries.register('Regina wards',
    domain='Regina, SK',
    last_updated=date(2012, 2, 28),
    name_func=boundaries.attr('WARD'),
    id_func=boundaries.attr('WARD'),
    authority='City of Regina',
    source_url='http://openregina1.cloudapp.net/DataBrowser/openregina/Wards',
    licence_url='http://www.regina.ca/residents/open-government/data/terms/',
    data_url='http://configdataogdiregina.blob.core.windows.net/converteddata/shp.Wards.zip',
    notes='Convert the features to 2D with: ogr2ogr -f "ESRI Shapefile" -overwrite . Wards.shp -nlt POLYGON',
    encoding='iso-8859-1',
)
