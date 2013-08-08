from datetime import date

import boundaries

boundaries.register('Toronto wards',
    domain='Toronto, ON',
    last_updated=date(2010, 6, 3),
    name_func=boundaries.dashed_attr('NAME'),
    id_func=boundaries.attr('SCODE_NAME'),
    authority='City of Toronto',
    source_url='http://www1.toronto.ca/wps/portal/open_data/open_data_item_details?vgnextoid=b1533f0aacaaa210VgnVCM1000006cd60f89RCRD&vgnextchannel=6e886aa8cc819210VgnVCM10000067d60f89RCRD',
    licence_url='http://www1.toronto.ca/wps/portal/open_data/open_data_fact_sheet_details?vgnextoid=59986aa8cc819210VgnVCM10000067d60f89RCRD',
    data_url='http://www1.toronto.ca/City_Of_Toronto/Information_Technology/Open_Data/Data_Sets/Assets/Files/wards_may2010_wgs84.zip',
    encoding='iso-8859-1',
    geographic_code='3520005',
)
