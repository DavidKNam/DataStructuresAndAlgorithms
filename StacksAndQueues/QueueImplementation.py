# Implementation of Queue in Python using Linked Lists

class Node():
    def __init__(self, value):
        self.data = value
        self.next = None

class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self.first:
            print(self.first.data)
        else:
            print("Empty Queue")

    def enqueue(self, value):
        newNode = Node(value)
        if self.first:
            self.last.next = newNode
            self.last = newNode
        else:
            self.first = newNode
            self.last = self.first
        self.length += 1

    def dequeue(self):
        if self.first:
            self.first = self.first.next
            self.length -= 1
            if self.length == 0:
                self.last = None
        else:
            print("Empty Stack")

    def printQueue(self):
        tmp = self.first
        if tmp:
            while tmp != None:
                print(tmp.data, end = " <- ")
                tmp = tmp.next
            print()
        else:
            print("Empty Stack")
        print(f"Length of Queue: {self.length}")

myQueue = Queue()
myQueue.enqueue(5)
myQueue.printQueue()
myQueue.enqueue(10)
myQueue.printQueue()
myQueue.peek()
myQueue.dequeue()
myQueue.printQueue()
myQueue.dequeue()
myQueue.printQueue()