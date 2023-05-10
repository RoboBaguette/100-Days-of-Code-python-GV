from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(pos)
        self.write(arg=f"{self.score}", align="center", font=('Arial', 32, 'normal'))
        self.hideturtle()

    def update(self):
        self.score += 1
        self.clear()
        self.write(arg=f"{self.score}", align="center", font=('Arial', 32, 'normal'))

    def game_done(self):
        self.goto(0, 0)
        self.write(arg="Game over", align="center", font=('Arial', 24, 'normal'))
