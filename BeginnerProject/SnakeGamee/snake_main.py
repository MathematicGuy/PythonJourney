from turtle import Screen
from snake_brain import snake
import time
from food import Food
from scoreBoard import ScoreBoard

# TODO-5: Create a scoreboard

# TODO-1: Setup Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('crimson')
screen.title('Second Snake Game')
screen.tracer(0)  # smoother animation. [action per frame]

# TODO-2: Create Snake body
Snake = snake(3, 'white')
apple = Food()
score_board = ScoreBoard()

screen.listen()  # listen before onkey()
screen.onkey(Snake.up, 'Up')
screen.onkey(Snake.down, 'Down')
screen.onkey(Snake.turn_right, 'Right')
screen.onkey(Snake.turn_left, 'Left')

# TODO-3: Control the Snake
is_alive = True
while is_alive:
	screen.update()
	time.sleep(0.1)  # delay time between block
	Snake.move()

	# TODO-4: Detect collision with food (head coords vs food coords)
	if Snake.head.distance(apple) < 15:
		print('nom nom nom')
		apple.refresh()
		Snake.extend()
		score_board.increase_score()

	# TODO-6: Detect wall collision (head coords ~ wall coords)
	if Snake.head.xcor() > 290 or Snake.head.xcor() < -290 or Snake.head.ycor() > 290 or Snake.head.ycor() < -290:
		is_alive = False
		score_board.lose()

	# TODO-7: Detect collision with tail
	for block in Snake.body[1:]:  # all block except the head
		if Snake.head.distance(block) < 15:
			is_alive = False
			score_board.lose()
# TODO-8: Replay ability (by clicking the screen)
screen.exitonclick()
