import json

classroom = {}


class Student:

	def __init__(self, name, gpa):
		self.name = name
		self.gpa = gpa

	def __repr__(self):
		return f'{self.name}, \n {self.gpa}'

add_more_student = True

while add_more_student:
	check_student_info = True
	while check_student_info:
		student_id = input('Student ID: ')
		student_name = input('Student name: ')
		student_gpa = float(input('Student gpa: '))  # highest value: 5.0

		if 'bit' == student_id[:3].lower() and len(student_id[3:]) == 6:
			student = Student(student_name, student_gpa)
			classroom[student_id] = student
			with open('Classinfo.txt', 'a') as class_file:  # not optimized
				for ID in classroom:
					class_file.write(json.dumps(ID))
					print()
					class_file.write(json.dumps(repr(classroom[ID])))

			check_student_info = False
		else:
			print('Invalid id, retype')
			print()

	make_choice = True
	while make_choice:
		choice = input('Add more student, type yes or no: ').lower()

		if choice == 'no':
			add_more_student = False
			make_choice = False
			for student in classroom:
				print('\nMã sinh viên: {}'.format(student.upper()))
				print('Họ và Tên: {}'.format(classroom[student].name.capitalize()))
				print('Ngày sinh: {}'.format(classroom[student].gpa))


		elif choice == 'yes':
			continue
		else:
			print('Invalid, pls enter again')
