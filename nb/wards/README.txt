# https://github.com/openaddresses/esri-dump/
npm install -g esri-dump
esri-dump http://geonb.snb.ca/ArcGIS/rest/services/ElectionsNB/GeoNB_ENB_MunicipalWards/MapServer/0 > wards.geojson
ogr2ogr -f "ESRI Shapefile" . wards.geojson
