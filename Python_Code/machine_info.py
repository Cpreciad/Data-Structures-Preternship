#!/usr/bin/env python3

import os
import collections

def machine_info(machine_name="", sortby="CPU"):
	'''
	This function will run ps aux externally, read in the output, 
	and store the resulting data into a default dictionary collection.
	'''
	# case for when a machine name is not given,
	# use the current machine name 

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
		if CPU != '0.0':
			print(CPU)
			continue

		data_dict[COMMAND]["CPU"] = CPU
		data_dict[COMMAND]["MEM"] = MEM
		data_dict[COMMAND]["PID"] = PID
		data_dict[COMMAND]["STAT"] = STAT

		
	
	
if __name__ == "__main__":
	machine_info()
