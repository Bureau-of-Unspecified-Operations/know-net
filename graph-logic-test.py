from graph_logic import *

alphabet = "abcdefghijklmnopqrstuvwxyz"

def makeAGraph():
    g = Graph()
    for c in alphabet:
        g.addNode(Node(c))
    return g

def testRelations():
    r = Relation()
    assert(r == r.compliment())

def testAddNode():
    g = Graph()
    for c in alphabet:
        g.addNode(Node(c))
    assert(g.getNodeCount() == len(alphabet))

def testDelNode():
    nodes = list()
    for c in alphabet:
        nodes.append(Node(c))
    g = Graph(nodes)
    assert(g.getNodeCount() == len(alphabet))
    for node in nodes:
        g.deleteNode(node)
    assert(g.getNodeCount() == 0)

def testHasEdge():
    n = [Node("a"), Node("b"), Node("c")]
    relations = [(n[0],n[1], Relation()), (n[1],n[2], Relation())]
    g = Graph(n, relations)
    assert(g.hasEdge(n[0],n[1],Relation()) == True)
    assert(g.hasEdge(n[0],n[2],Relation()) == False)
    assert(g.hasEdge(n[1],n[2],Relation()) == True)
    assert(g.hasEdge(n[1],n[0],Relation()) == True)
    assert(g.hasEdge(n[2],n[0],Relation()) == False)
    assert(g.hasEdge(n[2],n[1],Relation()) == True)

def testComplexDel():
    n = [Node("a"), Node("b"), Node("c"), Node("d"), Node("e")]
    r = [(n[0],n[1], Relation()), (n[0], n[2], Relation()), (n[0], n[3], Relation()), (n[0],n[4], Relation()), (n[1],n[2], Relation()), (n[2], n[3], Relation())]
    g = Graph(n,r)
    for rel in r:
        n1, n2, re = rel
        assert(g.hasEdge(n1,n2,re) == True)
        assert(g.hasEdge(n2,n1,re.compliment()) == True)
    g.deleteNode(n[1])
    assert(g.hasEdge(n[0],n[1],Relation()) == False)
    
    

def testAll():
    print("Testing...\n")
    testAddNode()
    testDelNode()
    testRelations()
    testHasEdge()
    testComplexDel()

    print("Passed!\n")


testAll()
