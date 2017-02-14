from datetime import date

import boundaries

boundaries.register('London wards',
    domain='London, ON',
    last_updated=date(2013, 6, 11),
    name_func=lambda f: 'Ward %s' % f.get('WARDS'),
    id_func=boundaries.attr('WARDS'),
    authority='City of London',
    source_url='http://www.london.ca/city-hall/open-data/Pages/Open-Data-Data-Catalogue.aspx',
    licence_url='http://www.london.ca/city-hall/open-data/Pages/OpenData-TermsofUse.aspx',
    data_url='http://apps.london.ca/OpenData/ShapeFiles_Zipped/2010_electoral_wards.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3539036'},
    prj='http://spatialreference.org/ref/epsg/26917/prj/',
)
