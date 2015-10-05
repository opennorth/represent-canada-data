from __future__ import unicode_literals

from datetime import date

import boundaries


def ider(f):
    """
    https://saskatoonopendatastorage.blob.core.windows.net/converteddata/kml.CurrentWardBoundaries.zip
    """
    return {
        'Holliston - Greystone Heights': 8,
        'Fairhaven - Confederation Park': 3,
        'Riversdale - Montgomery Park': 2,
        'Dundonald - Mount Royal': 4,
        'Silverwood Heights - Lawson Heights': 5,
        'Exhibition - Eastview': 7,
        'Sutherland - Erindale': 10,
        'Wildwood - Lakeview': 9,
        'City Park - River Heights': 1,
        'Nutana - City Centre': 6,
    }[f.get('Name')]

boundaries.register('Saskatoon wards',
    domain='Saskatoon, SK',
    last_updated=date(2015, 5, 22),
    name_func=boundaries.clean_attr('Name'),
    id_func=ider,
    authority='City of Saskatoon',
    source_url='http://opendata-saskatoon.cloudapp.net/DataBrowser/SaskatoonOpenDataCatalogueBeta/CurrentWardBoundaries',
    data_url='https://saskatoonopendatastorage.blob.core.windows.net/converteddata/kml.CurrentWardBoundaries.zip',
    licence_url='http://opendata-saskatoon.cloudapp.net/TermsOfUse/TermsOfUse',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/csd:4711066'},
)
