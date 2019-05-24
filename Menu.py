from graphics import *
from Level import *
class Menu:

	box_size = 4

	def __init__(self, num_of_levels):
		self.num_of_levels = num_of_levels
		self.win_x = 100.0
		self.win_y = 100.0
        # create window
		self.m_win = GraphWin( ("Menu"), 1000, 500)
		self.m_win.setCoords(0, 0, self.win_x, self.win_y)
		self.m_win.setBackground("light blue")
		self.r_levels = [None] * self.num_of_levels
		self.t_levels = [None] * self.num_of_levels
		self.prompt = Text(Point(50, 80),"Please Choose A Level")
		self.prompt.draw(self.m_win)

		for i in range(self.num_of_levels):
			center = [((i%7 +1) * self.win_x / 8), (self.win_y - ((i//7+1) * self.win_y / 3) )]

			self.r_levels[i] = Rectangle(Point(center[0] - Menu.box_size, center[1] - Menu.box_size), Point(center[0] + Menu.box_size, center[1] + Menu.box_size))

			self.t_levels[i] = Text(Point(center[0], center[1]), str(i+1))

			self.r_levels[i].draw(self.m_win)
			self.t_levels[i].draw(self.m_win)

		


	def get_level(self):
		pt = self.m_win.getMouse()
		x = pt.getX()
		y = pt.getY()

		for i in range(self.num_of_levels):
			r = self.r_levels[i]
			if x > r.getP1().getX() and x < r.getP2().getX() and y > r.getP1().getY() and y < r.getP2().getY():
				r.undraw()
				r.setFill("yellow")
				r.draw(self.m_win)
				
				return (i+1)
