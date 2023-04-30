"""
Coffee Machine
"""
from drink_ras import MENU, resources


# function to calculate how much money put into the machine
def pay_check():
    print("Please insert coins.")
    quar = float(input("How many quarters?: ")) * 0.25
    dime = float(input("How many dimes?: ")) * 0.1
    nick = float(input("How many nickles?: ")) * 0.05
    penn = float(input("How many pennies?: ")) * 0.01
    total_pay = quar + dime + nick + penn
    return total_pay


#  function to check if there are enough recodes to make the drink
def ing_check(drink_ing):
    for ing in drink_ing:
        if drink_ing[ing] > resources[ing]:
            return False
        else:
            return True


# function to change resources
def ing_red(drink_ing):
    for ing in drink_ing:
        resources[ing] -= drink_ing[ing]


close = ""
# exits loop if user enters 'off'
while close != "n":
    drink = input("(enter 'off' to exit)What would you like? (espresso/latte/cappuccino):")
    if drink == "report":
        water = resources["water"]
        milk = resources["milk"]
        coffee = resources["coffee"]
        print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}")
    elif drink == "espresso" or drink == "latte" or drink == "cappuccino":
        total_pay = pay_check()
        drink_info = MENU[drink]
        drink_ing = drink_info["ingredients"]
        if drink_info["cost"] <= total_pay:
            if ing_check(drink_ing):
                total_refun = total_pay - drink_info["cost"]
                print(f"Here is ${total_refun} in change")
                total_pay = 0
                ing_red(drink_ing)
                print(f"Here is your {drink}. Enjoy")
            else:
                print(f"sorry there is not enough ingredients")
                print("Money refunded")
                total_pay = 0
        elif drink_info["cost"] > total_pay:
            print("Sorry that is not enough money. Money refunded")
            total_pay = 0
    elif drink == "off":
        close = "n"
