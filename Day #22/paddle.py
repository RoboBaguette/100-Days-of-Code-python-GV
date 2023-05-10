from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.x = x
        self.goto(x, 0)

    def move_up(self):
        new_y = self.ycor()+20
        if new_y >= 250:
            new_y = 250
        self.goto(self.x, new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        if new_y <= -250:
            new_y = -250
        self.goto(self.x, new_y)
