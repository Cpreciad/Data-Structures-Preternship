#!/usr/bin/env python3

import os
import collections

# Set of desired fields present in /proc/meminfo
DESIRED_FIELDS = ('MemTotal', 'MemFree', 'MemAvailable', 
									'Buffers', 'Cached', 'SwapTotal', 'SwapFree', 
									'VmallocTotal', 'VmallocUsed', 'VmallocChunk')

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
	

	# Deletes the smallest items if the dictionary gets too big
	while (len(data_dict) > 30):
		del data_dict[( min(data_dict.items(), key = lambda k: int(k[1])) )[0]]

	return data_dict


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


def memory_info():
		''' 
		Uses the /proc/meminfo file to report information about the current Linux machine.
		
		Opens the /proc/meminfo file, which contains information about the file system: 
		https://man7.org/linux/man-pages/man5/proc.5.html. Selected fields provide a
		snapshot of the current memory state of the Linux machine.
		'''

		mem_info = collections.defaultdict()

		# Process output of /proc/meminfo
		for line in open('/proc/meminfo'):
			field = line.split(':')[0].strip()
			value = line.split(':')[1].strip()[:-3] # get rid of units as all are in kB
			
			if field in DESIRED_FIELDS: 
				mem_info[field] = value

		# Parse output to create new fields and analyses
		mem_info['MemPercentFree'] = int(mem_info['MemFree']) / int(mem_info['MemTotal']) * 100
		mem_info['MemPercentAvailable'] = int(mem_info['MemAvailable']) / int(mem_info['MemTotal']) * 100
		mem_info['SwapPercentFree'] = int(mem_info['SwapFree']) / int(mem_info['SwapTotal']) * 100

		return dict(mem_info)
		

if __name__ == "__main__":
	# testing out hard_drive_info
	data = hard_drive_info()
	print(data)

	# testing out cpu_mem_info
	data_dict = cpu_mem_info()
	for data in data_dict:
		print(f'process: {data}' )
		print(f'cpu usage: {data_dict[data]["CPU"]}')
		print(f'mem usage: {data_dict[data]["MEM"]}\n')
	
	# testing out mem_info
	mem_info = memory_info()
	print(mem_info)
	print(f"Percent of memory free: {mem_info['MemPercentFree']:0.2f} %")
	print(f"Percent of memory available: {mem_info['MemPercentAvailable']:0.2f} %")
	print(f"Percent of swap memory free: {mem_info['SwapPercentFree']:0.2f} %")
