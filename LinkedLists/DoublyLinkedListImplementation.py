# Implementation of Doubly Linked List in Python

class Node():

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList():
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.length = 1

    def append(self, data):
        newTail = Node(data)
        newTail.previous = self.tail
        self.tail.next = newTail
        self.tail = newTail
        self.length += 1

    def prepend(self, data):
        newHead = Node(data)
        self.head.previous = newHead
        newHead.next = self.head
        self.head = newHead
        self.length += 1

    def insert(self, index, data):
        if index == 0:
            self.prepend(data)
            return

        if index >= self.length:
            self.append(data)
            return

        tmp = self.head

        for _ in range(index-1):
            tmp = tmp.next

        newNode = Node(data)
        tmp.next.previous, tmp.next, newNode.next, newNode.previous = newNode, newNode, tmp.next, tmp
        self.length += 1

    def remove(self, index):
        if self.length == 0:
            return

        tmp = self.head

        if index == 0:
            self.head = tmp.next
            self.head.previous = None
        elif index >= self.length:
            self.tail = self.tail.previous
            self.tail.next = None
        else:
            for _ in range(index-1):
               tmp = tmp.next

            tmp.next.next.previous, tmp.next = tmp, tmp.next.next

        self.length -= 1

    def printList(self):
        tmp = self.head
        while tmp != None:
            print(tmp.data, end = " <-> ")
            tmp = tmp.next
        print()
        print(f"Length of Linked List: {self.length}")

myLinkedList = DoublyLinkedList(10)
myLinkedList.printList()
myLinkedList.append(5)
myLinkedList.append(16)
myLinkedList.printList()
myLinkedList.prepend(1)
myLinkedList.printList()
myLinkedList.insert(200, 11)
myLinkedList.printList()
myLinkedList.remove(0)
myLinkedList.remove(100)
myLinkedList.remove(1)
myLinkedList.printList()