#!/usr/bin/env python3

import argparse
import os
import sys

class ArgumentParser:
	''' Class to parse user command line arguments '''

	def get_args_from_user(self):
		''' Implements arguments parsing '''

		# Set up argparse object and print description as well as link to project proposal
		parser = argparse.ArgumentParser(description= 'Google Preternship Project\n'
																									'Carlo Preciado, Sam Neus\n'
																									'Connor Shields, Facundo Munoz\n',
																		formatter_class = argparse.RawTextHelpFormatter,
																		epilog= 'For more information, see: https://yld.me/PUz')

		# Optional Arguments
		parser.add_argument('-m', help='Which machine to check (default: current machine)')
		parser.add_argument('-H', help='Do not include hard drive usage. Default false.', action='store_true')
		parser.add_argument('-C', help='Do not include CPU usage. Default false.', action='store_true')
		parser.add_argument('-R', help='Do not include memory usage. Default false.', action='store_true')
		parser.add_argument('-S', help='Field to sort by (default: CPU usage)')

		# Parse arguments and return as mamespace object
		args = parser.parse_args()
		self.verify_args(args)
		return args

	def verify_args(self, args):
		''' Checks for errors with user argument specifications '''

		if args.H and args.C and args.R:
			sys.exit("Cannot omit all 3 options: hard drive usage, CPU usage, memory usage")

