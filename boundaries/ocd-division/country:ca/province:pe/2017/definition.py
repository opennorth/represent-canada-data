# coding: utf-8
from datetime import date

import boundaries

boundaries.register('Prince Edward Island electoral districts (2017)',
    singular='Prince Edward Island electoral district',
    domain='Prince Edward Island',
    last_updated=date(2021, 2, 19),
    name_func=boundaries.attr('DISTRICT'),
    id_func=boundaries.attr('DIST_NO'),
    authority='Her Majesty the Queen in Right of Prince Edward Island',
    source_url='http://www.gov.pe.ca/gis/index.php3?number=77554&lang=E',
    data_url=(
        'http://www.gov.pe.ca/gis/download.php3?'
        'name=2017_Electoral&file_format=SHP'
    ),
    licence_url='http://www.gov.pe.ca/gis/index.php3?number=77462&lang=E',
    encoding='iso-8859-1',
    extra={'division_id': 'ocd-division/country:ca/province:pe'},
    is_valid_func=lambda f: f.get('DISTRICT'),
)
