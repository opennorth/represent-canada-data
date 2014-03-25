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

sets = {}

DBF::Table.new(File.expand_path('Districts Elec Mun 2014-02-28_DetU_region.dbf', __dir__)).each do |record|
  if %w(ÉI RI).include?(record['CO_DESIGN'].force_encoding('iso-8859-1').encode('utf-8'))
    sets[record['CO_MUNCP']] = record['MODE_SUFRG']
  end
end

sets.each do |k,v|
  puts %(    #{k}: [u"#{names[k]}", u"#{v == 'Q' ? 'quartiers' : 'districts'}"],)
end
