from datetime import date

import boundaries

boundaries.register('Ontario English Catholic School Board boundaries',
    domain='Ontario',
    last_updated=date(2015, 11, 8),
    name_func=boundaries.attr('NAME'),
    id_func=boundaries.attr('SDSB_ID'),
    authority='Her Majesty the Queen in Right of Ontario',
    source_url='https://geohub.lio.gov.on.ca/datasets/school-board-boundaries',
    licence_url='https://geohub.lio.gov.on.ca/datasets/school-board-boundaries',
    data_url='https://ws.gisetl.lrc.gov.on.ca/fmedatadownload/Packages/SchoolBoardBoundaries.zip',
    encoding='utf-8',
)
