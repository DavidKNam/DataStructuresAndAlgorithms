# Implementation of Linked List in Python

class Node():

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.length = 1

    def append(self, data):
        newTail = Node(data)
        self.tail.next = newTail
        self.tail = newTail
        self.length += 1

    def prepend(self, data):
        newHead = Node(data)
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
        tmp.next, newNode.next = newNode, tmp.next
        self.length += 1

    def remove(self, index):
        if self.length == 0:
            return

        if index >= self.length:
            index = self.length - 1

        tmp = self.head

        if index == 0:
            self.head = tmp.next
        else:
            for _ in range(index-1):
               tmp = tmp.next

            tmp.next = tmp.next.next

            if index == self.length - 1:
                self.tail = tmp

        self.length -= 1

    def reverse(self):
        if self.length <= 1:
            return
        else:
            previous = None
            self.tail = self.head
            while self.head != None:
                tmp = self.head
                self.head = self.head.next
                tmp.next = previous
                previous = tmp
            self.head = tmp

    def printList(self):
        tmp = self.head
        while tmp != None:
            print(tmp.data, end = " -> ")
            tmp = tmp.next
        print()
        print(f"Length of Linked List: {self.length}")

myLinkedList = LinkedList(10)
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
myLinkedList.append(5)
myLinkedList.append(3)
myLinkedList.printList()
myLinkedList.reverse()
myLinkedList.printList()