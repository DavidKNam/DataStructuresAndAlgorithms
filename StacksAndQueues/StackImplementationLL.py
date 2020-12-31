# Implementation of Stack in Python using Linked Lists

class Node():
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.length == 0:
            print("Empty Stack")
        else:
            print(self.top.data)

    def push(self, data):
        newNode = Node(data)
        if self.length > 0:
            newNode.next = self.top
            self.top = newNode
        else:
            self.top = newNode
            self.bottom = self.top

        self.length += 1

    def pop(self):
        if self.length == 0:
            return
        else:
            self.top = self.top.next

        self.length -= 1

        if self.length == 0:
            self.bottom = None

    def printStack(self):
        tmp = self.top
        while tmp != None:
            print(tmp.data, end=" > ")
            tmp = tmp.next
        print()
        print(f"Length of Stack: {self.length}")

myStack = Stack()
myStack.push(5)
myStack.printStack()
myStack.peek()
myStack.push(10)
myStack.printStack()
myStack.pop()
myStack.printStack()