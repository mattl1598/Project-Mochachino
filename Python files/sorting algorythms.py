#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      matthewl9
#
# Created:     20/02/2018
# Copyright:   (c) matthewl9 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
pi = 54463
def Bubblesort(shuff):
  exchanges = True
  passnum = int(len(shuff)-1)

  while passnum > 0 and exchanges == True:
     exchanges = False
     for index in range(passnum):
         if shuff[index] > shuff[index+1]:
            exchanges = True
            temp = shuff[index]
            shuff[index] = shuff[index + 1]
            shuff[index + 1] = temp
     passnum = passnum - 1
  return(shuff)





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

def qsort2(data):
  if data:
   less, equal, greater = partition(data)
   return qsort2(less) + equal + qsort2(greater)
  return data



def import1():
    txt = open("D:\School Files\A Level\Computing\Python\Python files\wordsEn2.txt", "r")
    shuff = txt.read().splitlines()
    txt.close()
    return(shuff)



def main():
	shuff = import1()
	#print(len(shuff))
	print(qsort2(shuff))

if __name__ == '__main__':
    main()