from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Burlington wards',
    domain='Burlington, ON',
    last_updated=date(2016, 11, 22),
    name_func=lambda f: 'Ward %s' % f.get('WARD_NO'),
    id_func=boundaries.attr('WARD_NO'),
    authority='City of Burlington',
    source_url='http://cob.burlington.opendata.arcgis.com/datasets/3eba66ef43b0499d86d9e72aef66b65a_22',
    licence_url='http://www.burlington.ca/en/services-for-you/resources/Ongoing_Projects/Open_Data/OpenDataBurlingtonTermsOfUseSeptember192011.pdf',
    data_url='http://cob.burlington.opendata.arcgis.com/datasets/3eba66ef43b0499d86d9e72aef66b65a_22.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3524002'},
)
