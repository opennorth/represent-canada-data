# coding: utf-8
import os.path

from invoke import run

# Creates a shapefile for each Indian reserve and Indian settlement to be merged
# into its parent municipality's shapefile.
# 2014-03-25 IWergifosse@dgeq.qc.ca

sets = {
    72032: u"Oka",
    72802: u"Kanesatake", # Oka
    89008: u"Val-d'Or",
    89804: u"Lac-Simon", # Val d'Or
    90012: u"La Tuque",
    90801: u"Coucoucache", # La Tuque
    90802: u"Wemotaci", # La Tuque
    90804: u"Obedjiwan", # La Tuque
    97007: u"Sept-Îles",
    97802: u"Uashat", # Sept-Îles
    97804: u"Maliotenam", # Sept-Îles
}

for geographic_code, name in sets.items():
  file = 'qc/wip/%s-24%s.shp' % (name, geographic_code)
  if not os.path.exists(file):
    run('''ogr2ogr -f "ESRI Shapefile" "%s" "qc/districts/Districts Elec Mun 2014-02-28_DetU_region.shp" -where "CO_MUNCP='%s'"''' % (file, geographic_code), echo=True)
