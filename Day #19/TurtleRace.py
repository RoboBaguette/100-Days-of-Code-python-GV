"""
the turtle race program, window will pop up to make your bet, then the race will start
if the turtle that you bet on wins the race you win the bet
"""

from turtle import Turtle, Screen
import random


start_race = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle do you thing will, enter a color: ")
colors = ["red", "blue", "green", "yellow", "orange", "purple"]
val = -70
turtle_list =[]
win_color = ""
# the loop crates the turtle objects and moves them to the correct position
for t in range(0, 6):
    tom = Turtle(shape="turtle")
    tom.penup()
    tom.color(colors[t])
    tom.goto(x=-230, y=val)
    val += 30
    turtle_list.append(tom)


if user_bet:
    start_race = True

# the game loop will end once the turtle object crosses the finish line
while start_race:
    for turt in turtle_list:
        turt.forward(random.randint(0,10))
        if turt.xcor() > 230:
            start_race = False
            win_color = turt.pencolor()
            if user_bet == win_color:
                print(f"you have won your bet, the turtle {win_color} has won the race")
            else:
                print(f"you have lost your bet, the turtle {win_color} has won the race")

screen.exitonclick()