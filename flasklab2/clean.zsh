
##little zsh script to extract state codes and corresponding d attribute for defining the path in SVG 

cat us.svg |				#print us.svg 
grep -E "data-id=" -A 1 |	#find lines with state codes and print 1 line after 
sed 's/--//g' |				#rm '--' marker created by grep 
sed 's/^[ \t]*//'|  		#rm white space in front of line
sed 's/data-id=//' |		#rm 'data-id=' from relevant lines 
tr '\n' '|' |				#replace all new lines with | as a delimiter 
sed 's/|d=/,/g' |			#replace all instances of |d= with a comma 
tr '|' '\n' |				#replace delimiters with newlines 
awk NF > statepath.csv		#print only lines that has characters and export as statepath.csv
