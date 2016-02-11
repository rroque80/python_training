#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
import subprocess

'''
This module helps to test network connectivity.

Ping a list  of ip addresses, in order, to determine access.
This module also will help test connectivity to Messenger servers.
Credits: Reggie/Nathan

'''

crazy_variable = 10000000
b = 2

if (1 == crazy_variable):
	print ("hello world")
if (1 == b):
	print ("I shouldn't print")
else:
	print ("It didn't print")

my_command = subprocess.call(['ls', '-a'])

iplist = ['192.168.1.20', '10.0.0.1', 'google.com']

def iptest():
    '''Test ip addresses from a previously defined list and display results'''
    for ip in iplist:
        print (ip)
        subprocess.call(['ping', '-c', '10', ip])
