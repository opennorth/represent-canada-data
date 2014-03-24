require 'csv'
require 'open-uri'

require 'dbf'

names = {}
CSV.parse(open('https://raw.githubusercontent.com/opencivicdata/ocd-division-ids/master/identifiers/country-ca/ca_census_subdivisions.csv').read) do |id,name,name_fr,classification,organization_name|
  type_id = id[/[^:]+\z/]
  if type_id[0, 2] == "24"
    names[type_id[2, 5].to_i] = name
  end
end

DBF::Table.new('Districts Elec Mun 2014-02-28_DetU_region.dbf').each do |record|
  unless record['CO_DESIGN'] == 'RI'
    puts %(    '#{record['CO_MUNCP']}': [u"#{names[record['CO_MUNCP']]}", u"#{record['MODE_SUFRG'] == 'Q' ? 'quartiers' : 'districts'}"],)
  end
end
