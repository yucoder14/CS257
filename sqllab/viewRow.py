import csv


def read_row(row_num): 
	with open('earthquakeDataModified.csv','r') as file: 
		reader = csv.reader(file)
		for index, row in enumerate(reader): 
			if index == row_num: 
				print(row)
				break 

x = input()
read_row(int(x))
