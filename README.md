# Represent API: Data

[Represent](http://represent.opennorth.ca) is the open database of Canadian elected officials and electoral districts. It provides a [REST API](http://represent.opennorth.ca/api/) to boundary, representative, and postcode resources.

This repository stores the digital boundary files for the database. The [represent-canada](http://github.com/opennorth/represent-canada) repository is what's running at [represent.opennorth.ca](http://represent.opennorth.ca/).

## License

Open North has permission to redistribute all datasets in this repository. Please read the [overall license](http://github.com/opennorth/represent-canada-data/tree/master/LICENSE.txt) and the `LICENSE.txt` file in each directory to know your rights. In some cases, you will not have permission to redistribute the dataset.

## Data Quality

### Lineage

All datasets are from government sources, with one exception: the postal code dataset in the `postcodes/fed` directory is from [Geocoder.ca](http://geocoder.ca/). ([Canada Post has sued Geocoder.ca](http://geocoder.ca/?sued=1) for distributing this file.) The `definition.py` files will have more details on sources and any modifications made to the files.

### Completeness

We do not have permission to redistribute every dataset available through the [Represent API](http://represent.opennorth.ca/api/). Specifically, we do not have permission from the Government of Ontario to distribute its [boundary file](http://www.elections.on.ca/en-CA/Tools/ElectoralDistricts/Shapefile.htm) and [postal code concordance file](http://www.elections.on.ca/en-CA/Tools/ElectoralDistricts/PostalCodeFile.htm). You must download these files separately from Elections Ontario. You may then use the `definition.py` file we provide to load it into the database.

## Contributing

[We need the ward boundaries](https://github.com/opennorth/represent-canada/issues/13) for more municipalities. Please [let us know](mailto:represent@opennorth.ca) if you have a ward boundary file. To go one step further, you can write a `definition.py` file to describe the data, using an [example `definition.py` file](http://github.com/opennorth/represent-canada-data/tree/master/examples/definition.example.comments.py).

## Contact

Please use [GitHub Issues](http://github.com/opennorth/represent-data/issues) for bug reports. You may also contact [represent@opennorth.ca](mailto:represent@opennorth.ca).

## Acknowledgements

We would like to express our gratitude to [Kent Mewhort](http://www.openissues.ca/) at the [Canadian Internet Policy and Public Interest Clinic (CIPPIC)](http://www.cippic.ca/), whose [legal research](http://www.cippic.ca/en/open-licensing) ([PDF](http://www.cippic.ca/sites/default/files/CIPPIC%20-%20How%20to%20Redistribute%20Open%20Data.pdf)) made it possible for this repository to be made public.
