# Implementation of Binary Search Tree in Python

class Node():
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if not self.root:
            self.root = newNode
        else:
            current_node = self.root
            while current_node:
                if current_node.data >= newNode.data:
                    previous_node = current_node
                    current_node = current_node.right
                else:
                    previous_node = current_node
                    current_node = current_node.left

            if previous_node.data >= newNode.data:
                previous_node.right = newNode
            else:
                previous_node.left = newNode

    def lookup(self, value):
        if not self.root:
            return False
        else:
            current_node = self.root
            while current_node:
                if current_node.data > value:
                    current_node = current_node.right
                elif current_node.data < value:
                    current_node = current_node.left
                elif current_node.data == value:
                    return True
                else:
                    return False

    def print_tree(self):
        if self.root != None:
            self.printt(self.root)

    def printt(self, current_node):
        if current_node != None:
            self.printt(current_node.left)
            print(str(current_node.data))
            self.printt(current_node.right)

# Tree to make
#         9
#     4      20
#   1   6  15  170

myBST = BST()
myBST.insert(9)
myBST.insert(4)
myBST.insert(20)
myBST.insert(1)
myBST.insert(6)
myBST.insert(15)
myBST.insert(170)
print(myBST.lookup(170))
print(myBST.lookup(16))
print(myBST.lookup(6))
myBST.print_tree()