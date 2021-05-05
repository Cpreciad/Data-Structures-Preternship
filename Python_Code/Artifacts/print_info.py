#!/usr/bin/env python3
import machine_info
import re

TAB = ' '*8
PROCESS_INFO = ('CPU', 'MEM')

def print_separator(processes, char = '='):
	
	# Prints a row of separator characters
	for process in processes:
		print(char*8, end='')
	print(char*8, end='')

	print('')


def print_processes(data_dict):
	
	# prints the header of the table
	# will be the PID for now

	print('PID ', end='')
	for process in data_dict:
		print(f'{data_dict[process]["PID"]:>8}', end='')
	print('')


def print_fields(data_dict, fields = PROCESS_INFO, sortby = "CPU"):
	
	for field in fields:
		print(f'{field:>4}', end='') 
		for process in data_dict:
			print(f'{data_dict[process][field]:>8}', end='')
		print('')	


if __name__ == "__main__":
	data = machine_info.cpu_mem_info()
	
	print_processes(data)

	print_separator(data.keys(), '=')
	print_fields(data);
