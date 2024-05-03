#original attempt was to use python to write out html file...not ideal


import csv 

infile = open('statepath.csv','r')
outfile = open('index.html','w') 

reader = csv.reader(infile) 

outfile.write('<!DOCTYPE html>\n<html>\n<head>\n')
outfile.write('<link rel="stylesheet" type="text/css" href="{{ url_for(\'static\',filename=\'style/styleMain.css\') }}">\n')

outfile.write('<svg viewbox="0 0 1000 589" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\n')

for row in reader: 
	state_code = row[0]
	d_attribute = row[1] 
	
	outfile.write(f'\t<path id="{state_code}"\n\td="{d_attribute}"/>\n')  

outfile.write('</svg>\n') 
outfile.write('<script src="{{ url_for(\'static\',filename=\'script/scriptMain.css\')}}"></script>\n')
outfile.write('</body>\n')
outfile.write('</html>\n')

outfile.close()
