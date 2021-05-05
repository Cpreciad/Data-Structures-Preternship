#!/usr/bin/env python3

# Imports
import argparse
import json
import os
import sys

from datetime import datetime

import data_collector

TAB = ' '*8
PROCESS_INFO = ('CPU', 'MEM')


def get_args_from_user():
	''' Implements arguments parsing '''

	# Set up argparse object and print description as well as link to project proposal
	parser = argparse.ArgumentParser(description= 'Google Preternship Project\n \
		Carlo Preciado, Sam Neus\n \
		Connor Shields, Facundo Munoz\n',
		formatter_class = argparse.RawTextHelpFormatter,
		epilog= 'For more information, see: https://yld.me/PUz')

	# Optional Arguments
	parser.add_argument('-H', help='Do not include hard drive usage. Default false.', action='store_true')
	parser.add_argument('-C', help='Do not include CPU usage. Default false.', action='store_true')
	parser.add_argument('-M', help='Do not include memory usage. Default false.', action='store_true')
	parser.add_argument('-d', help='Store in a directory. Usage: {-d directory}')
	parser.add_argument('-s', help='Do not print out the information. Default false', action='store_true')

	# Parse arguments and return as mamespace object
	args = parser.parse_args()
	verify_args(args)
	return args


def verify_args(args):
	''' Checks for errors with user argument specifications '''

	if args.H and args.C and args.M:
		sys.exit("Cannot omit all 3 options: hard drive usage, CPU usage, memory usage")


def print_separator(processes, char = '='):
	''' Prints a row of separator characters'''

	for process in processes:
		print(char*8, end='')
	print(char*8, end='')

	print('')


def print_processes(data_dict):
	''' Prints the header of the table, using PIDs '''

	print('PID ', end='')
	for process in data_dict:
		print(f'{data_dict[process]["PID"]:>8}', end='')
	print('')


def print_fields(data_dict, fields = PROCESS_INFO, sortby = "CPU"):
	''' Prints fields for the table '''
	
	for field in fields:
		print(f'{field:>4}', end='') 
		for process in data_dict:
			print(f'{data_dict[process][field]:>8}', end='')
		print('')	


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
			json.dump(data_dict, output_file, indent=2)


def get_time_str():
	''' Helper function to return a formatted string representing the time. '''
	dt_string = datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
	return dt_string

if __name__ == "__main__":
	''' 
	Main driver for program to analyzing Linux machine's state.
	
	Gathers, parses, and prints data regarding hard drive usage,
	CPU usage, and memory available on machine depending on user-
	specified flags.
	'''

	# Get args from user
	args = get_args_from_user()

	# Obtain needed data
	hard_drive_data = data_collector.hard_drive_info(".")
	hard_drive_data = dict( sorted(hard_drive_data.items(), key=lambda h: int(h[1]), reverse = True) )

	cpu_data = data_collector.cpu_mem_info()
	memory_data = data_collector.memory_info()

	# Display data depending on flags
  # Do not print if silent flag is called
	if not args.s:
		if not args.H:
			print('Hard Drive Info')
			print('-----------------------------')
			for file_name, file_size in dict(hard_drive_data).items():
				print(f'{file_name}: {file_size} bytes')
			print('\n')

		if not args.C:
			print('CPU Info')
			print_separator(cpu_data.keys(), '-')
			print_processes(cpu_data)
			print_separator(cpu_data.keys(), '=')
			print_fields(cpu_data);
			print('\n')

		if not args.M:
			print('Memory Info')
			print('-------------------------')
			print(f"Percent of memory free: {memory_data['MemPercentFree']:0.2f} %")
			print(f"Percent of memory available: {memory_data['MemPercentAvailable']:0.2f} %")
			print(f"Percent of swap memory free: {memory_data['SwapPercentFree']:0.2f} %")	
			print('\n')

	# Output directory depending on flag
	if args.d:
		names_to_datadicts = {}
		if not args.H:
			names_to_datadicts['Hard_Drive_Info'] = hard_drive_data
		if not args.C:
			names_to_datadicts['CPU_Info'] = cpu_data
		if not args.M:
			names_to_datadicts['Memory_Info'] = memory_data

		generate_directory(args.d, names_to_datadicts)
