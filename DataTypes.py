########################3333
# some psuedo code for a knowledge graph
########################



class Edge(enum):
    SUBCLASS = 0


class Graph(object):

    def __init__(self, nodes):
        self.edges = make2dArray(len(nodes),None)
        self.nodes = list()
        self.nodes.extend(nodes)
    
    def getEdge(node1, node2)

    def getNodeData(node)

    def getNeighbors(node, filter)
    
    def addNode(node)

    def addEdge(node1, node2, edgetype)

    def deleteEdge(node1, node2)

    def deleteNode(node)



class Node(object):

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def




class HierarchyView(View):

    def display(graph, center):
        for neighbor in graph.getNeighbors(center, Edge.SUBCLASS):
            c

    def onClick
