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

def main(x):
	list1 = []
	for i in range(x):
		list1.append("else if (key = " +chr(34) + str(i) + chr(34)+ ")")
		list1.append("msgbox "+str(i))
	misc_python.write("if key2.txt", list1)

if __name__ == '__main__':
    main(32)
