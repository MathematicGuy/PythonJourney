import os
import datetime


def file_time(directory, da_file):
	if not os.path.isdir(directory):
		os.mkdir(directory)

	mtime = os.path.getmtime(directory)
	times = datetime.datetime.fromtimestamp(mtime)
	time = times.date()
	# y = times.year
	# m = times.month
	# d = times.day

	os.chdir(directory)  # Using chdir to redirect created file into the directed directory
	with open(da_file, 'w'):
		pass

	print('{} was created in {}'.format(directory, time))
	path = ''
	print(os.listdir())

file_time('Room', 'NguyenBui.txt')


''' Delete all empty sub_dir '''
# import os
#
# def remove_subdirs(main_dir):
#     for root, dirs, files in os.walk(main_dir, topdown=False):
#         for dir in dirs:
#             os.rmdir(os.path.join(root, dir))

''' Remove all dir and file. Warning: create a current directory's copy for your own good '''
# import shutil
#
# def remove_dir(dir_path):
#     shutil.rmtree(dir_path)
