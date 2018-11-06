from datetime import date

import boundaries

boundaries.register('London wards',
    domain='London, ON',
    last_updated=date(2018, 11, 5),
    name_func=lambda f: 'Ward %s' % f.get('Ward'),
    id_func=boundaries.attr('Ward'),
    authority='City of London',
    source_url='http://www.london.ca/city-hall/open-data/Pages/Open-Data-Data-Catalogue.aspx',
    licence_url='http://www.london.ca/city-hall/open-data/Pages/OpenData-TermsofUse.aspx',
    data_url='http://apps.london.ca/OpenData/ShapeFiles_Zipped/Election_2018_wardPollBoundaries.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3539036'},
    prj='http://spatialreference.org/ref/epsg/26917/prj/',
)
