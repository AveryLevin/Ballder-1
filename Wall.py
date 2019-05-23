from graphics import *
class Wall:

    def __init__(self, p_a, p_b, m_win):
        self.llx = p_a.getX()
        self.lly = p_a.getY()
        self.urx = p_b.getX()
        self.ury = p_b.getY()
        self.wall = Rectangle( Point(self.llx, self.lly), Point(self.urx, self.ury))
        self.wall.setFill("red")
        self.wall.draw(m_win)
