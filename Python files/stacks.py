#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      matthewl9
#
# Created:     28/03/2018
# Copyright:   (c) matthewl9 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import misc_python


def main():
	stack1 = misc_python.stack
	for i in range(20):
		stack1.add(stack1,i)
	print(stack1.stack)


if __name__ == '__main__':
    main()
