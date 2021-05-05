#!/usr/bin/env python3

import sys
import os

def usage(status=0):
	# By default, the program returns the hard drive usage, cpu usage, and memory

	progname = os.path.basename(sys.argv[0])
	print(f'''Usage: {progname} [options]		

	-m MACHINE		Which machine to check (default: current machine)
	-H						Do not include hard drive usage
	-C						Do not include cpu usage
	-R						Do not include memory usage
	-s SORTBY			Field to sort information by (default: cpu usage)
	''')
	sys.exit(status)
