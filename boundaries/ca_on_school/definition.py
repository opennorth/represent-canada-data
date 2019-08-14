from datetime import date

import boundaries

sets = {
    'English Catholic': 'BOARD_ENGLISH_CATHOLIC',
    'English Public': 'BOARD_ENGLISH_PUBLIC',
    'French Public': 'BOARD_FRENCH_PUBLIC',
}

for school_board_type, basename in sets.items():
    boundaries.register('Ontario {} School Board boundaries'.format(school_board_type),
        singular='Ontario {} School Board boundary'.format(school_board_type),
        domain='Ontario',
        last_updated=date(2017, 9, 12),
        name_func=boundaries.attr('NAME'),
        id_func=boundaries.attr('SDSB_ID'),
        authority='Her Majesty the Queen in Right of Ontario',
        source_url='https://geohub.lio.gov.on.ca/datasets/school-board-boundaries',
        licence_url='https://geohub.lio.gov.on.ca/datasets/school-board-boundaries',
        data_url='https://ws.gisetl.lrc.gov.on.ca/fmedatadownload/Packages/SchoolBoardBoundaries.zip',
        encoding='utf-8',
        basename=basename,
    )
