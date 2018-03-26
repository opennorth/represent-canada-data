Source: https://www.electionsquebec.qc.ca/francais/provincial/carte-electorale/entites-administratives-liees-a-un-code-postal.php

Download and pre-process:

    ./update.sh

Install:

    fab alpheus update_concordances:args="quebec-electoral-districts electionsquebec.qc.ca data/shapefiles/public/concordances/ocd-division/country:ca/province:qc/out.csv"
