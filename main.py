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


def resources_check(ingredients):
    is_enough = True
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return is_enough


def process_coins():
    print("Insert coins.")
    total_quart = int(input("How many quarters?:")) * 0.25
    total_di = int(input("How many dimes?:")) * 0.10
    total_ni = int(input("How many nickles?:")) * 0.05
    total_pe = int(input("How many pennies?:")) * 0.01
    total_of_money = total_pe + total_ni + total_di + total_quart
    return total_of_money


def make_coffee(items):
    for n in items:
        new_total = resources[n] - items[n]
        resources[n] = new_total


is_on = True
profit = 0

while is_on:

    decision = input("What would you like? (espresso/latte/cappuccino): ")

    if decision == "off":

        is_on = False

    elif decision == "report":

        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink = MENU[decision]
        if resources_check(drink["ingredients"]):
            total = (process_coins())
            if drink["cost"] > total:
                print(f"Sorry that's not enough money. Money Refunded.")
            else:
                if drink["cost"] <= total:
                    change = round(total - drink["cost"], 2)
                    print(f"Here is ${change} dollars in change")
                    make_coffee(drink["ingredients"])
                    profit += drink["cost"]
                    print(f"Here is your {decision}. Enjoy!")








