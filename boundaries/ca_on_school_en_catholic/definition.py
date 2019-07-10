from datetime import date

import boundaries

boundaries.register('Ontario English Catholic School Board',
    domain='Canada',
    last_updated=date(2015, 11, 8),
    name_func=boundaries.attr('CDNAME'),
    id_func=boundaries.attr('CDUID'),
    slug_func=boundaries.attr('CDUID'),
    authority='Land Information Ontario',
    source_url='https://geohub.lio.gov.on.ca/datasets/school-board-boundaries',
    licence_url='https://geohub.lio.gov.on.ca/datasets/school-board-boundaries#',
    data_url='https://ws.gisetl.lrc.gov.on.ca/fmedatadownload/Packages/SchoolBoardBoundaries.zip',
    encoding='utf-8',
)
