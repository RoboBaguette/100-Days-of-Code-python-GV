from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.goto(-250, 260)
        self.write(arg=f"level: {self.score}", align="center", font=('Arial', 18, 'normal'))
        self.hideturtle()

    def update(self):
        self.score += 1
        self.clear()
        self.write(arg=f"level: {self.score}", align="center", font=('Arial', 18, 'normal'))

    def game_done(self):
        self.goto(0, 0)
        self.write(arg="Game over", align="center", font=('Arial', 24, 'normal'))