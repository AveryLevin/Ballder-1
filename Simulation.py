from Projectile import *
from Wall import *

class Simulation:
    'Class for running simulation'
    # acceleration for simulated world
    accel = -9.8

    def __init__(self, time_step, window_x, window_y, x_vel, y_vel, wall , m_win):
        self.time_step = time_step
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.window_x = window_x
        self.window_y = window_y
        # create projectile object
        self.ball = Projectile(2, 0.8, m_win)
        self.wall = wall
        self.x_bnc = False
        self.y_bnc = False
        self.m_win = m_win

    def loop(self):

        # log last position
        x = self.ball.getX()
        y = self.ball.getY()

        # check for bounce occurence
        if self.check_for_x_bounce():
            self.x_vel *= -self.ball.elasticity
        if self.check_for_y_bounce():
            self.y_vel *= -self.ball.elasticity


        # accumulate position
        self.ball.setX(x + self.x_vel*self.time_step)
        self.ball.setY(y + self.y_vel*self.time_step + 0.5*Simulation.accel*(self.time_step**2) )

        self.y_vel += 0.5*Simulation.accel*self.time_step
        # draw ball
        self.ball.draw()
        # provide debug position readouts
        print("X:", x, "\t", "Y:", y, "\tACCELERATION:", (0.5*Simulation.accel*(self.time_step**2)))


    def check_for_x_bounce(self):
        if self.ball.getX() <= 0 or self.ball.getX() >= self.window_x:
            if self.x_bnc == False:
                print("X BOUNCE!!")
                self.x_bnc = True
                return True
            else:
                return False
        elif ( self.ball.getX() >= self.wall.llx and self.ball.getX() <= self.wall.urx and self.ball.getY() >= self.wall.lly and self.ball.getY() <= self.wall.ury) :
            if self.x_bnc == False:
                print("X BOUNCE!!")
                self.x_bnc = True
                return True
            else:
                return False
        else:
            self.x_bnc = False
            return False



    def check_for_y_bounce(self):
        if self.ball.getY() <= 0 or self.ball.getY() >= self.window_y:
            if self.y_bnc == False:
                print("Y BOUNCE!!")
                self.y_bnc = True
                return True
            else:
                return False
        else:
            self.y_bnc = False
            return False
