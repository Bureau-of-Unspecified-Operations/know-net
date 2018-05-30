import pantograph
import math

# Animate a spinning wheel on the canvas



# make some ircles, clicking in a circle adds another one
def distance(x,y,x1,y1):
    return math.sqrt((x - x1)**2 + (y -y1)**2)

def inBounds(x,y,c):
    return distance(x, y, c[0], c[1]) <= c[2]
        

class Rotary(pantograph.PantographHandler):
    def setup(self):
        self.circles = list()
        for i in range(5):
            self.circles.append((i * 100, i * 100, 20))
    
    def update(self):

        self.clear_rect(0, 0, self.width, self.height)
        # draw the circle for the "rim" of the wheel
        for circle in self.circles:
            self.draw_circle(circle[0], circle[1], circle[2], "#000")

    def on_mouse_down(self, InputEvent):
        x, y = InputEvent.x, InputEvent.y
        for circle in self.circles:
            if inBounds(x,y,circle):
                i = len(self.circles)
                self.circles.append((i * 100, i *100, 20))
        
    
    
if __name__ == '__main__':
    app = pantograph.SimplePantographApplication(Rotary)
    app.run()
