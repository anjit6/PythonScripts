#################################################################################################
# @author: Anjaneyulu Reddy BEERAVALLI <anji.t6@gmail.com>
# @file: effacer.py
# @date: 29th April 2012
#
# This script deletes all the matched folders/files recursivey from the specified root directory
# Options:
#	-v: verbose - Show verbose mode
#	-h/--help: help - Show help for using this script
#	-p/--p: path - String next to `-p` is taken as the root path
# 	-e/--expression: pattern - A regular expression next to `-e` is taken as the expression
# 				to match files and directories
#################################################################################################	

import os, sys, argparse, re, shutil
from types import *

def show_invalid_exp_msg():
	print '''Please enter a valid pattern. Example: r'\*.php$' - find files ending with `.php`'''
	exit()
	
def print_verbose(args, single_file):
	if (args['VERBOSE'] == True):
		print "found match at " + single_file + '... deleted'

def delete_recursively(args):

	files_list = []
	single_file = ''
	
	args['PATH'] = args['PATH'][0] if isinstance(args['PATH'], ListType) else args['PATH']
	args['PATTERN'] = args['PATTERN'][0] if isinstance(args['PATTERN'], ListType) else args['PATTERN']

	for root, dirs, names in os.walk(args['PATH']):
		
		if (args['TYPE'] == 'F' or args['TYPE'] == 'A'):

			for name in names:
				try:
					search_result = re.search(args['PATTERN'], name)
				except:
					show_invalid_exp_msg()

				if (search_result is not None):
					files_list.append(root + '/' + name)

		if (args['TYPE'] == 'D' or args['TYPE'] == 'A'):

			try:
				search_result = re.search(args['PATTERN'], root)
			except:
				show_invalid_exp_msg()
				
			if (search_result is not None):
				files_list.append(root)
	
	for single_file in files_list:
	
		if (args['TYPE'] == 'F'):
			if (os.path.isdir(single_file) == False):
				try:
					with open(single_file) as f:
						os.remove(single_file)
						print_verbose(args, single_file)
				except IOError as e:
					print_verbose(args, single_file)
					# do nothing here
		
		elif (args['TYPE'] == 'D'):
			if (os.path.isdir(single_file) == True):
				shutil.rmtree(single_file, True)
				print_verbose(args, single_file)

		else:
			if (os.path.isdir(single_file) == True):
				shutil.rmtree(single_file, True)
			else:
				try:
					with open(single_file) as f:
						os.remove(single_file)
						print_verbose(args, single_file)
				except IOError as e:
					print_verbose(args, single_file)
					 
	exit()
	
def parse_arguments():

	parser = argparse.ArgumentParser(
				description='''Delete matched files/directories recursively from the specified root directory.
**NOTE**: If path and expression are not mentioned, all the files and sub-directories in the
	  current working directory will be deleted.''',
				epilog="To report any bugs email <anji.t6@gmail.com>",
				formatter_class=argparse.RawDescriptionHelpFormatter,
				conflict_handler='resolve')

	parser.add_argument('-p', '--path', nargs=1, default=os.getcwd(), dest='PATH', required=True,
		help='''Specify path to the root directory from which files/directories are to be deleted. This option is mandatory ''')

	parser.add_argument('-e', '--expression', nargs=1, required=True, default='*', dest='PATTERN',
		help='''Specify regular expression to match target file/directory to be deleted. By default any given file/folder is deleted. Example: r'\*.php$' - find files ending with `.php`''')
					
	parser.add_argument('-type', default='A', choices='AFD', dest='TYPE',
		help='''What to delete? A - delete both files and directories, F - delete ONLY files, D - delete ONLY directories. (default: 'A')''')

	parser.add_argument('-v', '--verbose', dest='VERBOSE', default=False, action='store_true', help='Verbose mode')
				 
	parser.add_argument('-version', '--version', action='version', version='%(prog)s v1.0') # print version number

	args = vars(parser.parse_args()) # convert default Namespace object to dictionary

	delete_recursively(args)
	exit()

def main():
	parse_arguments()

if __name__ == '__main__':
	main()