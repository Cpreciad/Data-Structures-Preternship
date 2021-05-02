#!/usr/bin/env python3

import os
import collections

def hard_drive_info(path=os.getcwd()):
	'''
	This function will run stat on each file, read in the output, 
	and store the resulting data into a default dictionary collection.
	---------------------------------------------------------------------
	Inputs:
		path						 starting path to check.
							- default is the current working directory
	Output:
		data dict        collection dictionary holding machine data 
	---------------------------------------------------------------------
	'''
	# Initializes dictionary
	data_dict = collections.defaultdict(dict)
	for files in os.listdir(path):
		# Sets the current full path
		currPath = os.path.join(path,files)

		# If entry is a file, it will stat it
		if(os.path.isfile(currPath)):
			request_data = os.popen(f'stat {currPath}')
			file_data = request_data.read()
			size = file_data.split()[3]

			# adds the size to the dictionary
			data_dict[currPath] = size

		# If entry is a directory, it will enter it recursively
		elif (os.path.isdir(currPath)):
			data_dict.update(hard_drive_info(currPath))

	return data_dict

if __name__ == "__main__":
	# testing out the function
	data = hard_drive_info()
	print(data)
