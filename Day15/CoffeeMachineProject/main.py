MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


import sys


def resources_sufficient(user_choice):
    if (resources["water"] - MENU[user_choice]['ingredients']['water']) < 0:
        return 'water'
    elif (resources["milk"] - MENU[user_choice]['ingredients']['milk']) < 0:
        return 'milk'
    elif (resources['coffee'] - MENU[user_choice]['ingredients']['coffee']) < 0:
        return 'coffee'
    else:
        return 'yes'


def give_report(resources):
    print(f"Water:  {resources['water']} ml")
    print(f"milk: {resources['milk']} ml")
    print(f"coffee:  {resources['coffee']} g")
    print(f"Total profit: ${money_in_machine}")


machine_state = 'ON'
money_in_machine = 0
while machine_state == 'ON':
    user_choice = input('What would you like?(espresso/latte/capuccino):')
    if user_choice == 'OFF':
        sys.exit(0)
    if user_choice == 'Report':
        give_report(resources)

    # check if resources sufficient
    if resources_sufficient(user_choice) == 'yes':
        costs = MENU[user_choice]['cost']
        print(f'The {user_choice} costs {costs} $.')
        quarters = int(input("How many quarters (0.25$) do you want to input?"))
        dimes = int(input("How many quarters (0.10$) do you want to input?"))
        nickles = int(input("How many quarters (0.05$) do you want to input?"))
        pennies = int(input("How many quarters (0.01$) do you want to input?"))
        total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        if total >= costs:
            #if money suficient, output change
            change = round(total - costs, 3)
            print(f"Your change is {change}$")
            #calculate resources after production of beverage
            resources['water'] = resources['water'] - MENU[user_choice]['ingredients']['water']
            resources['milk'] = resources['milk'] - MENU[user_choice]['ingredients']['milk']
            resources['coffee'] = resources['coffee'] - MENU[user_choice]['ingredients']['coffee']
            money_in_machine += costs
            resources['Money'] = money_in_machine
            give_report(resources)
            print("Here is your latte. Enjoy :)")

        else:
            print("Sorry that's not enough money. Money refunded.")

    else:
        print(f'Sorry there is not enough {resources_sufficient(user_choice)}')

