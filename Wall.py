from graphics import *
import random
class Wall:

	color_cycle = ["red","yellow", "pink", "blue", "purple"]
	i = 0

	def __init__(self, p_a, p_b, draw, m_win):
		self.llx = p_a.getX()
		self.lly = p_a.getY()
		self.urx = p_b.getX()
		self.ury = p_b.getY()
		self.wall = Rectangle( Point(self.llx, self.lly), Point(self.urx, self.ury))
		self.wall.setFill(Wall.color_cycle[Wall.i])
		self.draw = draw

		if self.draw:
			self.wall.draw(m_win)


	def change_color(self):
		if self.draw:

			prev = Wall.i
			while Wall.i == prev:
				Wall.i = random.randint(0, (len(Wall.color_cycle) - 1))


			self.wall.setFill(Wall.color_cycle[Wall.i])
