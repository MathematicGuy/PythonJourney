from turtle import *
import random
import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('../resources/nightSky.jpg', 84)
colors_palate = []
bob = Turtle()

# Extract color form image
for pos in range(len(colors)):
    first_color = colors[pos]  # get each color code for in colors
    rgb = first_color.rgb  # e.g. (255, 151, 210) extract rgb
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]

    colors_palate.append((r, g, b))

colormode(255)  # must-have for RGB
bob.speed('fastest')
bob.penup()
bob.goto(-350, -350)
bob.pendown()

total_dots = 15
total_lines = 10
jump_length = 50
for line in range(total_lines+1):
    bob.setheading(0)
    for dot in range(total_dots):
        bob.pencolor(random.choice(colors_palate))  # pick random color
        bob.dot(15)
        bob.penup()
        bob.forward(jump_length)

    bob.setheading(90)
    bob.forward(30)
    bob.setheading(180)
    bob.forward(total_dots*jump_length)
    bob.setheading(270)


ws = Screen()
ws.exitonclick()

