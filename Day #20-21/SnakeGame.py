"""
Snake Game
"""
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# setup for the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
game_on = True

# initializing game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# detecting input from keys
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Down", fun=snake.down)

#game loop
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detecting collision with food
    if snake.head.distance(food) < 15:
        food.respawn()
        scoreboard.score += 1
        scoreboard.update()
        snake.extend()

    # detecting collision with walls
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        scoreboard.reset()
        snake.reset()

    # detecting collision with tail
    if snake.collision():
        scoreboard.reset()
        snake.reset()

screen.exitonclick()