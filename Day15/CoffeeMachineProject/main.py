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


def input_money():
    pay = int(input("How many quarters (0.25$) do you want to input?")) * 0.25
    pay += int(input("How many quarters (0.10$) do you want to input?")) * 0.1
    pay += int(input("How many quarters (0.05$) do you want to input?")) * 0.05
    pay += int(input("How many quarters (0.01$) do you want to input?")) * 0.01
    return pay


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
        beverage = MENU[user_choice]
        costs = beverage['cost']
        print(f'The {user_choice} costs {costs} $.')
        total = input_money()
        if total >= costs:
            # if money suficient, output change
            change = round(total - costs, 3)
            print(f"Your change is {change}$")
            # calculate resources after production of beverage
            for item in beverage['ingredients']:
                resources[item] -= beverage['ingredients'][item]
            money_in_machine += costs
            resources['Money'] = money_in_machine
            give_report(resources)
            print(f"Here is your {user_choice}. Enjoy :)")

        else:
            print("Sorry that's not enough money. Money refunded.")

    else:
        print(f'Sorry there is not enough {resources_sufficient(user_choice)}')

