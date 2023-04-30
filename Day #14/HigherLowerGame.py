"""
Higher or Lower Game
the user guesses which of two celebrities has more followers
"""
from game_data import data
import random
from art import logo, vs
from replit import clear


# converts the dictionary to an f sting
def name_split(save_d):
    name = save_d["name"]
    disc = save_d["description"]
    coun = save_d["country"]
    return f"{name}, a {disc}, from {coun}"


loop_game = ""
# game loop, will end if user enter n and doesn't want to continue
while loop_game != "n":
    score = 0
    score_cur = 0
    score_t = 1
    # loop will end if the user enters the wrong answer
    while score_t == 1:
        print(logo)
        if score > 0:
            print(f"Your score is {score}")
        if score_cur == 0:
            save_1 = random.choice(data)
            print("Compare A: " + name_split(save_1))
            save_1_foll = save_1["follower_count"]
            print(vs)
            save_2 = random.choice(data)
            print("Compare B: " + name_split(save_2))
            save_2_foll = save_2["follower_count"]
        if score_cur > 0:
            save_1 = save_2
            save_1_foll = save_1_foll
            print("Compare A: " + name_split(save_1))
            print(vs)
            save_2 = random.choice(data)
            print("Compare B: " + name_split(save_2))
            save_2_foll = save_2["follower_count"]
        if save_2_foll > save_1_foll:
            ans = "B"
        elif save_2_foll < save_1_foll:
            ans = "A"
        user_ans = input("Who has more followers? Type 'A' or 'B'")
        if user_ans == ans:
            score += 1
            score_cur += 1
        else:
            print("Wrong you lose.")
            score_t = 0
        clear()
    loop_game = input("would you like to continue? Type 'y' for yes, typer 'n' for no. ")
