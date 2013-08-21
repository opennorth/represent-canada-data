from datetime import date

import boundaries

boundaries.register('Calgary wards',
    domain='Calgary, AB',
    last_updated=date(2011, 11, 23),
    name_func=boundaries.clean_attr('LABEL'),
    id_func=boundaries.attr('WARD_NUM'),
    authority='City of Calgary',
    source_url='https://cityonline.calgary.ca/Pages/Category.aspx?cat=CITYonlineDefault&category=PDCAdministrativeBoundaries&publicdata',
    licence_url='https://cityonline.calgary.ca/Pages/PdcTermsOfUse.aspx',
    encoding='iso-8859-1',
    metadata={'geographic_code': '4806016'},
)
