

class Graph(object):

    #edges are (node1, node2, relation) triplets
    def __init__(self, nodes = None, edges = None):
        self.adjacencyDict = dict()
        if nodes is not None:
            for node in nodes:
                self.adjacencyDict[node] = list()
        if edges is not None:
            for edge in edges:
                n1, n2, rel = edge
                self.addRelation(n1, n2, rel) #might be unpacking issue

    def printLL(self, l):
        print("Linked list:")
        while l is not None:
            print("\t" + str(l.node))
            l = l.nextN

    def linkedList2List(self, start):
        l = list()
        while start is not None:
            l.append((start.node,start.relation))
            start = start.nextN
        return l

    def getNeighbors(self, node, relation = None):
        neighbors = list()
        for lnode in self.adjacencyDict[node]:
            neighbors.extend(self.linkedList2List(lnode))
        return neighbors

    def addEdge(self, node1, node2, relation):
        #print("adding " + str(node1) + " and " + str(node2))
        for lnode in self.adjacencyDict[node1]:
            if lnode.relation == relation:
                #print("\t old ll")
                #add to linked list chain
                newRelation = ListNode(node2, lnode, relation)
                self.adjacencyDict[node1].remove(lnode)
                self.adjacencyDict[node1].append(newRelation)
                return
        #no existing relations of this type
        #print("\t new ll")
        self.adjacencyDict[node1].append(ListNode(node2, None, relation))

    def spliceFromLinkedList(self, start, node):
        if start.node == node:
            #leave start "dangling"
            return start.nextN
        searchNode = start
        while searchNode.nextN is not None:
            if searchNode.nextN.node == node:
               searchNode.nextN = searchNode.nextN.nextN
               return start
            searchNode = searchNode.nextN
        #print("oops, nothing to splice")
        

    def addRelation(self, node1, node2, relation):
        self.addEdge(node1, node2, relation)
        self.addEdge(node2, node1, relation.compliment())


    #deletes a relation, only in one direction    
    def deleteRelation(self, node1, node2, relation):
        for lnode in self.adjacencyDict[node1]:
            if lnode.relation == relation:
                splicedList =self. spliceFromLinkedList(lnode, node2)
                self.adjacencyDict[node1].remove(lnode)
                self.adjacencyDict[node1].append(splicedList)
        #print("oops, nothing to delete")
                
    
    def isInLinkedList(self, start, node):
        while start is not None:
            if start.node == node:
                return True
            else:
                start = start.nextN
        return False
    
    # return true if certain relation exists between nodes (if no relation
    # specified, it serches for any relation)
    def hasEdge(self, node1, node2, relation = None):
        #print("checking " + str(node1) + " and " + str(node2))
        for lnode in self.adjacencyDict[node1]:
            #self.printLL(lnode)
            if relation is not None:
                if lnode.relation == relation:
                    #print("1")
                    return self.isInLinkedList(lnode, node2)
                else:
                    #print("2")
                    return False
            else:
                if self.isInLikedList(lnode, node2):
                    #print("3")
                    return True
        #print("4")
        return False
    
    #add unconnceted node
    def addNode(self, node):
        if node not in self.adjacencyDict:
            self.adjacencyDict[node] = list()

    #removes all references to a node form a graph
    def deleteNode(self, node):
        if node in self.adjacencyDict:
            for neighbor in self.getNeighbors(node):
                nNode, rel = neighbor
                #backwards order important
                self.deleteRelation(nNode, node, rel.compliment())
            del self.adjacencyDict[node]
        else:
            print("oops, no node to delete")

    def getNodeCount(self):
        cnt = 0
        for key in self.adjacencyDict.keys():
            cnt += 1
        return cnt
                
            
    def getNodes(self):
        return self.adjacencyDict.keys()


class ListNode(object):

    def __init__(self, node, nextN, relation):
        self.node = node
        self.nextN = nextN
        self.relation = relation

    def __str__(self):
        return "list node with " + str(self.node)

class Node(object):

    def __init__(self, title, coord = None, filePath = None, label = None):
        self.title = title
        self.filePath = filePath
        self.label = label
        self.coord = coord 

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.title == other.title

    def __hash__(self):
        return hash(self.title)

    def __str__(self):
        return self.title


    #for now, just one relation class, it's compliment() will be the same type
class Relation(object):
    

    def __eq__(self, other):
        if isinstance(other, Relation):
            return True

    def compliment(self):
        return Relation()
    
