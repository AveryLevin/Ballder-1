from graphics import *
class Projectile:
    'Base Class for projectile objects'

# constructor
# radius for size of ball (>0)
# elasticity for bouncyness (>0 & <1)
    def __init__( self, radius, elasticity, color, m_win):
        self.elasticity = elasticity
        self.radius = radius
        self.x = 1.0
        self.y = 1.0
        self.x_prev = self.x
        self.y_prev = self.y
        self.m_win = m_win
        self.color = color
        # animation
        self.a = Circle(Point(self.getX(),self.getY()), self.radius)
        self.a.setFill(color)
        self.a.setOutline(self.color)
        self.a.draw(m_win)
        """
        self.b = Circle(Point(self.getX(),self.getY()), self.radius)
        self.b.setFill(color)
        self.b.setOutline(self.color)
        self.b.draw(m_win)
        """
        self.draw_count = 0

    def draw(self):
        """
        if (self.draw_count == 0):
            self.draw_a()
        elif (self.draw_count == 1):
            self.draw_b()
        """
        self.draw_a()

        #print("draw loop")

    def draw_b(self):
        print("B")
        # draws new circle B
        """
        self.b.undraw()
        self.b = Circle(Point(self.getX(),self.getY()), self.radius)
        self.b.setFill(self.color)
        self.b.setOutline(self.color)
        self.b.draw(self.m_win)
        self.draw_count = 0
        """

    def draw_a(self):
        #print("A")
        # draws new circle A

        dx = self.x - self.x_prev
        dy = self.y - self.y_prev
        self.a.move(dx, dy)
        """
        self.a.undraw()
        self.a = Circle(Point(self.getX(),self.getY()), self.radius)
        self.a.setFill(self.color)
        self.a.setOutline(self.color)
        self.a.draw(self.m_win)
        self.draw_count = 1
        """

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):

        self.x_prev = self.x
        self.x = x

    def setY(self, y):

        self.y_prev = self.y
        self.y = y
