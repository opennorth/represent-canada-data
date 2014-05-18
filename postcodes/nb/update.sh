in2csv --no-inference --sheet "All PCs" "Postal Codes per PED_Aug_29_2012.xlsx" | csvcut -c 2,1 | sed 's/ //' | sed 's/\.0//' | tail +2 > one.csv
in2csv --no-inference --sheet "Duplicate PCs" "Postal Codes per PED_Aug_29_2012.xlsx" | sed 's/ //' | sed 's/\.0//' > two.csv
csvstack one.csv two.csv > out.csv
rm -f one.csv two.csv
