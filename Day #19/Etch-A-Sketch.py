"""
Etch-A-Sketch program tha uses the arrow keys to move the cursor, the 'c' key will clear the screen
"""
from turtle import Turtle, Screen

tom = Turtle()
tom.shape("turtle")
tom.color("black")

screen = Screen()


def move_fwds():
    tom.forward(10)


def move_bwds():
    tom.backward(10)


def turn_right():
    tom.right(10)


def turn_left():
    tom.left(10)


screen.listen()
screen.onkey(key="Up", fun=move_fwds)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Down", fun=move_bwds)
screen.onkey(key="c", fun=screen.resetscreen)
screen.exitonclick()
