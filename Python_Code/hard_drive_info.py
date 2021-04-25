#!/usr/bin/env python3

import os
import collections
import re

def hard_drive_info(machine_name=""):
	'''
	This function will run stat on each file, read in the output, 
	and store the resulting data into a default dictionary collection.
	---------------------------------------------------------------------
	Inputs:
		machine_name     name of machine to check. 
							- default is current machine

	Output:
		data dict        collection dictionary holding machine data 
	---------------------------------------------------------------------
	'''
	# case for when a machine name is not given,
	# use the current machine name 

	data_dict = collections.defaultdict(dict)

	for files in os.listdir(os.getcwd()):
		# stats each file
		request_data = os.popen(f'stat {files}')
		file_data = request_data.read()
		size = file_data.split()[3]

		# adds the size to the dictionary
		data_dict[files] = size

	return data_dict
	
	
if __name__ == "__main__":
	# testing out the function	
	data = hard_drive_info()
	print(data)
