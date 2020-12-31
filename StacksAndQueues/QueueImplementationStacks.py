# Implementation of Queue in Python using Stacks

class Stack():
    def __init__(self):
        self.stack = []
        self.length = len(self.stack)

    def peek(self):
        if self.stack:
            return self.stack[0]
        else:
            return None

    def push(self, value):
        self.stack.append(value)
        self.length += 1

    def pop(self):
        if self.length > 0:
            self.length -= 1
            return self.stack.pop()
        else:
            return None

    def printStack(self):
        if self.stack:
            for data in self.stack:
                print(data, end = " > ")
            print()
        else:
            print("Empty Stack")

        print(f"Length of Stack: {self.length}")

class Queue():
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, data):
        self.stack1.push(data)

    def pop(self):
        if self.stack2.stack:
            self.stack2.pop()
        else:
            while self.stack1.stack:
                self.stack2.push(self.stack1.pop())
            self.stack2.pop()

    def peek(self):
        if self.stack2.stack:
            return self.stack2.peek()
        else:
            while self.stack1.stack:
                self.stack2.push(self.stack1.pop)
            return self.stack2.peek()

    def empty(self):
        return not self.stack1.stack and not self.stack2.stack

    def printStacks(self):
        self.stack1.printStack()
        self.stack2.printStack()

myQueue = Queue()
myQueue.push(5)
myQueue.push(15)
myQueue.pop()
myQueue.printStacks()
print(myQueue.peek())
myQueue.pop()
print(myQueue.empty())