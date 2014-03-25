import os.path

from invoke import run

sets = {
    72802: u"Kanesatake",
    89804: u"Lac-Simon",
    90801: u"Coucoucache",
    90802: u"Wemotaci",
    90804: u"Obedjiwan",
    97802: u"Uashat",
    97804: u"Maliotenam",
}

for geographic_code, name in sets.items():
  file = 'qc/wip/%s-%s.shp' % (name, geographic_code)
  if not os.path.exists(file):
    run('''ogr2ogr -f "ESRI Shapefile" "%s" "qc/districts/Districts Elec Mun 2014-02-28_DetU_region.shp" -where "CO_MUNCP='%s'"''' % (file, geographic_code), echo=True)
