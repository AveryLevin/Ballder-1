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
        self.c = Circle(Point(self.getX(),self.getY()), self.radius)
        self.c.setFill("orange")
        self.c.draw(m_win)

    def draw(self):
        self.c.undraw()
        self.c = Circle(Point(self.getX(),self.getY()), self.radius)
        self.c.setFill("orange")
        self.c.draw(self.m_win)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y
