from datetime import date

import boundaries

boundaries.register('Caledon wards',
    domain='Caledon, ON',
    last_updated=date(2012, 2, 24),
    name_func=boundaries.dashed_attr('WARDNUM'),
    id_func=boundaries.attr('WARDNUM'),
    authority='Region of Peel',
    source_url='http://opendata.peelregion.ca/data-categories/regional-geography/ward-boundaries-(2010-2014).aspx',
    licence_url='http://opendata.peelregion.ca/terms-of-use.aspx',
    data_url='http://opendata.peelregion.ca/media/2549/wardboundaries_shp.zip',
    notes="""Select only Caledon wards: ogr2ogr -f "ESRI Shapefile" -where "MUNIC='10'" Caledon.shp wardbnd_1014.shp""",
    encoding='iso-8859-1',
)
