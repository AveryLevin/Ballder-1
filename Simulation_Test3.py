from Simulation import *
from graphics import *
from Target import *
from Wall import *
def main():
    rad = 2
    time_step = 0.05
    win_x = 200.0
    win_y = 100.0
    xv = 20.0
    yv = 30.0
    # create window
    m_win = GraphWin("My Application", 1000, 500)
    # set up coordinate system
    m_win.setCoords(0, 0, win_x, win_y)
    # fill in background
    m_win.setBackground("light blue")

    wall_a = Wall(Point(80, 20), Point(85, 80), m_win)
    wall_b = Wall(Point(150, 0), Point(152, 20), m_win)
    wall_c = Wall(Point(150, 80), Point(152, 100), m_win)
    walls = [wall_a, wall_b, wall_c]
    m_sim = Simulation(time_step, win_x, win_y, xv, yv, walls, m_win)
    # goal setup
    llx = 80
    lly = 0
    urx = 85
    ury = 4
    m_target = Target(Point(llx, lly), Point(urx, ury), m_win)


    # run loop
    for i in range(1000):
        # plot one pixel

        m_sim.loop()
        if m_target.hit_target(m_sim.ball, m_win):
            message = Text(Point(50,50), "YOU WON!")
            message.setSize(30)
            message.setStyle("bold")
            message.setTextColor("green")
            message.draw(m_win)
            print("YOU WON! CONGRATULATIONS!")
            break
        time.sleep(time_step/10)
    # wait for click
    m_win.getMouse()

main()
