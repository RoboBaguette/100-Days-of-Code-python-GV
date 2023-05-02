"""
Program that creates a Damien Hirst esque painting
"""
import turtle as t
from turtle import Turtle, Screen
import random

t.colormode(255)


# function that returns a random RGB tuple
def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

# initializing the turtle object, its attributes and position
tom = Turtle()
tom.shape("circle")
tom.penup()
tom.setposition(-300, -280)
tom.pensize(50)
tom.pendown()
tom.speed("fastest")

# the loop create the painting by moving the object
for a in range(7):
    for _ in range(6):
        tom.forward(1)
        tom.penup()
        tom.forward(100)
        tom.pendown()
        tom.forward(1)
        tom.color(rand_color())
    tom.penup()
    tom.setheading(90)
    tom.forward(100)
    if a % 2 == 0:
        tom.setheading(180)
    else:
        tom.setheading(360)
    tom.pendown()

screen = Screen()
screen.exitonclick()


