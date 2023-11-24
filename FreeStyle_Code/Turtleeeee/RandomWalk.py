from turtle import Turtle
import random

direction = [0,180,90,270]
RGB = []

color1 = ['#001219', '#005f73', '#0a9396', '#94d2bd', '#e9d8a6', '#ca6702', '#f2bac9', '#baf2e9', '#83e377', '#54478c', '#ff0000']

bob = Turtle()    
        
for i in range(1000):
    # bob.color(random.choice(color1))
    random_color = random.choice(color1)
    random_direction = random.choice(direction)
    
    bob.speed(30)
    bob.color(random_color)
    bob.pensize(8)
    bob.forward(60)
    bob.setheading(random_direction)
    