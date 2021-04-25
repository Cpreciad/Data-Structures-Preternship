#!/usr/bin/env python3

import os
import collections

# Set of desired fields present in /proc/meminfo
DESIRED_FIELDS = ('MemTotal', 'MemFree', 'MemAvailable', 
									'Buffers', 'Cached', 'SwapTotal', 'SwapFree', 
									'VmallocTotal', 'VmallocUsed', 'VmallocChunk')

def memory_info():
		''' Uses the /proc/meminfo file to report information about the current Linux machine '''

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
	mem_info = memory_info()
	print(mem_info)
	print(f"Percent of memory free: {mem_info['MemPercentFree']:0.2f} %")
	print(f"Percent of memory available: {mem_info['MemPercentAvailable']:0.2f} %")
	print(f"Percent of swap memory free: {mem_info['SwapPercentFree']:0.2f} %")
