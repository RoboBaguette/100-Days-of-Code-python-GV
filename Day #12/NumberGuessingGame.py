"""

"""
from replit import clear
import random

# function for the game difficulty
def game_mode(mode):
    if mode == "easy":
        att = 10
    else:
        att = 5
    return att

# loop returns 1 if the number is guessed, returns 0 otherwise
def game_loop(w):
    num = random.randint(1, 100)
    ans = 0
    for n in range(0, game_mode(w)):
        print(f"You have {game_mode(w) - n} attempts remaining to guess the number.")
        guess_c = int(input("Make a guess: "))
        if guess_c == num:
            ans = 1
            break
        elif guess_c > num:
            print("Too high")
        elif guess_c < num:
            print("Too low")
    if ans == 1:
        return 1
    else:
        return 0


play = ""
# game loop, stops if user doest want to play again
while play != "n":
    print("Welcome to the Number Guessing Game!\nIm thinking of a number between 1 and 100.")
    diff = input("Chosse a dificulty. Type 'easy' or 'hard': ")
    if diff == "easy" or diff == "hard":
        a = game_loop(diff)
        if a == 1:
            print("You got it!\nYou WIN")
        else:
            print("Wrong!!!\nYou lose.")
    else:
        print("Error.\nYour input was not recocnized")
    play = input("Would you like to play again. Type 'y' for yes or 'n' for no.")
    clear()
