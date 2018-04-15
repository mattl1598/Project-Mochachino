#-------------------------------------------------------------------------------
# Name:        misc_python
# Purpose:     misc python utilities
#
# Author:      matthewl9
#
# Version:     1.0
#
# Contains:    write to file, quicksort, import_list
#
# Created:     21/02/2018
# Copyright:   (c) matthewl9 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def write(filepath, list1):
	filepath = str(filepath)
	file = open(filepath,"w")
	for count in range (len(list1)):
		file.write(list1[count])
		if count < (len(list1)-1):
			file.write("\n")
	file.close

def partition(data):
  pivot = data[0]
  less, equal, greater = [], [], []
  for elm in data:
   if elm < pivot:
    less.append(elm)
   elif elm > pivot:
    greater.append(elm)
   else:
    equal.append(elm)
  return less, equal, greater

def quicksort(data):
  if data:
   less, equal, greater = partition(data)
   return qsort2(less) + equal + qsort2(greater)
  return data

def import_list(filepath):
	filepath = str(filepath)
	txt = open(filepath, "r")
	shuff = txt.read().splitlines()
	txt.close()
	return(shuff)
