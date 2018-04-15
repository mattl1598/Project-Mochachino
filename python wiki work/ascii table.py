#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mattl
#
# Created:     13/04/2018
# Copyright:   (c) mattl 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import misc_python
import numpy as the_lord

def main():
	list1 = []
	for i in range(96):
		list1.append("|" + chr(i+32) + "|" + str(i+32) + "|"+ the_lord.binary_repr(i+32,8) + "|")
	misc_python.write("ascii.txt", list1)

if __name__ == '__main__':


    main()
	#i=127-32
	#print("|" + chr(i+32) + "|" + str(i+32) + "|"+ the_lord.binary_repr(i+32,8) + "|")
