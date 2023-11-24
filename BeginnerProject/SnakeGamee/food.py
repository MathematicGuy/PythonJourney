# create random dots base on (x,y) axis
import random
from turtle import Turtle


def random_coords():
	return random.randint(-280, 280)

x = random_coords()
y = random_coords()


class Food(Turtle):
	def __init__(self):
		super().__init__()

		# Able to use these commands bc they are inherited from the super class
		self.shape('circle')
		self.shapesize(stretch_len=0.7, stretch_wid=0.7)
		self.color('white')
		self.speed('fastest')
		self.penup()
		self.goto(x, y)

	def refresh(self):
		self.goto(random_coords(), random_coords())



