from datetime import date

import boundaries

sets = {
    3530004: 'North Dumfries',
    3530010: 'Cambridge',
    3530013: 'Kitchener',
    3530016: 'Waterloo',
    3530020: 'Wilmot',
    3530027: 'Wellesley',
    3530035: 'Woolwich',
}

for geographic_code, name in sets.items():
    boundaries.register('%s wards' % name,
        domain='%s, ON' % name,
        last_updated=date(2017, 11, 20),
        name_func=lambda f: 'Ward %s' % f.get('WardNumber'),
        id_func=boundaries.attr('WardNumber'),
        authority='Regional Municipality of Waterloo',
        source_url='https://rowopendata-rmw.opendata.arcgis.com/datasets/8556e15d83d649e69f5806054c83ad8e_15',
        licence_url='https://www.regionofwaterloo.ca/en/regional-government/open-data.aspx',
        data_url='https://opendata.arcgis.com/datasets/8556e15d83d649e69f5806054c83ad8e_15.zip',
        encoding='iso-8859-1',
        extra={'division_id': 'ocd-division/country:ca/csd:%d' % geographic_code},
        is_valid_func=lambda f, name=name: f.get('Municipali') == name,
        notes='Compare the subdivisions in boundaries/ca_on_waterloo_wards/definition.py to:\nogrinfo -al -geom=NO boundaries/ca_on_waterloo_wards | grep " Municipali" | sort | uniq | cut -d= -f 2',
        skip_crc32=True,
    )
