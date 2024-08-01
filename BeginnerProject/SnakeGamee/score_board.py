from turtle import Turtle, Screen

# Tips: put inconstant variable on top
Alignment = 'center'
Font = 'Comic Sans'


class ScoreBoard(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.highest_score = 0  # save highest score to json file

		self.color('white')
		self.hideturtle()
		self.penup()
		self.goto(0, 265)
		self.update_score()

	def update_score(self):
		self.clear()
		self.write(f"Score: {self.score}", align=Alignment, font=(Font, 18, 'bold'))
		if self.score > self.highest_score:
			self.highest_score = self.score

	def increase_score(self):
		self.score += 1
		self.update_score()

	def lose(self):
		self.goto(0, 0)
		self.color('white')
		# fix this with format
		self.write(f"      You Lose\n Highest Score: {self.highest_score}", align=Alignment, font=(Font, 25, 'bold'))
