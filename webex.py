#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
import subprocess

crazy_variable = 10000000
b = 2

if (1 == crazy_variable):
	print ("hello world")
if (1 == b):
	print ("I shouldn't print")
else:
	print ("It didn't print")

my_command = subprocess.call(['ls', '-a'])
