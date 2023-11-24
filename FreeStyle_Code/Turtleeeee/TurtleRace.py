import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=700, height=600)
turtle.speed('fastest')
# define Turtle
turtle_name = []
turtle_list = []
total_racer = 6
for i in range(total_racer):
    random_name = chr(random.randint(65, 90))
    turtle_name.append(random_name)  # random names
print(turtle_name)

color_palate = ['#001219', '#005f73', '#0a9396', '#94d2bd', '#e9d8a6', '#ca6702', '#f2bac9', '#baf2e9', '#83e377',
                '#54478c', '#ff0000']

# Start Position
next_pos = 0
for pos, racer in enumerate(turtle_name):
    racer = Turtle(shape='turtle')
    turtle_list.append(turtle_name[pos])
    racer.color(color_palate[pos])
    pos += 1

    racer.penup()
    next_pos += 30
    racer.goto(-270, -100 + next_pos)
    racer.pendown()

is_race_on = False
user_bet = screen.textinput(title="Make your Bet",
                            prompt=f"Guess who would win {turtle_name}: ".lower())
print('Your bet: ', user_bet)
if user_bet:
    is_race_on = True
while is_race_on:
    if racer.xcor() > 270:
        is_race_on = False
        if user_bet == (turtle_name[pos]).lower():
            print("Your guess is right")
            print(f'{turtle_name[pos]} is the Winner')
        else:
            print(f'Sorry but {turtle_name[pos]} is the Winner')
    for pos, racer in enumerate(turtle_list):
        random_jump = random.randint(0, 10)
        racer.forward(random_jump)
screen = Screen()
screen.exitonclick()
