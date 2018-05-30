

class Graph(object):

    #edges are (node1, node2, relation) triplets
    def __init__(self, nodes, edges):
        self.adjacencyDict = dict()
        for node in nodes:
            self.adjacencyDict[node] = list()
        for edge in edges:
            self.addRelation(edge) #might be unpacking issue

    def addEdge(self, node1, node2, relation):
        for lnode in self.adjacencyDict[node1]:
            if lnode.relation == relation:
                #add to linked list chain
                newRelation = ListNode(node2, lnode, relation)
                lnode = newRelation
        #no existing relations of this type
        self.adjacencyDict[node1].append(ListNode(node2, None, relation))

    def removeFromLinkedList(self, start, node):
        if start.node == node:
            start 
        while start.nextN is not None:
            if start.nextN.node == node:
                node.nextN = start.nextN.nextN
                

    def addRelation(self, node1, node2, relation):
        addEdge(node1, node2, relation)
        addEdge(node1, node2, relation.compliment)

    def deleteRelation(self, node1, node2, relation):
        for lnode in self.adjacecyDict[node1]:
            if lnode.relation == relation:
                removeFromLinkedList(start, trgNode)
                

    def isInLinkedList(start, node):
        while start is not None:
            if start.node = node:
                return True
            else:
                start = start.nextN
        return False

    def hasEdge(self, node1, node2, relation = None):
        for lnode in self.adjacencyDict[node1]:
            if relation is not None:
                if lnode.relation == relation:
                    return isInLinkedList(lnode, node2)
                else: return False
            else:
                if isInLikedList(lnode, node2):
                    return True
        return False
    def addNode(self, node):
        self.adjacencyDict[node] = list()

    def deleteNode(self, node):
        if node in self.adjacencyDict:
            



class ListNode(object):

    def __init__(self, node, nextN, relation):
        self.node = node
        self.nextN = nextN
        self.relation = relation
    

class Node(object):

    def __init__(self, title, filePath, label = None):
        self.title = title
        self.filePath = filePath
        self.label = label

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.title = other.title

    def __hash__(self):
        return hash(self.title)


class Relation(object):
