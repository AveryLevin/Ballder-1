from graphics import *
from Level import *
from Simulation import *
class Menu:

	box_size = 4

	def __init__(self, num_of_levels):
		self.num_of_levels = num_of_levels
		self.win_x = 200.0
		self.win_y = 100.0
        # create window
		self.m_win = GraphWin( ("Menu"), 1000, 500, autoflush=False)
		self.m_win.setCoords(0, 0, self.win_x, self.win_y)
		self.m_win.setBackground("light blue")
		self.r_levels = [None] * self.num_of_levels
		self.w_levels = [None] * self.num_of_levels
		self.t_levels = [None] * self.num_of_levels
		self.title = Text(Point(100, 80),"Welcome to BALLDER")
		self.title.setSize(30)
		self.title.setTextColor("dark green")
		self.title.draw(self.m_win)
		self.prompt = Text(Point(100, 60),"Please Choose A Level")
		self.prompt.draw(self.m_win)


		for i in range(self.num_of_levels):
			center = [((i%7 +1) * self.win_x / 8), (self.win_y - ((i//7+1) * self.win_y / 3) )]

			self.r_levels[i] = Rectangle(Point(center[0] - Menu.box_size, center[1] - Menu.box_size), Point(center[0] + Menu.box_size, center[1] + Menu.box_size))
			self.w_levels[i] = Wall(Point(center[0] - Menu.box_size, center[1] - Menu.box_size), Point(center[0] + Menu.box_size, center[1] + Menu.box_size), False, self.m_win)

			self.t_levels[i] = Text(Point(center[0], center[1]), str(i+1))

			self.r_levels[i].draw(self.m_win)
			self.t_levels[i].draw(self.m_win)

		self.background = Simulation(0.07, 200, 100, self.w_levels, 1.0, "blue", self.m_win)
		
		self.background.set_vel([20,30])

		


	def get_level(self):

		is_valid = False
		i = 0
		while is_valid == False:

			self.background.loop()
			if i%2 == 0:
				update(30)

			i += 1
			pt = self.m_win.checkMouse()
			if pt != None:
				x = pt.getX()
				y = pt.getY()

				for i in range(self.num_of_levels):
					r = self.r_levels[i]
					if x > r.getP1().getX() and x < r.getP2().getX() and y > r.getP1().getY() and y < r.getP2().getY():
						r.undraw()
						r.setFill("yellow")
						r.draw(self.m_win)
						is_valid = True
						return (i+1)


	def update_lvl(self, level_num, is_complete):


		self.r_levels[level_num-1].undraw()

		center = [(((level_num-1)%7 +1) * self.win_x / 8), (self.win_y - (((level_num-1)//7 + 1) * self.win_y / 3) )]

		self.r_levels[level_num-1] = Rectangle(Point(center[0] - Menu.box_size, center[1] - Menu.box_size), Point(center[0] + Menu.box_size, center[1] + Menu.box_size))

		if is_complete:
			self.r_levels[level_num-1].setFill("green")

		self.r_levels[level_num-1].draw(self.m_win)
		# self.t_levels[level_num-1].draw(self.m_win)

	def display_win_screen(self):
		for i in range(self.num_of_levels):

			self.r_levels[i].undraw()
			self.t_levels[i].undraw()
		self.prompt.undraw()
		self.title.undraw()

		self.m_win.setBackground("yellow")

		self.title.setText("YOU BEAT THE GAME! CONGRATULATIONS!")
		self.title.draw(self.m_win)

		nice_img = Image(Point(100,45), "nice.gif")
		nice_img.draw(self.m_win)

		end_cred = Text(Point(100,10), "Press 'q' to quit")
		end_cred.draw(self.m_win)
		r_val = self.m_win.getKey()

		while r_val != "q":
			r_val = self.m_win.getKey()
		self.m_win.close()

