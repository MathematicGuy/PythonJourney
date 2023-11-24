import csv
''' CSV: Sort Variable by ROW '''
with open('../NguyenBui.txt') as f:
	f.readline()
	csv_F = csv.reader(f) # instead of read()
	for row in csv_F:
		print()
		print(row)
		# # name, phone, field = row # take content from row for ech Comma
		print('Name: {} - Status: {}'.format(row[0], row[2]))




import csv

def read_employees(csv_file_location):
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        employee_file = csv.DictReader(open(csv_file_location), dialect='empDialect')

        employee_list = []
        for data in employee_file:
                employee_list.append(data)
        return employee_list


employee_list = read_employees('/home/student-00-ea72615385e0/data/employees.cs')
print(employee_list)




