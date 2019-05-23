from Simulation import *
from graphics import *
def main():
    time_step = 0.05
    win_x = 100.0
    win_y = 100.0
    goal = 100.0
    xv = 10.0
    yv = 20.0
    m_sim = Simulation(time_step, win_x, win_y, goal, xv, yv)
    # create window
    m_win = GraphWin("My Application", 1000, 500)
    # set up coordinate system
    m_win.setCoords(0, 0, 100, 100)
    # fill in background
    m_win.setBackground("black")
    # run loop
    for i in range(1000):
        # plot one pixel
        m_win.plot(m_sim.ball.getX(),m_sim.ball.getY(),"white")
        m_sim.loop()
        time.sleep(.01)
    # wait for click
    m_win.getMouse()

main()
