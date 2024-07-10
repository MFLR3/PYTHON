from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while True:
    user_input = input("What would you like? (" + menu.get_items()[:-1] + ")...").lower()
    if user_input == "off":
        quit()
    elif user_input == "report":
        print(f"Report after last purchase")
        print(coffee_maker.report())
        money_machine.report()

    while user_input != "espresso" and user_input != "latte" and user_input != "cappuccino":
        print("Please select a valid option...")
        user_input = input("What would you like? (" + menu.get_items()[:-1] + ")...").lower()
        if user_input == "off":
            quit()
        elif user_input == "report":
            print(coffee_maker.report())

    # resources_check(user_input)
    user_selection = menu.find_drink(user_input)

    if coffee_maker.is_resource_sufficient(user_selection):
        # make payment
        if money_machine.make_payment(user_selection.cost):
            coffee_maker.make_coffee(user_selection)

    print(f"\nReport after last purchase")
    print(coffee_maker.report())
    money_machine.report()
    print()
