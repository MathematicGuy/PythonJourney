import csv

# be careful with blank space in dictionary "name" != "name "
with open('../solfware.csv', 'r') as file:
	content = csv.reader(file)
	for row in content:
		print("Name: {} - Status: {}".format(row[0], row[1]))

