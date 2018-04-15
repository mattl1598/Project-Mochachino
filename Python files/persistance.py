#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      matthewl9
#
# Created:     01/02/2018
# Copyright:   (c) matthewl9 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    value = 0
    operation = 0
    value = int(input("Enter Integer (0-99)"))
    operation = str(input("Calculate additive or multiplicative persistance (a or m) ?"))
    count = 0
    while value>9:
        if operation == "a":
	       	value = (int(value/10))+(value%10)
        else:
	       	value = (int(value/10))*(value%10)
        count = count + 1
    print("The persistance is: ")
    print(count)

if __name__ == '__main__':
    main()
