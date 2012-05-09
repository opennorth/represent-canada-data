from datetime import date

import boundaries

boundaries.register('', # The name of the boundary set
    # Generic singular name for a boundary from this set. Optional if the
    # boundary set's name ends in "s".
    singular='',
    # Geographic extents which the boundary set encompasses
    domain='',
    # Last time the source was updated or checked for new data
    last_updated=date(1970, 1, 1),
    # Function to extract a feature's "name" property
    name_func=boundaries.attr(''),
    # Function to extract a feature's "external_id" property
    id_func=boundaries.attr(''),
    # Authority that is responsible for the accuracy of this data
    authority='',
    # A URL to the source of this data
    source_url='',
    # A URL to the license for this data
    licence_url='',
    # A URL to the data file, e.g. a ZIP archive
    data_url='',
    # Notes identifying any pecularities about the data, such as columns that
    # were deleted or files which were merged
    notes='',
    # Encoding of the text fields in the shapefile, e.g. 'utf-8'. Default: 'ascii'
    encoding='',
)
