#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      mattl
#
# Created:     27/02/2018
# Copyright:   (c) mattl 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import misc_python as misc

def main():
	data = misc.sortFromFile("E:\School Files\A Level\Computing\Python\Python files\wordsEn2.txt", False)
	data2 = [99999]
	for count in range(99999):
		data2.append(data[count])
		#print(count, data[count])
	misc.write("E:\School Files\A Level\Computing\Python\Python files\shortEn.txt", data2)


if __name__ == '__main__':
    main()
