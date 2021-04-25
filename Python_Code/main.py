#!/usr/bin/env python3

#imports
import argument_parser
import machine_info

#calling arg parser function
argp = argument_parser.ArgumentParser()
args = argp.get_args_from_user()

#obtain cpu memory unless user specified not to
if not args[C]:
    cpu_data = machine_info.cpu_mem_info()

    #print cpu data
    for data in cpu_data:
		print(f'process: {data}' )
		print(f'cpu usage: {cpu_data[data]["CPU"]}')
		print(f'mem usage: {cpu_data[data]["MEM"]}\n')
