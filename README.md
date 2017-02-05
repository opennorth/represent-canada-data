# Represent API: Data

[Represent](https://represent.opennorth.ca/) is the open database of Canadian elected officials and electoral districts. It provides a [REST API](https://represent.opennorth.ca/api/) to boundary, representative, and postcode resources.

This repository stores the digital boundary files for the database. The [represent-canada](https://github.com/opennorth/represent-canada) repository is what's running at [represent.opennorth.ca](https://represent.opennorth.ca/).

## License

Open North has permission to redistribute all shapefiles in this repository. Please read the [overall license](https://github.com/opennorth/represent-canada-data/tree/master/LICENSE.txt) and the `LICENSE.txt` file in each directory to know your rights. In some cases, you will not have permission to redistribute the shapefile.

## Completeness

Open North lacks permission to redistribute the shapefiles of some boundary sets in the API. Refer to the `source_url`, `licence_url` and `data_url` of those boundary sets to get copies of those shapefiles.

## Provenance

All datasets are from government sources, with one exception: the postal code<sup>OM</sup> dataset in the `postcodes/fed` directory is from [Geocoder.ca](http://geocoder.ca/). The `definition.py` files will have more details on sources and any modifications made to the files. Postal Code<sup>OM</sup> is an official mark of Canada Post Corporation.

## Maintenance

### One-time setup

    # Invoke must not be installed globally.
    pip uninstall invoke

    # Create a virtual environment.
    mkvirtualenv representdata

    # Install the requirements.
    pip install -r requirements.txt flake8
    npm install -g esri-dump

### Regular tasks

For all the following commands, add `--base=path/to/private/data` to run then on the private repository.

Load the virtual environment:

    workon representdata

Make the code style consistent:

    flake8

Check that all `definition.py` files are valid:

    invoke definitions

Check that the source, data and license URLs work:

    invoke urls

Check that all data directories contain a `LICENSE.txt`:

    invoke licenses

Update a specific out-of-date shapefile:

    invoke shapefiles --base=boundaries/ocd-division/country:ca/province:qc

Or, update all out-of-date shapefiles. The output may contain additional instructions:

    invoke shapefiles

Some shapefiles are online but require exceptional processing. Remember to update `last_updated` in `definition.py`:

    esri-dump http://geonb.snb.ca/ArcGIS/rest/services/GeoNB_ENB_MunicipalWards/MapServer/0 > boundaries/ca_nb_wards/wards.geojson
    ogr2ogr -f "ESRI Shapefile" boundaries/ca_nb_wards boundaries/ca_nb_wards/wards.geojson

Fix file permissions:

    invoke permissions

Check if the data request process spreadsheet is out-of-date:

    invoke spreadsheet

Or less verbose:

    invoke spreadsheet --base=. --private-base=../represent-canada-data-private > /dev/null

## Contact

Please use [GitHub Issues](https://github.com/opennorth/represent-canada-data/issues) for bug reports. You may also contact [represent@opennorth.ca](mailto:represent@opennorth.ca).

## Acknowledgements

We would like to express our gratitude to [Kent Mewhort](http://www.openissues.ca/) at the [Canadian Internet Policy and Public Interest Clinic (CIPPIC)](https://cippic.ca/), whose [legal research](https://cippic.ca/en/open_governance) ([PDF](https://cippic.ca/en/publications/how_to_redistribute_open_data)) made it possible for this repository to be made public.
