#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      matthewl9
#
# Created:     06/03/2018
# Copyright:   (c) matthewl9 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
import dijkstra #work for dictionarys not matrixes

def createMatrix(adjMatrix):
	for x in range(9):
		for y in range(9):
			rand = random.randint(1,15)
			#print
			adjMatrix[x][y] = rand
	return adjMatrix
def main():
	w, h = 9, 9;
	adjMatrix = [[None for x in range(w)] for y in range(h)]
	adjMatrix = createMatrix(adjMatrix)
	print(adjMatrix)
	print(dijkstra.shortestPath(adjMatrix,2,7))

if __name__ == '__main__':
    main()
