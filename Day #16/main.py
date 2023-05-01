"""
Coffee Machine
"""
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_moneymachine = MoneyMachine()
by_coffeemaker = CoffeeMaker()
cy_menu = Menu()

close = ""
while close != "n":
    options = cy_menu.get_items()
    drink = input(f"What would you like ({options}): ")
    if drink == "report":
        by_coffeemaker.report()
        my_moneymachine.report()
    elif drink == "off":
        close = "n"
    else:
        drink_n = cy_menu.find_drink(drink)
        if by_coffeemaker.is_resource_sufficient(drink_n):
            if my_moneymachine.make_payment(drink_n.cost):
                by_coffeemaker.make_coffee(drink_n)
