from graphics import *
class Projectile:
    'Base Class for projectile objects'

# constructor
# radius for size of ball (>0)
# elasticity for bouncyness (>0 & <1)
    def __init__( self, radius, elasticity, m_win):
        self.elasticity = elasticity
        self.radius = radius
        self.x = 1.0
        self.y = 1.0
        self.m_win = m_win
        # animation
        self.a = Circle(Point(self.getX(),self.getY()), self.radius)
        self.a.setFill("orange")
        self.a.draw(m_win)

        self.b = Circle(Point(self.getX(),self.getY()), self.radius)
        self.b.setFill("orange")
        self.b.draw(m_win)

        self.draw_count = 0

    def draw(self):
        if (self.draw_count == 0):
            self.draw_a()
        elif (self.draw_count == 1):
            self.draw_b()

        print("draw loop")

    def draw_b(self):
        print("B")
        # draws new circle B
        self.b.undraw()
        self.b = Circle(Point(self.getX(),self.getY()), self.radius)
        self.b.setFill("orange")
        self.b.draw(self.m_win)
        self.draw_count = 0

    def draw_a(self):
        print("A")
        # draws new circle A
        self.a.undraw()
        self.a = Circle(Point(self.getX(),self.getY()), self.radius)
        self.a.setFill("orange")
        self.a.draw(self.m_win)
        self.draw_count = 1

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y
