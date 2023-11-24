import csv

users = [ {'name': 'Sol Masil', 'username': 'solm', 'department': 'IT'},
         {'name': 'Jacko', 'username': 'Mukka', 'department': 'Labor'},]
keys = ['name', 'username', 'department']
with open('../../by_department.csv', 'w') as by_department:
	writer = csv.DictWriter(by_department, fieldnames=keys)
	writer.writeheader() # write & set header in keys to csv file
	writer.writerows(users) # write each item in each dict

