#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      matthewl9
#
# Created:     13/03/2018
# Copyright:   (c) matthewl9 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import misc_python
# simple binary tree
# in this implementation, a node is inserted between an existing node and the root


class BinaryTree():

    def __init__(self,rootid):
      self.left = None
      self.right = None
      self.rootid = rootid

    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def setNodeValue(self,value):
        self.rootid = value
    def getNodeValue(self):
        return self.rootid

    def insertRight(self,newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree

    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            self.left = tree
            tree.left = self.left


def printPreTree(tree):
        if tree != None:
            print(tree.getNodeValue())
            printPreTree(tree.getLeftChild())
            printPreTree(tree.getRightChild())

def printInTree(tree):
        if tree != None:
            printInTree(tree.getLeftChild())
            print(tree.getNodeValue())
            printInTree(tree.getRightChild())

def printPostTree(tree):
        if tree != None:
            printPostTree(tree.getLeftChild())
            printPostTree(tree.getRightChild())
            print(tree.getNodeValue())



# test tree



def testTree():
	myTree = BinaryTree("Maud")
	myTree.insertLeft("Bob")
	myTree.insertRight("Tony")
	myTree.insertRight("Steven")

	printPreTree(myTree)
	print()
	printInTree(myTree)
	print()
	printPostTree(myTree)



def main():
	testTree()

if __name__ == '__main__':
    main()
