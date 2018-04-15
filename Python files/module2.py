#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      matthewl9
#
# Created:     07/03/2018
# Copyright:   (c) matthewl9 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import socket
import os
import sys
import platform
#import meminfo
import psutil
import uuid

def main():
	print ("Name: " +socket.gethostname())
	print ("FQDN: " +socket.getfqdn())
	print ("System Platform: "+sys.platform)
	print ("Machine: " +platform.machine())
	print ("Node " +platform.node())
	print ("Platform: "+platform.platform())
	print ("Processor: " +platform.processor())
	print ("System OS: "+platform.system())
	print ("Release: " +platform.release())
	print ("Version: " +platform.version())
	print ("Number of CPUs: " +str(psutil.cpu_count()) )
	print ("Number of Physical CPUs: " +str(psutil.cpu_count(logical=False)))
	mem = psutil.virtual_memory()
	print(mem.total)
if __name__ == '__main__':
    main()
