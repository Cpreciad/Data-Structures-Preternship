#!/usr/bin/env python3

# Imports
import argument_parser
import directory_output
import hard_drive_info
import machine_info
import mem_info
import print_info

if __name__ == "__main__":
	''' 
	Main driver for program to analyzing Linux machine's state.
	
	Gathers, parses, and prints data regarding hard drive usage,
	CPU usage, and memory available on machine depending on user-
	specified flags.
	'''

	# Get args from user
	argp = argument_parser.ArgumentParser()
	args = argp.get_args_from_user()

	# Obtain needed data
	hard_drive_data = hard_drive_info.hard_drive_info(".")
	cpu_data = machine_info.cpu_mem_info()
	memory_data = mem_info.memory_info()

	# Display data depending on flags
  # Do not print if silent flag is called
	if not args.s:
	  if not args.H:
		  print('Displaying hard drive info...')
		  print('-----------------------------')
		  for fname, fsize in dict(hard_drive_data).items():
			  print(f'{fname}: {fsize} bytes')
		  print('\n')

	  if not args.C:
		  print('Displaying CPU info...')
		  print_info.print_separator(cpu_data.keys(), '-')
		  print_info.print_processes(cpu_data)
		  print_info.print_separator(cpu_data.keys(), '=')
		  print_info.print_fields(cpu_data);
		  print('\n')

	  if not args.M:
		  print('Displaying memory info...')
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

		directory_output.generate_directory(args.d, names_to_datadicts)
