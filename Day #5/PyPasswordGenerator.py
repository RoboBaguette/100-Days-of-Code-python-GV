"""
the password generator will prompt the user for to input the number of letters, numbers, and symbols
then randomly chooses the characters, shuffles and combines them
"""
import random

# List of all characters that can be used in the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# the main text and te input prompts
print("Welcome to the PyPassword Generator!")
num_let = int(input("How many letters would you like in your password?\n"))
num_sym = int(input("How many numbers would you like in your password?\n"))
num_numm = int(input("How many numbers would you like in your password?\n"))
# for the number entered it adds a random characters into the list
pass_list = []
for c in range(1, num_let + 1):
    pass_list.append(random.choice(letters))
for n in range(1, num_numm + 1):
    pass_list.append(random.choice(numbers))
for s in range(1, num_sym + 1):
    pass_list.append(random.choice(symbols))
# the list is shuffled then turned into a string
random.shuffle(pass_list)
pas = ""
for c in pass_list:
    pas += c
# the password is displayed
print(f"Here is your password: {pas} ")
