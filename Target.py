from Projectile import *
from graphics import *
class Target:

    speed = 0.6

    def __init__(self, p_a, p_b, moves, m_win):
        self.llx = p_a.getX()
        self.lly = p_a.getY()
        self.urx = p_b.getX()
        self.ury = p_b.getY()
        self.moves = moves
        self.goal = Rectangle( Point(self.llx, self.lly), Point(self.urx, self.ury))
        self.goal.setFill("green")
        self.goal.draw(m_win)


    def set_moves(self, moves):
        self.moves = moves

    def hit_target(self, p , m_win):

        if self.moves:
            # get input
            key = m_win.checkKey()

            if key == "Left":
                self.llx -= Target.speed
                self.urx -= Target.speed
            if key == "Right":
                self.llx += Target.speed
                self.urx += Target.speed

        # draw goal
        self.goal.undraw()
        self.goal = Rectangle( Point(self.llx, self.lly), Point(self.urx, self.ury))
        self.goal.setFill("green")
        self.goal.draw(m_win)
        # check location
        x = p.getX()
        y = p.getY()
        # check x dimensions
        if x > self.llx and x < self.urx:
            # check y dimensions
            if y > self.lly and y < self.ury:
                # reached goal
                return True

        # if didnt return True
        return False
