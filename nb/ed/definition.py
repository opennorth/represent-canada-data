from datetime import date

import boundaries

boundaries.register('New Brunswick electoral districts',
    domain='New Brunswick',
    last_updated=date(2011, 3, 8),
    name_func=boundaries.attr('PED_Name_E'),
    id_func=boundaries.attr('PED_Num'),
    authority='Office of the Chief Electoral Officer',
    source_url='http://www.gnb.ca/elections/10prov/10provmap-e.asp',
    data_url='http://www.gnb.ca/elections/pdf/2010PEDMaps/NB_Electoral_Districts.zip',
    notes='We use NAD83(CSRS) / New Brunswick Stereographic (EPSG:2953) from http://spatialreference.org/ref/epsg/2953/prj/',
    encoding='iso-8859-1',
    geographic_code='13',
)
