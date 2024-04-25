import csv 

with open('earthquakeData.csv','r') as infile, open('earthquakeDataModified.csv','w',newline='') as outfile: 
	reader = csv.reader(infile)
	writer = csv.writer(outfile)
	
	headers = next(reader) 
	for i in range(6):
		del headers[5] 

	del headers[6]	
	
	for i in range(7): 
		del headers[8] 


	writer.writerow(['date']+headers)


	for row in reader: 
		for i in range(6):
			del row[5] 
		
		del row[6]	
	
		for i in range(7): 
			del row[8] 
		
		raw_time = row[0].split("Z") 
		new_time = raw_time[0].split("T")
		new_time[0] = new_time[0].replace("/","-")
		formatted = new_time + row[1:]
	
		writer.writerow(formatted)	
		
