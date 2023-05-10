"""
Pong
"""
from turtle import Turtle, Screen
import time
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

# setup for the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
game_on = True

# setup for the scoreboard
score_right = Scoreboard((30, 250))
score_left = Scoreboard((-30, 250))

paddle_right = Paddle(350)
paddle_left = Paddle(-350)
ball = Ball()

# detecting input from keys
screen.listen()
screen.onkey(key="Up", fun=paddle_right.move_up)
screen.onkey(key="Down", fun=paddle_right.move_down)
screen.onkey(key="w", fun=paddle_left.move_up)
screen.onkey(key="s", fun=paddle_left.move_down)

# game loop
while game_on:
    screen.update()
    time.sleep(ball.speed)
    ball.move()

    # detect ball bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    if (ball.distance(paddle_right) < 50 and ball.xcor() > 320) or (ball.distance(paddle_left) < 50 and ball.xcor() < -320):
        ball.bounce_paddle()

    # Detecting if ball has scored
    if ball.xcor() > 430:
        score_left.update()
        ball.score()
    if ball.xcor() < -430:
        score_right.update()
        ball.score()

    # detecting game win
    if score_right.score >= 10 or score_left.score >= 10:
        score_right.game_done()
        game_on = False


screen.exitonclick()