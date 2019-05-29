from graphics import *
from Level import *
from Menu import *
class Ballder:

	num_of_levels = 14

	def __init__(self):

		
		self.levels = [None] * Ballder.num_of_levels
		self.win = False
		self.menu = Menu(Ballder.num_of_levels)
		self.completed_levels = [False] * Ballder.num_of_levels



	def launch_level(self):
		self.lvl = self.menu.get_level()
		print("returned level:", self.lvl)
		self.level = Level(self.lvl, (self.lvl+1)//2, (self.lvl%2 == 0))
		return self.level.run_game()

	def main_loop(self):
		is_complete = self.launch_level()		
		self.menu.update_lvl(self.lvl, is_complete)
		self.completed_levels[self.lvl-1] = is_complete
		self.check_for_win()

	def check_for_win(self):
		self.win = True
		for i in self.completed_levels:
			if i == False:
				self.win = False
				break

		if self.win:
			print("You beat the game!")
			self.menu.display_win_screen()


def main():
	b = Ballder()
	while b.win == False:
		b.main_loop()

main()