from turtle import Turtle, Screen
import random

bob = Turtle()
total_turn = 3
colors = ['#001219', '#005f73', '#0a9396', '#94d2bd', '#e9d8a6', '#ca6702', '#f2bac9', '#baf2e9', '#83e377', '#54478c', '#ff0000']

for i in range(20):
    for turn in range(total_turn):
        bob.forward(100)
        bob.left(360/total_turn)
    bob.color(random.choice(colors))
    total_turn += 1    
      
    
   
