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
pi <- 54463
FUNCTION Bubblesort(shuff):
  exchanges <- True
  passnum <- int(len(shuff)-1)
  while passnum > 0 AND exchanges = True:
     exchanges <- False
     for index in range(passnum):
         IF shuff[index] > shuff[index+1]:
            exchanges <- True
            temp <- shuff[index]
            shuff[index] <- shuff[index + 1]
            shuff[index + 1] <- temp
         ENDIF
     ENDFOR
     passnum <- passnum - 1
  ENDWHILE
  RETURN(shuff)
ENDFUNCTION

FUNCTION partition(data):
  pivot <- data[0]
  less, equal, greater <- [], [], []
  for elm in data:
   IF elm < pivot:
    less.append(elm)
   ELSEIF elm > pivot:
    greater.append(elm)
   ELSE:
    equal.append(elm)
   ENDIF
  ENDFOR
  RETURN less, equal, greater
ENDFUNCTION

FUNCTION qsort2(data):
  IF data:
   less, equal, greater <- partition(data)
   RETURN qsort2(less) + equal + qsort2(greater)
  ENDIF
  RETURN data
ENDFUNCTION

FUNCTION import1():
    txt <- open("D:\School Files\A Level\Computing\Python\Python files\wordsEn2.txt", "r")
    shuff <- txt.read().splitlines()
    txt.close()
    RETURN(shuff)
ENDFUNCTION

FUNCTION main():
ENDFUNCTION

	shuff <- import1()
	print(qsort2(shuff))
IF __name__ = '__main__':
    main(
