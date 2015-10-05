in2csv Electoral.Postal.Codes.Jan.2012.xls | csvcut -c 2,1 | sed 's/WINDSOR-BUCHANS/WINDSOR\/BUCHANS/' | tail +2 > out.csv
