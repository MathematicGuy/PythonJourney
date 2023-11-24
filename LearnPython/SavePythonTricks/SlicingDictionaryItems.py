import itertools

''' Get items in range(start,[items], end) '''
student = {'RNo': 10, 'Marks': 90, 'Percentage': 90, 'Alice': 38738, 'Maja': 00, 'Guid':39}
print(len(student))
end = len(student)
new_dict = dict(itertools.islice(student.items(), 1, end))
print(new_dict)
