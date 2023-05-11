"""
The States game, user enters the name of the state if correct the name of the state will appear on the map
"""
import turtle
import pandas

# screen/game set up
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
num_of_states = []

# open csv file
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

# game loop
while len(num_of_states) < 50:
    answer_state = screen.textinput(title=f"{len(num_of_states)}/50 states guessed", prompt="name another state").title()

    # check for state
    if (answer_state in states) and answer_state not in num_of_states:
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        num_of_states.append(answer_state)
    if answer_state == "Exit":
        missing_states = [s for s in states if s not in num_of_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

