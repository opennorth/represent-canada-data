from datetime import date

import boundaries

boundaries.register('Caledon wards',
    domain='Caledon, ON',
    last_updated=date(2019, 1, 3),
    name_func=lambda f: 'Ward %s' % f.get('WARDNUM'),
    id_func=boundaries.attr('WARDNUM'),
    authority='Regional Municipality of Peel',
    source_url='http://opendata.peelregion.ca/data-categories/regional-geography/ward-boundaries-(2018-2022).aspx',
    licence_url='http://opendata.peelregion.ca/terms-of-use.aspx',
    data_url='http://opendata.peelregion.ca/media/43508/wardbnd1822_shp.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3521024'},
    is_valid_func=lambda f: f.get('MUNIC') == 'Caledon',
)
