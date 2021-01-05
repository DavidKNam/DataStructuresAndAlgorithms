# Implementation of Binary Search Tree Validation in Python

class Node():
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class BST():
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            current_node = self.root
            while current_node:
                if current_node.data <= new_node.data:
                    previous_node = current_node
                    current_node = current_node.right
                else:
                    previous_node = current_node
                    current_node = current_node.left

            if previous_node.data <= new_node.data:
                previous_node.right = new_node
            else:
                previous_node.left = new_node

    def lookup(self, value):
        if not self.root:
            return False
        else:
            current_node = self.root
            while current_node:
                if current_node.data < value:
                    current_node = current_node.right
                elif current_node.data > value:
                    current_node = current_node.left
                elif current_node.data == value:
                    return True
                else:
                    return False

    def validateBST(self):

        queue = []

        if not self.root:
            return True
        else:
            queue.append(self.root)
            while len(queue) > 0:
                current_node = queue.pop(0)
                if current_node.left:
                    if current_node.left.data < current_node.data:
                        queue.append(current_node.left)
                    else:
                        return False
                if current_node.right:
                    if current_node.right.data >= current_node.data:
                        queue.append(current_node.right)
                    else:
                        return False
        return True


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
print(myBST.validateBST())