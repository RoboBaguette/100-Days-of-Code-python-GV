import time
from turtle import Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# initializing objects
scoreboard = Scoreboard()
player = Player()
car = Cars()

# detecting input from keys
screen.listen()
screen.onkey(key="Up", fun=player.up)
screen.onkey(key="Left", fun=player.move_left)
screen.onkey(key="Right", fun=player.move_right)


game_on = True
while game_on:
    time.sleep(car.move_distance)
    screen.update()

    car.move_cars()

    # move to next level
    if player.ycor() > 260:
        car.clear_car()
        scoreboard.update()
        player.next_level()
        car.level_up()

    # detect collisions
    if car.detect_collision(player):
        scoreboard.game_done()
        game_on = False


screen.exitonclick()