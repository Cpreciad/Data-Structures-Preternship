#!/usr/bin/env python3

import os
import collections

def cpu_mem_info(sortby="CPU"):
	'''
	This function will run ps aux externally, read in the output, 
	and store the resulting data into a default dictionary collection.
	---------------------------------------------------------------------
	Inputs:
		machine_name     name of machine to check. 
							- default is current machine

		sortby           parameter to prioritize when sorting. 
							- default is CPU
	Output:
		data dict        collection dictionary holding machine data 
	---------------------------------------------------------------------
	'''

	data_dict = collections.defaultdict(dict)

	request_data = os.popen('ps aux')
	
	data = request_data.read()
	for line in data.splitlines()[1:]:
	
		# if the specified sorting field is 0, add it to the list

		line = line.split()

		USER    = line[0]
		PID     = line[1]
		CPU     = line[2]
		MEM     = line[3]
		STAT    = line[7]
		COMMAND = line[10]
	
		# if the prioritized statistic is zero, skip it
		# this will keep the data being stored only relavent to what the user wants
		if MEM == "0.0" and CPU == '0.0':
			continue
		

		data_dict[COMMAND]["CPU"] = CPU
		data_dict[COMMAND]["MEM"] = MEM
		data_dict[COMMAND]["PID"] = PID
		data_dict[COMMAND]["STAT"] = STAT
	
	# sort the dictionaries with respect to prioritizing cpu
	data_dict = dict(sorted(data_dict.items(), key = lambda p: float(p[1]["MEM"]), reverse = True))
	data_dict = dict(sorted(data_dict.items(), key = lambda p: float(p[1]["CPU"]), reverse = True))

	return data_dict
	
	
if __name__ == "__main__":
	# testing out the function	
	data_dict = cpu_mem_info()
	
	for data in data_dict:
		print(f'process: {data}' )
		print(f'cpu usage: {data_dict[data]["CPU"]}')
		print(f'mem usage: {data_dict[data]["MEM"]}\n')
