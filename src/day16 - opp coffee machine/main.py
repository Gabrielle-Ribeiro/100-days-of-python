from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

coffe_machine_is_on = True

while(coffe_machine_is_on):

    user_answer = input("What would you like? (" + menu.get_items() + "): ").lower()

    if user_answer == "off":
        coffe_machine_is_on = False
    elif user_answer == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        item = menu.find_drink(user_answer)

        if item != None:
            is_enough_resources = coffee_maker.is_resource_sufficient(item)
            is_payment_successful = money_machine.make_payment(item.cost)
            if is_enough_resources and is_payment_successful:
                coffee_maker.make_coffee(item)
        else:
            print("Sorry! We don't have this drink. Please choose one of our options.")
