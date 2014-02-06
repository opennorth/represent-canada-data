# Represent API: Data

[Represent](http://represent.opennorth.ca) is the open database of Canadian elected officials and electoral districts. It provides a [REST API](http://represent.opennorth.ca/api/) to boundary, representative, and postcode resources.

This repository stores the digital boundary files for the database. The [represent-canada](http://github.com/opennorth/represent-canada) repository is what's running at [represent.opennorth.ca](http://represent.opennorth.ca/).

## License

Open North has permission to redistribute all datasets in this repository. Please read the [overall license](http://github.com/opennorth/represent-canada-data/tree/master/LICENSE.txt) and the `LICENSE.txt` file in each directory to know your rights. In some cases, you will not have permission to redistribute the dataset.

## Data Quality

### Lineage

All datasets are from government sources, with one exception: the postal code<sup>OM</sup> dataset in the `postcodes/fed` directory is from [Geocoder.ca](http://geocoder.ca/). ([Canada Post has sued Geocoder.ca](http://geocoder.ca/?sued=1) for distributing this file.) The `definition.py` files will have more details on sources and any modifications made to the files. Postal Code<sup>OM</sup> is an official mark of Canada Post Corporation.

### Completeness

We do not have permission to redistribute every dataset available through the [Represent API](http://represent.opennorth.ca/api/). For example, we do not have permission from the Government of Ontario to distribute its [boundary file](http://www.elections.on.ca/en-CA/Tools/ElectoralDistricts/Shapefile.htm) and [postal code<sup>OM</sup> concordance file](http://www.elections.on.ca/en-CA/Tools/ElectoralDistricts/PostalCodeFile.htm) (no longer available). You must download these files separately from Elections Ontario. You may then use the `definition.py` file we provide to load it into the database.

## Contributing

[We need the ward boundaries](https://github.com/opennorth/represent-canada/issues/13) for more municipalities. Please [let us know](mailto:represent@opennorth.ca) if you have a ward boundary file. To go one step further, you can write a `definition.py` file to describe the data, using the [example](https://github.com/rhymeswithcycle/represent-boundaries/blob/master/definition.example.py) `definition.py` file.

## Maintenance

### One-time setup

    # Invoke must not be installed globally.
    pip uninstall invoke
    # Create a virtual environment.
    mkvirtualenv representdata
    # Install the requirements.
    pip install -r requirements.txt

### Regular tasks

Load the virtual environment:

    workon representdata

#### Boundaries

Check that all data directories contain a `LICENSE.txt`:

    invoke licenses

Check that all `definition.py` files are valid:

    invoke definitions

Check that the source, data and license URLs work:

    invoke urls

Update any out-of-date shapefiles:

    invoke shapefiles

File file permissions:

    invoke permissions

Tidy Python:

    autopep8 -i -a -r --ignore=E111,E121,E124,E128,E501,W6 .

## Contact

Please use [GitHub Issues](http://github.com/opennorth/represent-canada-data/issues) for bug reports. You may also contact [represent@opennorth.ca](mailto:represent@opennorth.ca).

## Acknowledgements

We would like to express our gratitude to [Kent Mewhort](http://www.openissues.ca/) at the [Canadian Internet Policy and Public Interest Clinic (CIPPIC)](http://www.cippic.ca/), whose [legal research](http://www.cippic.ca/en/open-licensing) ([PDF](http://www.cippic.ca/sites/default/files/CIPPIC%20-%20How%20to%20Redistribute%20Open%20Data.pdf)) made it possible for this repository to be made public.
