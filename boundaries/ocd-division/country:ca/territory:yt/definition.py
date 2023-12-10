from datetime import date

import boundaries

boundaries.register('Yukon electoral districts (2015)',
    singular='Yukon electoral district',
    domain='Yukon',
    last_updated=date(2020, 11, 6),
    name_func=boundaries.attr('ELECT_NAME'),
    id_func=boundaries.attr('ELECT_NUM'),
    source_url='https://open.yukon.ca/data/datasets/yukon-electoral-districts-2015',
    data_url='https://map-data.service.yukon.ca/GeoYukon/Administrative_Boundaries/Yukon_Electoral_Districts_2015/Yukon_Electoral_Districts_2015.shp.zip',
    licence_url='https://open.yukon.ca/open-government-licence-yukon',
    authority='Her Majesty the Queen in Right of Yukon',
    encoding='utf-8',
    extra={'division_id': 'ocd-division/country:ca/territory:yt'},
)
