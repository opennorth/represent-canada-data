from __future__ import unicode_literals

import re
from datetime import date

import boundaries

boundaries.register('Haldimand County wards',
    domain='Haldimand County, ON',
    last_updated=date(2016, 10, 5),
    name_func=boundaries.attr('Ward'),
    id_func=lambda f: re.sub(r'\D', '', f.get('Ward')),
    authority='Corporation of Haldimand County',
    source_url='http://opendata.haldimandcounty.on.ca/datasets/8e0ac38a4c96452ab3c9900a8251e42c_49',
    licence_url='http://opendata.haldimandcounty.on.ca/',
    data_url='http://opendata.haldimandcounty.on.ca/datasets/8e0ac38a4c96452ab3c9900a8251e42c_49.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:3528018'},
)
