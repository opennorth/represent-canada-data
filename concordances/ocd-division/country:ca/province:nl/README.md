Source: Received via email from Elections Newfoundland and Labrador.

Pre-process:

    ./update.sh

Install:

    fab alpheus update_concordances:args="--searchfield=name newfoundland-and-labrador-electoral-districts gov.nl.ca data/shapefiles/public/concordances/ocd-division/country:ca/province:nl/out.csv"

The Excel file contains a few postcodes containing invalid letters D, F or O.
