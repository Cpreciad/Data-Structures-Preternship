#!/usr/bin/env python3

# Imports
import json
import os
from datetime import datetime

def generate_directory(dir_name, names_to_datadicts):
	''' 
	Generates a directory with the given dir_name or adds to it if it exists.
	
	Creates a directory which contains .json files for each dict in the input data_dicts.
	Inputs: 
		dir_name: the name of the directory for the files to be placed in
		names_to_datadicts: a dictionary mapping a name to each dictionary to be outputted.
	'''

	# Check if directory does not exist, create one if this is the case
	if not os.path.exists(dir_name):
		os.mkdir(dir_name)

	# Loop through names_to_datadicts, create a file path for each one
	for name, data_dict in names_to_datadicts.items():
		file_name = f'{name}_{get_time_str()}'
		file_path = os.path.join(dir_name, file_name + '.json')

		# Dump dictionary to json file
		with open(file_path, 'w') as output_file:
			json.dump(data_dict, output_file)

def get_time_str():
	''' Helper function to return a formatted string representing the time. '''
	dt_string = datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
	return dt_string

if __name__ == '__main__':
	dict_test= {'meminfo':{'key1':'val1'}, 'cpuinfo':{'key2':'val2'}}
	generate_directory('test_dir', dict_test)
