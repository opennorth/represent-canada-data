curl -s -O https://www.electionsquebec.qc.ca/documents/zip/CP_CIRC_MUN_MRC_RA_BRUT.zip
unzip -o -q CP_CIRC_MUN_MRC_RA_BRUT.zip
rm -f CP_CIRC_MUN_MRC_RA_BRUT.zip
export TMP=$LANG
export LC_CTYPE=en_CA.ISO8859-1
cut -d ";" -f 1-2 CP_CIRC_MUN_MRC_RA_BRUT.txt | tail +2 | uniq | sed 's/;/,/' > out.csv
export LC_CTYPE=$TMP
unset TMP
rm -f CP_CIRC_MUN_MRC_RA_BRUT.txt
