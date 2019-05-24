import random
from Wall import *
from graphics import *
from Simulation import *
from Target import *
from Aimer import *
class Level:

    # x_range = [ [20,40], [40,60], [60,80], [80,100], [100,120], [120,140], [140,160] ]
    # y_range = [ [0,20], [20,40], [40,60], [60,80], [80,100] ]
    x_range = [ [20,25], [40,45], [60,65], [80,85], [100,105], [120,125], [140,145] ]
    y_range = [ [0,20], [70,100], [0,40], [50,100], [0,60] ]

    def __init__(self, level_num, difficulty, moving_target):
        self.difficulty = difficulty
        self.moves = moving_target
        self.level_num = level_num

        self.rad = 2
        self.time_step = 0.05
        self.win_x = 200.0
        self.win_y = 100.0
        self.center = Point(self.win_x / 2, self.win_y / 2)
        # create window
        self.m_win = GraphWin( ("Level" + str(self.level_num)), 1000, 500)
        # set up coordinate system
        self.m_win.setCoords(0, 0, self.win_x, self.win_y)
        self.prime_msg()
        # fill in background
        self.m_win.setBackground("light blue")
        # make walls
        self.walls = self.get_walls()
        # start simulation
        self.sim = Simulation(self.time_step, self.win_x, self.win_y, self.walls, self.m_win)
        # static target for now
        self.target = Target(Point(175,0), Point(180,5), False, self.m_win)

        # if no moving target
        if (self.moves == False):
            # create aiming tool
            self.aim_tool = Aimer(self.m_win)
            self.sim.set_vel(self.aim_tool.aim_loop())
            self.target.set_moves(False)
        else:
            # dont use aimer
            vel = [random.randint(2,30), random.randint(2,30)]
            self.sim.set_vel(vel)
            # make target move
            self.target.set_moves(True)


    def run_game(self):
        # run loop
        for i in range(10000):
            # plot one pixel

            self.sim.loop()
            if self.target.hit_target(self.sim.ball, self.m_win):
                message = Text(Point(50,50), "YOU WON!")
                message.setSize(30)
                message.setStyle("bold")
                message.setTextColor("green")
                message.draw(self.m_win)
                print("YOU WON! CONGRATULATIONS!")
                # wait for click
                self.m_win.getMouse()
                break
            elif self.sim.ball.getY() < -1:
                message = Text(Point(50,50), "YOU LOSE!")
                message.setSize(30)
                message.setStyle("bold")
                message.setTextColor("black")
                message.draw(self.m_win)
                print("YOU LOSE! Try again? (y/n)")
                # wait for click
                self.m_win.getMouse()
                break
            # time.sleep(self.time_step/10)



    def get_walls(self):
        walls = [None] * self.difficulty
        for x in range(self.difficulty):

            x %= len(self.x_range)
            lx = Level.x_range[x][0]
            rx = Level.x_range[x][1]
            tempx = lx
            lx = min(lx, rx)
            rx = max(tempx, rx)

            # for y in range(self.difficulty):
            if True:
                y = x
                y %= len(self.y_range)



                ly = random.randint(Level.y_range[y][0],Level.y_range[y][1])
                uy = random.randint(Level.y_range[y][0],Level.y_range[y][1])
                tempy = ly
                ly = min(ly, uy)
                uy = max(tempy, uy)

                if Level.y_range[y][0] == 0:
                    ly = 0
                else:
                    uy = 100

                p_a = Point(lx, ly)
                p_b = Point(rx, uy)
                print("expected:", self.difficulty**2)
                print("length:", (x)*self.difficulty + (y))
                walls[x] = Wall(p_a, p_b, self.m_win)
        return walls

    def prime_msg(self):
        greet = Text( self.center, ("Welcome to level " + str(self.level_num)))
        p_diff = Point(self.center.getX(), self.center.getY() - 8)
        diff = Text( p_diff, ("Difficulty:", self.difficulty))
        p_inst = Point(self.center.getX(), self.center.getY() - 20)

        if(self.moves):
            instructions = Text( p_inst, ("Your goal is to catch the ball.\nMove the goal with the left/right arrow keys\nPress any key to continue"))
        else:
            instructions = Text( p_inst, ("Your goal is to score ball.\nAim with the up/down/left/right arrow keys\nPress any key to continue"))

        self.m_win.setBackground("dark blue")
        greet.setSize(30)
        greet.setStyle("bold")
        greet.setTextColor("white")
        diff.setSize(20)
        diff.setStyle("bold")
        diff.setTextColor("white")
        instructions.setSize(15)
        instructions.setTextColor("white")
        greet.draw(self.m_win)
        diff.draw(self.m_win)
        instructions.draw(self.m_win)
        # wait
        self.m_win.getKey()

        greet.undraw()
        diff.undraw()
        instructions.undraw()
