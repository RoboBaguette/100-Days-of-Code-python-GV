"""
Blackjack game
"""
import random
from replit import clear
import art

cards_list = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
cards = {
    "Ace": 11,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
}
cont = input("do you want to play a game of Blackjack? Type 'y' or 'n' ")
clear()
# loop for the Blackjack game, it will end when the user doesn't want to play anymore
while cont != "n":
    print(art.logo)
    user_cards = [cards_list[random.randint(0, 12)], cards_list[random.randint(0, 12)]]
    print(user_cards)
    user_val = 0
    comp_val = 0
    # calculate initial total value of the users cards
    for num, val in enumerate(user_cards):
        if val == "Ace":
            user_val += int(input("You Have pulled an Ace would you like its value to be 1 or 11"))
        else:
            user_val += cards[val]
    comp_cards = [cards_list[random.randint(0, 12)], cards_list[random.randint(0, 12)]]
    # calculate initial total value of the computers cards
    for num, val in enumerate(comp_cards):
        if val == "Ace":
            a = random.randint(0, 1)
            if a == 0:
                comp_val += 11
            else:
                comp_val += 1
        else:
            comp_val += cards[val]
    print(f"the computers first card is\n{comp_cards[1]}")
    cont_n = input("Type 'y' to get another card, type 'n' to pass ")
    b = 2
    n = ""
    # loop for drawing cards, it will end when the user doesn't want anymore cards
    while cont_n != "n":
        user_cards.append(cards_list[random.randint(0, 12)])
        if user_cards[b] == "Ace":
            user_val += int(input("You Have pulled an Ace would you like its value to be 1 or 11 "))
        else:
            user_val += cards[user_cards[b]]
        b += 1
        print(user_cards)
        if user_val > 21:
            break
        cont_n = input("Type 'y' to get another card, type 'n' to pass ")
    # computing who won
    if user_val > 21:
        print(" you bust, you have lost the game.")
    else:
        c = 2
        while comp_val < user_val and comp_val < 21:
            comp_cards.append(cards_list[random.randint(0, 12)])
            comp_val += cards[comp_cards[c]]
            c += 1
    if comp_val > user_val and comp_val < 21:
        print(f"the comuters cards are\n{comp_cards}\nYou lose")
    elif comp_val > 21:
        print(f"the comuters cards are\n{comp_cards}\nYou win")
    elif comp_val < user_val and user_val < 21:
        print(f"the comuters cards are\n{comp_cards}\nYou win")
    cont = input("Would you like to play another game of Blackjack? Type 'y' or 'n' ")
    clear()
print("The game has ended\nGoodBye")
