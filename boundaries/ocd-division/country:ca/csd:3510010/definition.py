from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Kingston wards',
    domain='Kingston, ON',
    last_updated=date(2012, 10, 25),
    name_func=boundaries.attr('ELECTORAL_'),
    id_func=boundaries.attr('ELECTORAL1'),
    # @note The new data license is more restrictive than our current custom
    #   agreement. However, the new data is for 2014 boundaries.
    # source_url='http://www.cityofkingston.ca/explore/data-catalogue',
    # licence_url='http://www.cityofkingston.ca/documents/10180/144997/GIS+-+Data+License+Agreement+Template.pdf/45503bd1-500f-4cfd-af6f-f34221ce78c3',
    authority='City of Kingston',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3510010'},
)
