####################################################################################
# @author: Anjaneyulu Reddy BEERAVALLI <anji.t6@gmail.com>
# @file: effacer.py
# @date: 28th April 2012
#
# This script deletes all the matched folders/files recursivey from the specified root directory
# Options:
#	-v: verbose - Show verbose mode
#	-h: help - Show help for using this script
#	-p: path - String next to `-p` is taken as the root path
# 	-m: match - A regular expression next to `-m` is taken as the expression
# 				to match files and directories
####################################################################################

import os, sys, argparse
	
def parseArguments():

	parser = argparse.ArgumentParser(description="Delete matched files/directories recursively from the specified root directory",
				epilog="To report any bugs email <anji.t6@gmail.com>",
				formatter_class=argparse.RawDescriptionHelpFormatter,
				conflict_handler='resolve')

	parser.add_argument('-p', '--path', nargs=1, default=os.getcwd(), dest='PATH',
		help='''Specify path to the root directory from which files/directories are to be deleted. (default: current working directory)''')
		
	parser.add_argument('-type', default='A', choices='AFD', dest='TYPE',
		help='''What to delete? A - delete both files and directories, F - delete ONLY files, D - delete ONLY directories. (default: 'A')''')
		 
	parser.add_argument('-version', '--version', action='version', version='%(prog)s 1.0') # print version number

	args = parser.parse_args()
	
	print args
	exit()
	
def main():
	parseArguments()

if __name__ == '__main__':
	main()