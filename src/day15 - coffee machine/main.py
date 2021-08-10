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
    "coins": 0.0,
}

is_on = True

def report():
    print("Water: " + str(resources['water']) + "ml")
    print("Milk: " + str(resources['milk']) + "ml")
    print("Coffee: " + str(resources['coffee']) + "g")
    print("Money: ${:.2}".format(resources['coins']))


def check_resources_sufficient(type_coffee):
    water = MENU[type_coffee]['ingredients']['water']
    milk = MENU[type_coffee]['ingredients']['milk']
    coffee = MENU[type_coffee]['ingredients']['coffee']

    if resources['water'] >= water and resources['milk'] >= milk and resources['coffee'] >= coffee:
        return True
    if resources['water'] < water:
        print("Sorry there is not enough water.")
    if resources['milk'] < milk:
        print("Sorry there is not enough milk.")
    if resources['coffee'] < coffee:
        print("Sorry there is not enough coffee.")
    return False    


def process_coins(quarter, dimes, nickles, pennies, type_coffee):
    total =  quarter * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    cost = MENU[type_coffee]['cost']

    if total < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = total - cost
        resources['coins'] += cost
        if change > 0:
            print("Here is ${:.2f} dollars in change.".format(change))
        return True

def make_coffee(type_coffee):
    resources['water'] -= MENU[type_coffee]['ingredients']['water']
    resources['milk'] -= MENU[type_coffee]['ingredients']['milk']
    resources['coffee'] -= MENU[type_coffee]['ingredients']['coffee']

    print(f"Here is your {type_coffee}. Enjoy!")

while is_on:
    answer = input("What would you like? (espreso/latte/cappuccino): ").lower()

    if answer == "report":
        report()
    elif answer == "off":
        is_on = False
    elif answer == "latte" or answer == "cappuccino" or answer == "espresso":
        if check_resources_sufficient(answer):
            print("Please insert coins.")
            quarter = int(input("How many quartes? "))
            dimes = int(input("How many dimes? "))
            nickles = int(input("How many nickles? "))
            pennies = int(input("How many pennies? "))

            if process_coins(quarter, dimes, nickles, pennies, answer):
                make_coffee(answer)
    else:
        print("Command not recognized.")