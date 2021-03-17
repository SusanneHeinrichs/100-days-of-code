from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys

my_coffee_maker = CoffeeMaker()
my_menu = Menu()
my_money_machine = MoneyMachine()

machine_running = True
while machine_running:
    different_beverages = my_menu.get_items()
    user_choice = input(f"What do you want? {different_beverages}:")
    if user_choice == 'OFF':
        sys.exit(0)
    elif user_choice == 'report':
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        beverage = my_menu.find_drink(user_choice)
        if my_coffee_maker.is_resource_sufficient(beverage):
            if my_money_machine.make_payment(beverage.cost):
                my_coffee_maker.make_coffee(beverage)
                my_coffee_maker.report()





