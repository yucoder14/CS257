import csv 

infile = open('statepath.csv','r')
outfile = open('main.html','w') 

reader = csv.reader(infile) 

outfile.write('<!DOCTYPE html>\n<html>\n<head>\n')
outfile.write('\t<link rel="stylesheet" type="text/css" href="styles.css">\n</head>\n<body>\n')
outfile.write('<svg viewbox="0 0 1000 589" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">\n')

for row in reader: 
	state_code = row[0]
	d_attribute = row[1] 
	
	outfile.write(f'\t<path id="{state_code}"\n\td="{d_attribute}"/>\n')  
 
outfile.write('</svg>\n') 
outfile.write('</body>\n')
outfile.write('</html>\n')
	
