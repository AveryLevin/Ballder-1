from Projectile import *
from Wall import *

class Simulation:
	'Class for running simulation'
	# acceleration for simulated world
	accel = -9.8

	def __init__(self, time_step, window_x, window_y, walls , elas, color, m_win):
		self.time_step = time_step
		self.x_vel = 0.0
		self.y_vel = 0.0
		self.window_x = window_x
		self.window_y = window_y
		# create projectile object
		self.ball = Projectile(2, elas, color, m_win)
		self.walls = walls
		self.x_bnc = False
		self.y_bnc = False
		self.m_win = m_win

	def set_vel(self, vel):
		self.x_vel = vel[0]
		self.y_vel = vel[1]

	def x_b(self):
		self.x_vel *= -self.ball.elasticity


	def y_b(self):
		self.y_vel *= -self.ball.elasticity

	def loop(self):

		# log last position
		x = self.ball.getX()
		y = self.ball.getY()

		# check for bounce occurence
		if self.check_for_x_bounce():
			self.x_b()
		if self.check_for_y_bounce():
			self.y_b()




		# accumulate position
		self.ball.setX(x + self.x_vel*self.time_step)
		self.ball.setY(y + self.y_vel*self.time_step + 0.5*Simulation.accel*(self.time_step**2) )

		bounce = self.check_for_wall_bounce(x,y)

		if (bounce == 1) :
			self.y_b()

		if (bounce == 2) :
			self.x_b()

		self.y_vel += 0.5*Simulation.accel*self.time_step
		# draw ball
		self.ball.draw()
		# provide debug position readouts
		#print("X:", self.ball.getX(), "\t", "Y:", self.ball.getY(), "\tACCELERATION:", (0.5*Simulation.accel*(self.time_step**2)))


	def check_for_x_bounce(self):
		rad = self.ball.radius

		if self.ball.getX() <= (0 + rad) or self.ball.getX() >= (self.window_x - rad):
			if self.x_bnc == False:
				#print("X BOUNCE!!")
				self.x_bnc = True
				return True
			else:
				return False
		else:
			self.x_bnc = False
			return False



	def check_for_y_bounce(self):
		rad = self.ball.radius

		if self.ball.getY() <= (0 + rad) or self.ball.getY() >= (self.window_y - rad):
			if self.y_bnc == False:
				#print("Y BOUNCE!!")
				self.y_bnc = True
				return True
			else:
				return False
		else:
			self.y_bnc = False
			return False


	def check_for_wall_bounce(self, x_prev, y_prev):
		rad = self.ball.radius

		
		for i in self.walls:
			if ( self.ball.getX() >= (i.llx-rad) and self.ball.getX() <= (i.urx+rad) and self.ball.getY() >= (i.lly-rad) and self.ball.getY() <= (i.ury+rad) ) :
				# ball has hit the wall somewhere

				if(x_prev >= (i.llx-rad) and x_prev <= (i.urx+rad)):
					# in last frame, ball was above or below wall

					if self.wall_bnc == False:
						print("Y BOUNCE!!")
						i.change_color()
						self.wall_bnc = True
						return 1
					else:
						return 0
				elif(y_prev >= (i.lly-rad) and y_prev <= (i.ury+rad)):
					# in last frame, ball was next to wall
					
					if self.wall_bnc == False:
						print("X BOUNCE!!")
						i.change_color()
						self.wall_bnc = True
						return 2
					else:
						return 0

		self.wall_bnc = False
		return 0

		

