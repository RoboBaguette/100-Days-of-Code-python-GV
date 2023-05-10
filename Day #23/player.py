from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, -260)

    def next_level(self):
        self.goto(0, -260)

    def up(self):
        self.forward(10)

    def move_right(self):
        self.goto(self.xcor()+10, self.ycor())

    def move_left(self):
        self.goto(self.xcor()-10, self.ycor())
