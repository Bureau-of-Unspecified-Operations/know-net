import pantograph
from graph_logic import *
import math

colors = ["#FF8C00", "#00BFFF", "#A9A9A9", "#ADFF2F"]

def distance(x,y,x1,y1):
    return math.sqrt((x - x1)**2 + (y -y1)**2)

def inBounds(x,y,c):
    return distance(x, y, c[0], c[1]) <= c[2]

def inBoundsNode(x, y, node, r):
    x1,y1 = node.coord
    return distance(x,y,x1,y1) <= r
        

class GraphVis(pantograph.PantographHandler):

    def colorFromText(self,text):
        return colors[hash(text) % len(colors)]

    def drawNode(self,node, r):
        x, y = node.coord
        self.fill_circle(x,y,r, self.colorFromText(node.title))

    def drawEdge(self,node1, node2):
        x0, y0 = node1.coord
        x1, y1 = node2.coord
        color = '#000'
        self.draw_line(x0, y0, x1, y1, color)

    def setup(self):
        n = [Node("A",(self.width // 2, self.height // 2)), Node("B",(200,200)),Node("C",(200,800))]
        r = [(n[0],n[1], Relation()), (n[0], n[2], Relation())]
        self.graph = Graph(n,r)
        self.centerNode = n[0]
        self.isMoving = False


    def update(self):
        visited = set()
        queue = list()
        queue.append(self.centerNode)
        while len(queue) != 0:
            node = queue.pop(0)
            if node not in visited:
                self.drawNode(node, 50)
                neighbors = self.graph.getNeighbors(node)
                for neighbor in neighbors:
                    n, r = neighbor
                    if n not in visited:
                        self.drawEdge(node, n)
                        queue.append(n)
                visited.add(node)

    def on_mouse_down(InputEvent):
        for node in self.graph.getNodes():
            if inBoundsNode(InputEvent.x, InputEvent.y, node, 50):
                newNode = Node("new",node.coord)
                self.graph.addNode(newNode)
                self.graph.addRelation(node, newNode, Relation())
                self.isMoving = True

    def on_mouse_move(InputEvent):
        if self.isMoving:
            self.movingNode.coord = (InputEvent.x, InputEvent.y)

    def on_mouse_up(InputEvent):
        self.movingNode = None
        self.isMoving = False
                

                
            
        
        

if __name__ == '__main__':
    app = pantograph.SimplePantographApplication(GraphVis)
    app.run()
