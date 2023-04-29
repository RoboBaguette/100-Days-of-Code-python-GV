"""
in the secret auction program the bidders do not know the bid ofg the last person
the users will enter their name and bid once all bidders entered their bids the winner is announced
"""
from replit import clear
import art

print(art.logo)
print("\n\nwelcome to the secret auction program.")
# initializing variables for the names and values of the bids
bid_current = 0
bid_name_current = ''
bid_new = 0
bid_new_name = ''
new_bid = ''
# bidding sequence loop
while new_bid != "no":
    bid_new_name = input("What is your name? ")
    bid_new = int(input("What is your bid?: $"))
    if bid_new > bid_current:
        bid_current = bid_new
        bid_name_current = bid_new_name
    new_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    # clear the screen so the next user can't see what the previous user did
    if new_bid == 'yes':
        clear()
    else:
        clear()
        break
print(f"The winners is {bid_name_current} with a bid of ${bid_current}.")
