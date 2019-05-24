from graphics import *
import math

class Aimer:

    def __init__(self, m_win):
        self.m_win = m_win

        self.ang = 45.0
        self.mag = 2.0**0.5
        self.x_comp = 1.0
        self.y_comp = 1.0
        self.scope = Line(Point(0,0), Point(self.x_comp, self.y_comp))
        self.scope.setArrow("last")
        self.scope.setFill("dark green")
        self.scope.draw(self.m_win)

    def aim_loop(self):
        while True:
            # get input
            key = self.m_win.checkKey()
            print(key)
            # comprehend input
            if key == "Left":
                self.mag -= 0.5
            if key == "Right":
                self.mag += 0.5
            if key == "Up":
                if self.ang <= 89.0:
                    self.ang += 0.5
            if key == "Down":
                if self.ang >= 0.0:
                    self.ang -= 0.5
            if key == "Return":
                # return velocity compnents
                rVal = [self.x_comp, self.y_comp]
                return rVal
            # calculate components of line
            self.x_comp = math.cos(math.radians(self.ang))*self.mag
            self.y_comp = math.sin(math.radians(self.ang))*self.mag
            # draw aim tool
            self.scope.undraw()
            self.scope = Line(Point(0,0), Point(self.x_comp, self.y_comp))
            self.scope.setArrow("last")
            self.scope.setFill("dark green")
            self.scope.draw(self.m_win)
            time.sleep(.05)
