from datetime import date

import boundaries

boundaries.register('St. Catharines wards',
    domain='St. Catharines, ON',
    last_updated=date(2016, 5, 17),
    name_func=boundaries.clean_attr('WardName'),
    authority='City of St. Catharines',
    encoding='iso-8859-1',
    source_url='https://niagaraopendata.ca/dataset/st-catharines-wards',
    licence_url='https://niagaraopendata.ca/pages/open-government-license-2-0-the-corporation-of-the-city-of-st-catharines',
    data_url='https://www.niagaraopendata.ca//dataset/04304ccc-e282-41df-9bd9-e997bc1f2d96/resource/77dfbcf3-4faf-446e-a816-c6def452150f/download/stcathwards.zip',
    extra={'division_id': 'ocd-division/country:ca/csd:3526053'},
)
