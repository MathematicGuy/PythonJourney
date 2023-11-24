from turtle import Turtle, Screen

Up = 90
Down = 270
Left = 180
Right = 0
move_distance = 20


class snake:

	def __init__(self, length, color):
		self.length = length
		self.color = color

		self.space = 0
		self.body = []
		self.createSnake()
		self.head = self.body[0]

	def createSnake(self):
		for position in range(self.length):
			self.add_block((self.space, 0))
			self.space -= 20
		Screen().update()

	def add_block(self, position):
		new_block = Turtle('square')
		new_block.color(self.color)
		new_block.penup()
		new_block.goto(position)
		self.body.append(new_block)
		print(self.body)

	def extend(self):
		# add new block at last position
		self.add_block(self.body[-1].position())  # get .position is a turtle function

	def move(self):
		# By making each block follow its adj block. Snake can move freely
		for pos in range(len(self.body) - 1, 0, -1):  # range(start=len(self.body), end=0, step=-1) >> pos: 2,1
			# Extract x, y coordinates of snake_body
			# Making the last block follow its adj block
			new_x = self.body[pos - 1].xcor()
			new_y = self.body[pos - 1].ycor()
			self.body[pos].goto(new_x, new_y)

		self.head.forward(move_distance)

	def up(self):
		if self.head.heading() != Down:
			self.head.setheading(Up)
			print('Up')

	def down(self):
		if self.head.heading() != Up:
			self.head.setheading(Down)
			print('Down')

	def turn_right(self):
		if self.head.heading() != Left:
			self.head.setheading(Right)
			print('Right')

	def turn_left(self):
		if self.head.heading() != Right:
			self.head.setheading(Left)
			print('Left')
