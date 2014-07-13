from datetime import date

import boundaries

boundaries.register('Winnipeg wards',
    domain='Winnipeg, MB',
    last_updated=date(2014, 7, 13),
    name_func=boundaries.attr('DESCRIPTIO'),
    id_func=boundaries.attr('ID'),
    authority='City of Winnipeg',
    source_url='https://data.winnipeg.ca/Council-Services/Electoral-Ward/ede3-teb8',
    licence_url='https://data.winnipeg.ca/open-data-licence',
    data_url='https://data.winnipeg.ca/api/geospatial/ede3-teb8?method=export&format=Shapefile',
    encoding='iso-8859-1',
    metadata={'geographic_code': '4611040'},
)
