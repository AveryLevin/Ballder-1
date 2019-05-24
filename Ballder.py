from graphics import *
from Level import *
from Menu import *
class Ballder:

	num_of_levels = 14

	def __init__(self):

		self.levels = [None] * Ballder.num_of_levels

		self.menu = Menu(Ballder.num_of_levels)

		#for i in range(Ballder.num_of_levels):
		#	self.levels[i] = Level(i, i%2, (i%2 == 0))


	def loop(self):
		print("returned level:", self.menu.get_level())

		


def main():
	b = Ballder()
	b.loop()

main()