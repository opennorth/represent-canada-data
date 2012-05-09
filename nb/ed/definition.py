from datetime import date

import boundaries

boundaries.register('New Brunswick electoral districts',
    domain='New Brunswick',
    last_updated=date(2011, 3, 8),
    name_func=boundaries.attr('PED_Name_E'),
    id_func=boundaries.attr('PED_Num'),
    authority='Office of the Chief Electoral Officer',
    source_url='http://www.snb.ca/gdam-igec/e/2900e_1e_i.asp',
    licence_url='http://www.snb.ca/gdam-igec/e/2900e_agreement.asp',
    data_url='http://www.snb.ca/topo/aadb/shape/nbaa_5013_ranb.zip',
    notes='The shapefile is out-of-date. Instead, we use a shapefile received via email with NAD83(CSRS) / New Brunswick Stereographic (EPSG:2953) from http://spatialreference.org/ref/epsg/2953/prj/',
    encoding='iso-8859-1',
)