MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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


# PROGRAM
def resources_check(user_selection):
    required_water = MENU[user_selection]["ingredients"].get("water", 0)
    required_milk = MENU[user_selection]["ingredients"].get("milk", 0)
    required_coffee = MENU[user_selection]["ingredients"].get("coffee", 0)

    if (resources["water"] < required_water or
            resources["milk"] < required_milk or
            resources["coffee"] < required_coffee):
        return False
    else:
        return True


def print_report(resource, user_selection):
    for key, value in resource.items():
        if value < MENU[user_selection]["ingredients"].get(key, 0):
            print(f"{key}: {value}ml")


def process_order(user_selection):
    enough_resources = resources_check(user_selection)

    if enough_resources:
        # Process coins
        print("Please insert coins")
        quarters = int(input("How many quarters? "))  # 25 cents
        dimes = int(input("How many dimes? "))  # 10 cents
        nickels = int(input("How many nickels? "))  # 5 cents
        pennies = int(input("How many pennies? "))  # 1 cent

        total_in_pennies = (quarters * 25) + (dimes * 10) + (nickels * 5) + (pennies * 1)
        total_in_usd = total_in_pennies / 100

        cost = MENU[user_selection]['cost']

        if total_in_usd < MENU[user_selection]["cost"]:
            print(f"Sorry, you only have ${total_in_usd:,.2f}. The {user_selection} costs ${cost:,.2f}.")
        else:
            resources["water"] -= MENU[user_selection]["ingredients"]["water"]
            resources["milk"] -= MENU[user_selection]["ingredients"].get("milk", 0)
            resources["coffee"] -= MENU[user_selection]["ingredients"]["coffee"]

            change = total_in_usd - MENU[user_selection]["cost"]

            print(f"You gave me ${total_in_usd:,.2f} and the cost of your "
                  f"{user_selection} is ${MENU[user_selection]['cost']:,.2f}.")
            print(f"Here is your {user_selection} and your ${change:,.2f} change. Have a nice day.")
    else:
        print(f"Sorry, there's not enough of the following resources for a {user_selection}: ")
        print_report(resources, user_selection)


while True:
    user_input = input("What would you like? (espresso/latte/cappuccino)").lower()
    if user_input == "off":
        quit()
    elif user_input == "report":
        print_report(resources, user_input)

    while user_input != "espresso" and user_input != "latte" and user_input != "cappuccino":
        print("Please select a valid option...")
        user_input = input("What would you like? (espresso/latte/cappuccino)").lower()
        if user_input == "off":
            quit()
        elif user_input == "report":
            print(resources)

    resources_check(user_input)
    process_order(user_input)

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino)
# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
# TODO: 3. Print report.
# TODO: 4. Check resources sufficient?
# TODO: 5. Process coins.
# TODO: 6. Check transaction successful?
# TODO: 7. Make Coffee.
