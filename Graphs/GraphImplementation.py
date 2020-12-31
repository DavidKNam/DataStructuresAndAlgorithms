# Implementation of Graph in Python

class Graph():
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}

    def addVertex(self, node):
        if node in self.adjacentList:
            print("Node already exists")
            return
        else:
            self.adjacentList[node] = set()
            self.adjacentList += 1

    def addEdge(self, node1, node2):
        if node1 in self.adjacentList and node2 in self.adjacentList:
            self.adjacentList[node1].add(node2)
            self.adjacentList[node2].add(node1)
        else:
            print("One of the Nodes not available")
            return

    def showConnections(self):
        for nodes in self.adjacentList:
            print(f"{nodes}: {self.adjacentList[nodes]}")

myGraph = Graph()
myGraph.addVertex(0)
myGraph.addVertex(1)
myGraph.addVertex(2)
myGraph.addVertex(3)
myGraph.addVertex(4)
myGraph.addVertex(5)
myGraph.addVertex(6)
myGraph.addEdge(3,1)
myGraph.addEdge(3,4)
myGraph.addEdge(4,2)
myGraph.addEdge(4,5)
myGraph.addEdge(1,2)
myGraph.addEdge(1,0)
myGraph.addEdge(0,2)
myGraph.addEdge(6,5)
myGraph.showConnections()