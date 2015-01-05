from __future__ import unicode_literals

from datetime import date

import boundaries

boundaries.register('Calgary wards',
    domain='Calgary, AB',
    last_updated=date(2015, 1, 5),
    name_func=boundaries.clean_attr('LABEL'),
    id_func=boundaries.attr('WARD_NUM'),
    authority='City of Calgary',
    source_url='https://data.calgary.ca/OpenData/Pages/DatasetDetails.aspx?DatasetID=PDC0-99999-99999-00009-P%28CITYonlineDefault%29',
    licence_url='https://data.calgary.ca/OpenData/Pages/TermsofUse.aspx',
    data_url='https://data.calgary.ca/_layouts/OpenData/DownloadDataset.ashx?Format=SHP&DatasetId=PDC0-99999-99999-00009-P(CITYonlineDefault)&VariantId=3(CITYonlineDefault)',
    encoding='iso-8859-1',
    metadata={'geographic_code': '4806016'},
)
