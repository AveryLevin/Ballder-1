from Simulation import *
from graphics import *
from Target import *
def main():
    rad = 2
    time_step = 0.05
    win_x = 200.0
    win_y = 100.0
    xv = 25.0
    yv = 20.0
    m_sim = Simulation(time_step, win_x, win_y, xv, yv)
    # create window
    m_win = GraphWin("My Application", 1000, 500)
    # set up coordinate system
    m_win.setCoords(0, 0, win_x, win_y)
    # fill in background
    m_win.setBackground("light blue")
    # goal setup
    llx = 80
    lly = 0
    urx = 85
    ury = 4
    m_target = Target(Point(llx, lly), Point(urx, ury), m_win)
    c = Circle(Point(m_sim.ball.getX(),m_sim.ball.getY()), rad)
    c.setFill("orange")
    c.draw(m_win)
    # run loop
    for i in range(1000):
        # plot one pixel
        c.undraw()
        c = Circle(Point(m_sim.ball.getX(),m_sim.ball.getY()), rad)
        c.setFill("orange")
        c.draw(m_win)
        m_sim.loop()
        if m_target.hit_target(m_sim.ball, m_win):
            message = Text(Point(50,50), "YOU WON!")
            message.setSize(30)
            message.setStyle("bold")
            message.setTextColor("green")
            message.draw(m_win)
            print("YOU WON! CONGRATULATIONS!")
            break
        time.sleep(.005)
    # wait for click
    m_win.getMouse()

main()
