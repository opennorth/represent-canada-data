from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Ottawa wards',
    domain='Ottawa, ON',
    last_updated=date(2016, 1, 5),
    name_func=boundaries.attr('Name'),
    id_func=lambda f: re.sub(r'\D', '', f.get('Name')),
    authority='City of Ottawa',
    source_url='http://data.ottawa.ca/en/dataset/wards-2014',
    licence_url='http://ottawa.ca/en/mobile-apps-and-open-data/open-data-terms-use',
    # Jan 8: Reported the shapefile as missing a DBF file.
    # http://data.ottawa.ca/dataset/8321248d-0b86-47cd-9c83-c848a1bc0098/resource/8152e707-fc28-409c-9bbe-8cb9f88dca86/download/wards-2014shp.shp.zip
    data_url='http://data.ottawa.ca/dataset/8321248d-0b86-47cd-9c83-c848a1bc0098/resource/d63e4443-febd-4d4a-ba9a-444d49c10124/download/wards-2014kmz.kmz',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3506008'},
)
