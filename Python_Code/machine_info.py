#!/usr/bin/env python3

import os
import collections

def machine_info(machine_name="", sortby=""):
	
	# case for when a machine name is not given,
	# use the current machine name 

	data_dict = collections.defaultdict(dict)

	request_data = os.popen('ps aux')
	data = request_data.read()
	for line in data.splitlines()[1:]:
		
		line = line.split()

		USER    = line[0]
		PID     = line[1]
		CPU     = line[2]
		MEM     = line[3]
		STAT    = line[7]
		COMMAND = line[10]

		data_dict[COMMAND]["CPU"] = CPU
		data_dict[COMMAND]["MEM"] = MEM
		data_dict[COMMAND]["PID"] = PID
		data_dict[COMMAND]["STAT"] = STAT

		
	
	
if __name__ == "__main__":
	machine_info()
