from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.setheading(random.choice([45, 135, 225, 315]))
        self.speed = 0.1

    def move(self):
        self.forward(15)

    def score(self):
        self.goto(0, 0)
        self.setheading(random.choice([45, 135, 225, 315]))
        self.speed = 0.1

    def bounce_wall(self):
        heading = self.heading()
        if heading == 0:
            heading_new = 180
        elif heading == 180:
            heading_new = 0
        else:
            heading_new = 360 - heading
        self.setheading(heading_new)

    def bounce_paddle(self):
        heading = self.heading()
        if heading < 90 or 180 < heading < 270:
            heading += 90
        elif heading > 270 or 90 < heading < 180:
            heading -= 90
        self.setheading(heading)
        self.speed *= 0.9
