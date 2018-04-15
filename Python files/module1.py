nextFree2 = 0

class Node:
	def __init__(self, contents=None, next=None):
		self.contents = contents
		self.next  = next
		nextFree = nextFree2 + 1

	def getContents(self):
		return self.contents

	def __str__(self):
		return str(self.contents)

def print_list(node):
    while node:
        print(node.getContents())
        node = node.next
    print()




def main():
	nextFree2 = 0
	node1 = Node("car")
	node2 = Node("bus")
	node3 = Node("lorry")
	node1.next = node3
	node3.next = node2
	print_list(node1)
	position = int(input("which position?"))
	data = str(input("What data?"))
	str1 = 'print("'
	str2 = '")'
	nextFree2 = str(nextFree2)
	position2 = str(position-1)
	if input("add?") == "add":
		code1 = "node" + position2 + ".next = node" + str(nextFree2)
		code2 = "node" + nextFree2 + ' = "' + data + '"'
		code3 = "node" + nextFree2 + ".next = node" + str(position)
		exec(code2)
		exec(code1)
		exec(code3)

if __name__ == '__main__':
	#setup()
	main()
