import sys
import codeforces
import os

def get_arg_value(arg, arguments):
	arg = "--" + arg

	for i in xrange(len(arguments)):
		if arguments[i] == arg:
			if i+1 >= len(arguments):
				return None
			return arguments[i+1]

	return None

# Getting the arguments.
arguments = sys.argv[1:]

#link = get_arg_value("link", arguments)
#code = get_arg_value("code", arguments)

input_list, output_list = codeforces.get_input_output(arguments[0])
os.system("g++ ../CP/code.cpp -std=c++11")

