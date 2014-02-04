from datetime import date

import boundaries

boundaries.register('Toronto wards',
    domain='Toronto, ON',
    last_updated=date(2012, 10, 24),
    name_func=boundaries.dashed_attr('NAME'),
    id_func=lambda f: re.sub('\A0', '', f.get('SCODE_NAME')),
    authority='City of Toronto',
    source_url='http://www1.toronto.ca/wps/portal/contentonly?vgnextoid=b1533f0aacaaa210VgnVCM1000006cd60f89RCRD&vgnextchannel=1a66e03bb8d1e310VgnVCM10000071d60f89RCRD',
    licence_url='http://www1.toronto.ca/wps/portal/contentonly?vgnextoid=4a37e03bb8d1e310VgnVCM10000071d60f89RCRD&vgnextfmt=default',
    data_url='http://www1.toronto.ca/City_Of_Toronto/Information_Technology/Open_Data/Data_Sets/Assets/Files/wards_may2010_wgs84.zip',
    encoding='iso-8859-1',
    metadata={'geographic_code': '3520005'},
)
