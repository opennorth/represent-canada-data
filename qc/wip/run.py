# coding: utf-8
from __future__ import unicode_literals

import os.path

from invoke import run
from unidecode import unidecode

# Creates a shapefile for each Indian reserve and Indian settlement to be merged
# into its parent municipality's shapefile.
# 2014-03-25 IWergifosse@dgeq.qc.ca

sets = {
    72032: "Oka",
    72802: "Kanesatake",  # Oka
    89008: "Val-d'Or",
    89804: "Lac-Simon",  # Val d'Or
    90012: "La Tuque",
    90801: "Coucoucache",  # La Tuque
    90802: "Wemotaci",  # La Tuque
    90804: "Obedjiwan",  # La Tuque
    97007: "Sept-Îles",
    97802: "Uashat",  # Sept-Îles
    97804: "Maliotenam",  # Sept-Îles
}

for geographic_code, name in sets.items():
  file = 'qc/wip/%s-24%s.shp' % (unidecode(name), geographic_code)
  if not os.path.exists(file):
    run('''ogr2ogr -f "ESRI Shapefile" "%s" "qc/districts/Districts Elec Mun 2014-02-28_DetU_region.shp" -where "CO_MUNCP='%s'"''' % (file, geographic_code), echo=True)
