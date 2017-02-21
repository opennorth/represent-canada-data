# Represent API: Data

[Represent](https://represent.opennorth.ca/) is the open database of Canadian elected officials and electoral districts. It provides a [REST API](https://represent.opennorth.ca/api/) to boundary, representative, and postcode resources.

This repository stores the digital boundary files for the database. The [represent-canada](https://github.com/opennorth/represent-canada) repository is what's running at [represent.opennorth.ca](https://represent.opennorth.ca/).

## Layout

Boundary files are under [boundaries/](boundaries/). Most are stored in a directory tree matching [Open Civic Data Division Identifiers (OCD-ID)](http://docs.opencivicdata.org/en/latest/proposals/0002.html) starting at [boundaries/ocd-division/](boundaries/ocd-division/). Federal, provincial and territorial boundary files are further scoped by [redistribution year](https://github.com/opennorth/represent-canada/issues/102).

A few boundary files exist outside the OCD-ID tree. Some, like `ca_cd` and `ca_csd`, are Census geography files whose OCD-ID would clash with Canada's. Others are the sources of multiple boundary sets in the API, each with a different OCD-ID.

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

For all the following commands, add `--base=path/to/private/data` to run them on the private repository.

Load the virtual environment:

    workon representdata

List the available maintenance tasks:

    invoke -l

#### Maintain definition files

Make the code style consistent:

    flake8

Check that all `definition.py` files are valid:

    invoke definitions

Check that all data directories contain a `LICENSE.txt` (don't run on the private repository):

    invoke licenses

Check that the source, data and license URLs work:

    invoke urls

Find and correct the URLs in `definition.py` files. If you update a `licence_url`, you may need to update other occurrences in `LICENSE.txt`, `constants.py`, `tasks.py` and [this master spreadsheet](https://docs.google.com/spreadsheets/d/1AmLQD2KwSpz3B4eStLUPmUQJmOOjRLI3ZUZSD5xUTWM/edit#gid=0). Once all corrections are made, re-run `definitions` and `urls`.

If you update a `data_url`, update its shapefile, `name_func` and `id_func` following the instructions below.

#### Download shapefiles

Check for old boundaries that may require manual updates:

    invoke manual

Update a specific out-of-date shapefile. This task updates the `last_updated` date in the `definition.py` file:

    invoke shapefiles --base=boundaries/ocd-division/country:ca/province:qc/2011

Or, update all out-of-date shapefiles. The output may contain additional instructions:

    invoke shapefiles

Some shapefiles are online but require exceptional processing. Remember to update `last_updated` in `definition.py`:

    esri-dump http://geonb.snb.ca/ArcGIS/rest/services/GeoNB_ENB_MunicipalWards/MapServer/0 > boundaries/ca_nb_wards/wards.geojson
    ogr2ogr -f "ESRI Shapefile" boundaries/ca_nb_wards boundaries/ca_nb_wards/wards.geojson

After receiving a new boundary file for all municipalities in Quebec, you need to update the `definition.py` file in `ca_qc_districts`.

* Run `ruby boundaries/ca_qc_districts/sets.rb`
* Copy the output into the appropriate section of `qc/districts/definition.py`
* Comment out jurisdictions for which other sources have more complete data (Dorval, Kirkland)
* Separately define the boundaries of jurisdictions whose names duplicate others' (Plessisville (32045))
* After loading the boundaries into Represent, check La Tuque and Sept-Îles in particular.

#### Process shapefiles

Get information about the shapefile:

    ogrinfo -al -geom=NO boundaries/ocd-division/country:ca/province:qc/2011

Determine the attribute for the feature's name and, if it exists, the attribute for the feature's public identifier.

For features that are numbered like "Ward 1", if there is no attribute for the numeric identifier, we can extract it from the name, like `id_func=lambda f: re.sub(r'\D', '', f.get('WARD'))`. Similarly, if there is no attribute for the name, we can build it from the numeric identifier, like `name_func=lambda f: 'Ward %s' % f.get('WARD')`.

For features that aren't numbered like "Ward 1", determining the public identifier may be tricky: the ID should be discoverable online; no two features should have the same ID; and `OBJECTID` is never the ID.

Read [this section](https://github.com/opennorth/represent-boundaries/blob/master/definition.example.py#L51-L76) of the example `definition.py` file for help writing a `name_func` and `id_func`.

If you're updating many shapefiles, it may be long to run `ogrinfo` on each. Instead, run `../represent-canada/manage.py analyzeshapefiles -d . > manifest` and `git diff manifest` instead.

#### Cleanup

Fix file permissions:

    invoke permissions

Check if the data request process spreadsheet is out-of-date:

    invoke spreadsheet

Or less verbose:

    invoke spreadsheet --base=. --private-base=../represent-canada-private-data > /dev/null

#### Postcode concordances

Each data directory under [concordances/](concordances/) has a README explaining how to source and update its concordances. If the concordances are more than a year old and can't be sourced, they should be removed. To do so, substitute the corresponding values in the above READMEs for `<slug>` and `<source>`:

    fab ohoh update_concordances:args="<slug> <source> data/shapefiles/public/concordances/empty.csv"

#### Postcodes

Each data directory under [postcodes/](postcodes/) has a README explaining how to source and update its postcodes.

## Contact

Please use [GitHub Issues](https://github.com/opennorth/represent-canada-data/issues) for bug reports. You may also contact [represent@opennorth.ca](mailto:represent@opennorth.ca).

## Acknowledgements

We would like to express our gratitude to [Kent Mewhort](http://www.openissues.ca/) at the [Canadian Internet Policy and Public Interest Clinic (CIPPIC)](https://cippic.ca/), whose [legal research](https://cippic.ca/en/open_governance) ([PDF](https://cippic.ca/en/publications/how_to_redistribute_open_data)) made it possible for this repository to be made public.
