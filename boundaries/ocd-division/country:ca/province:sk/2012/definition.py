from datetime import date

import boundaries


boundaries.register('Saskatchewan electoral districts (Representation Act, 2012)',
    singular='Saskatchewan electoral district',
    domain='Saskatchewan',
    last_updated=date(2014, 3, 20),  # historical
    name_func=boundaries.dashed_attr('Con_Name'),
    id_func=boundaries.attr('Con_Num'),
    authority='Her Majesty the Queen in Right of Saskatchewan',
    source_url='https://www.geosask.ca/',
    licence_url='https://www.geosask.ca/Portal/jsp/terms_popup.jsp',
    # The data, previously available from GeoSask, is now available from Elections Saskatchewan, but without a license, at http://www.elections.sk.ca/voters/maps/
    # data_url='http://electionssk1.blob.core.windows.net/shapefiles/Constit_2012.zip',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/province:sk'},
)
