from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(arg=f"score: {self.score} High Score: {self.high_score}", align="center", font=('Arial', 18, 'normal'))
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(arg=f"score: {self.score} High Score: {self.high_score}", align="center", font=('Arial', 18, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))
        self.score = 0
        self.update()

    def game_done(self):
        self.goto(0, 0)
        self.write(arg="Game over", align="center", font=('Arial', 24, 'normal'))