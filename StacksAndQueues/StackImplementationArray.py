# Implementation of Stack in Python using List / Array

class Stack():
    def __init__(self):
        self.stack = []
        self.length = len(self.stack)

    def peek(self):
        if self.stack:
            print(self.stack[0])
        else:
            print("Empty Stack")

    def push(self, value):
        self.stack.append(value)
        self.length += 1

    def pop(self):
        if self.length > 0:
            self.stack.pop()
            self.length -= 1
        else:
            return

    def printStack(self):
        if self.stack:
            for data in self.stack:
                print(data, end = " > ")
            print()
        else:
            print("Empty Stack")

        print(f"Length of Stack: {self.length}")

myStack = Stack()
myStack.push(5)
myStack.printStack()
myStack.peek()
myStack.push(10)
myStack.printStack()
myStack.pop()
myStack.printStack()
myStack.pop()
myStack.printStack()