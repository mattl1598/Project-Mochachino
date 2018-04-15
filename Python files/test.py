#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      matthewl9
#
# Created:     21/02/2018
# Copyright:   (c) matthewl9 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import misc_python as misc
import time

def main2():                             # timing python search
	data = misc.sortromFile("E:\School Files\A Level\Computing\Python\Python files\wordsEn2.txt", False)
	start = time.time()
	#data = misc.sortFromFile("E:\School Files\A Level\Computing\Python\Python files\wordsEn2.txt", False)
	print(data.index("bee"))
	end = time.time()
	print(end-start)



def main():
	#data = misc.sortFromFile("D:\School Files\A Level\Computing\Python\Python files\wordsEn2.txt", False)
	start = time.time()
	data = misc.sortFromFile("Z:\School Files\A Level\Computing\Python\Python files\wordsEn2.txt", False)
	#print(misc.binSearch("bee", data))
	end = time.time()
	print(end-start)
	#print(data)
	#input("bees?")
	#print(misc.binSearch(input("what word?"), data))

if __name__ == '__main__':
    main()
    #time.sleep(10)
    #main2()
