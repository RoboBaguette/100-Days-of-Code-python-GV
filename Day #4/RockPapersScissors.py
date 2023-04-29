import random

# images for the choices
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list_output = [rock, paper, scissors]
list_choice = ["rock", "paper", "scissors"]
print("Welcome to the rock paper scissors game.")
user_val = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# conditional statements to check if user follows the rules, then the computer randomly chooses an option
if user_val >= 3 or user_val < 0:
    print("\n")
else:
    print(f"You have chosen {list_choice[user_val]}.")
    print(list_output[user_val])
    comp_val = random.randint(0, 2)
    print(f"The computer has chosen {list_choice[comp_val]}.")
    print(list_output[comp_val])
# conditional statements to determine who won
if user_val >= 3 or user_val < 0:
    print("You typed an invalid number, you can't follow instructions you lose ")
elif user_val == 0 and comp_val == 2:
    print("You have won.\nThe game has ended.")
elif user_val == 1 and comp_val == 0:
    print("You have won.\nThe game has ended.")
elif user_val == 2 and comp_val == 1:
    print("You have won.\nThe game has ended.")
elif user_val == comp_val:
    print("You have tied.\nThe game has ended.")
else:
    print("You have lost.\nThe game has ended.")
